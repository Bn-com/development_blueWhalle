#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = command
__author__ = Ben 
__mtime__ = 2021/4/5 : 14:02
__description__: 

THEOREM: A good programmer should wipe the butts of his predecessors in an amicable way,
    instead of reinventing a new butt.
        As long as this , code is far away from bugs, and with the god animal protecting
            I love animals. They taste delicious.
"""
import os,sys,re
def unifiedpath(path):
    """
        \\ > /
    :param path:
    :return:
    """
    return re.sub(r"\\","/",os.path.normpath(path))

def joinpath(*args):
    """
          join path return unified path    "\\" >> "/"
    :param args:
    :return:
    """
    return unifiedpath(os.path.join(*args))
def normalJoinpath(*args):
    return os.path.normpath(os.path.join(*args))