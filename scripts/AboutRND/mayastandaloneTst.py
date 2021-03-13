#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,re,yaml,copy,sys
MAYA_LOCATION = r"C:\tools\Autodesk\Maya2018"
os.environ["MAYA_LOCATION"] = MAYA_LOCATION
os.environ["PATH"]= MAYA_LOCATION+"/bin;" + os.environ["PATH"]
PYTHON_LOCATION = MAYA_LOCATION + "/Python/Lib/site-packages"
# os.environ["PYTHONPATH"] = PYTHON_LOCATION
# sys.path.append(PYTHON_LOCATION)
#4
PTHON_HOME = MAYA_LOCATION + "/python"
os.environ["PYTHONPATH"] = PTHON_HOME

from maya import standalone
standalone.initialize()
print("initialized....ok....")