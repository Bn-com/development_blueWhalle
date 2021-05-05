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

def tierpath(path,tier=0,normalize=True):
    if normalize: return os.path.abspath(normalJoinpath(path,"../"*tier))
    else: return os.path.abspath(joinpath(path,"../"*tier))
def tierfolder(path,tier=0):
    bsnm = os.path.basename(tierpath(path,tier))
    if not bsnm: bsnm = os.path.splitdrive(path)[0]
    return bsnm

def update_env(var,value):
    old_v = os.environ[var]
    old_v_spl = old_v.split(';')
    old_v_spl_unified = [unifiedpath(p) for p in old_v_spl]
    v_spl = value.split(';')
    for e_v in v_spl:
        e_v_unified = unifiedpath(e_v)
        if e_v_unified not in old_v_spl_unified:
            old_v_spl.append(e_v)
    os.environ[var] = ";".join(old_v_spl)

def sysPathAppend(path):
    sys_pth_unif = [unifiedpath(e_pth) for e_pth in sys.path]
    path_uni = unifiedpath(path)
    if path_uni not in sys_pth_unif: sys.path.append(path)
