import sys
import os
import time
from subprocess import call


install_dir = os.getcwd()
print install_dir+'/python-api'

sys.path.insert(0, install_dir+'/python-api')

from gstswitch.helpers import PreviewSinks
from gstswitch.server import Server
from gstswitch.helpers import TestSources

path = os.getcwd()

print path

#sys.path.insert(0, install_dir + 'gst-switch/python-api/gstswitch')

PATH = install_dir + '/tools/'
sys.path.insert(0, install_dir+ '/tools')
print PATH

# The default location is '/usr/bin'. Change to wherever the gst-switch executables are located
serv = Server(path=PATH, video_port=3000, audio_port=4000)
serv.run()

time.sleep(5)

sources = TestSources(video_port=3000, audio_port=4000)
sources.new_test_video(pattern=1)
call(["./tools/gst-switch-ui"])

time.sleep(5)
   
sources.new_test_video(pattern=18)
