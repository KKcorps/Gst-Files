import sys
import os


install_dir = os.getcwd()
sys.path.insert(0, install_dir+'/python-api')

from gstswitch.helpers import PreviewSinks
from gstswitch.server import Server
from gstswitch.helpers import TestSources

#path = os.getcwd()
#print path

#sys.path.insert(0, install_dir + 'gst-switch/python-api/gstswitch')

PATH = '/usr/bin/'
# The default location is '/usr/bin'. Change to wherever the gst-switch executables are located
serv = Server(path=PATH, video_port=3000, audio_port=4000)
serv.run()

sources = TestSources(video_port=3000, audio_port=4000)
sources.new_test_video()
sources.new_test_audio()


preview = PreviewSinks(preview_port=3001)
preview.run()
