# run-demo.py
# simple example of gst-switch python api

# pass the path to the binaries:
# 

import argparse

import time
import subprocess

from gstswitch.helpers import PreviewSinks
from gstswitch.server import Server
from gstswitch.helpers import TestSources

def wait(secs):
    print("sleeping {} secconds...".format(secs))
    time.sleep(secs)

def main(args):

    print("running server")
    serv = Server(path=args.path)
    serv.run()

    wait(5)

    print("running source pattern=1")
    sources = TestSources(video_port=3000, audio_port=4000)
    sources.new_test_video(pattern=1)

    wait(5)

    print("running gst-switch-ui")
    # the & will run this in the background so control returns 
    # and we can bring up the 2nd source 

    # Replaced call with subprocess.Popen. 
    SwitchUi = subprocess.Popen("gst-switch-ui &",shell=True)

    wait(5)
       
    print("running source pattern=18")
    sources.new_test_video(pattern=18)

    raw_input("hit enter:")


    # Replaced pkill call with Popen.kill
    subprocess.Popen.kill(SwitchUi)
    serv.kill()

    

def pars_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path")
    args = parser.parse_args()
    return args

if __name__=='__main__':
    args=pars_args()
    main(args)
