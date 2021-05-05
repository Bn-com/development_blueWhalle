#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = upEnv
__author__ = zhangben 
__mtime__ = 2021/3/24 : 9:47
__description__: 

THEOREM: A good programmer should wipe the butts of his predecessors in an amicable way,
    instead of reinventing a new butt.
        As long as this , code is far away from bugs, and with the god animal protecting
            I love animals. They taste delicious.
"""
import re,os,sys
from subprocess import check_call
if sys.hexversion > 0x03000000:
    import winreg
else:
    import _winreg as winreg

class Win32Environment(object):
    """Utility class to get/set windows environment variable"""
    def __init__(self, scope='system'):
        assert scope in ('user', 'system')
        self.scope = scope
        if scope == 'user':
            self.root = winreg.HKEY_CURRENT_USER
            self._subkey = 'Environment'
        else:
            self.root = winreg.HKEY_LOCAL_MACHINE
            self._subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        self._name = None
    @property
    def name(self):
        return self._name
    name.setter
    def name(self,name):
        self._name = name
    @property
    def subkey(self):
        return self._subkey
    @subkey.setter
    def subkey(self,key):
        self._subkey = key
    def getenv(self):
        try:
            key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
            value, _ = winreg.QueryValueEx(key, self.name)
        except WindowsError:
            value = ''
        return value

    def setenv(self,value,append=False):
        # Note: for 'system' scope, you must run this as Administrator
        if append: value = self.expandValue(self.name,value)
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, self.name, 0, winreg.REG_EXPAND_SZ, value)
        winreg.CloseKey(key)
        # For some strange reason, calling SendMessage from the current process
        # doesn't propagate environment changes at all.
        # TODO: handle CalledProcessError (for assert)
        check_call('''"%s" -c "import win32api, win32con; assert win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')"''' % sys.executable)
    def expandValue(self,value,expandTo=None):
        if not expandTo: oldvalue = self.getenv(self.name)
        if not expandTo: return value
        set_value_lst = [os.path.normpath(e_p) for e_p in  expandTo.split(';')]
        value_spl = value.split(';')
        for e_v in value_spl:
            new_pth_nrml = os.path.normpath(e_v)
            if not os.path.isdir(new_pth_nrml):continue
            if new_pth_nrml not in set_value_lst:
                set_value_lst.append(new_pth_nrml)
        return ";".join(set_value_lst)
    def contractValue(self,remove,source):
        src_spl = source.split(';')
        remove_spl = remove.split(';')
        for e_rm in remove_spl:
            if e_rm in src_spl:
                src_spl.remove(e_rm)
        return ";".join(src_spl)
    def delenv(self):
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(key, self.name)
        winreg.CloseKey(key)
        check_call(
            '''"%s" -c "import win32api, win32con; assert win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')"''' % sys.executable)


if __name__ == '__main__':
    winenv = Win32Environment()
    winenv.subkey = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Autodesk Maya {}".format(2016)
    winenv.name = "InstallLocation"
    print(winenv.getenv())