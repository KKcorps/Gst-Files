#!/bin/bash -ex 

gst_home=~/src/gst-switch

PATH=$gst_home/tools:$PATH
export PYTHONPATH=$gst_home/python-api

python run-demo.py --path $gst_home/tools/

