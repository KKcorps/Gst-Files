#!/bin/bash -ex 

gst_home=~/Downloads/gst-switch-master/

PATH=$gst_home/tools:$PATH
export PYTHONPATH=$gst_home/python-api

python run-demo2.py --path $gst_home/tools/
