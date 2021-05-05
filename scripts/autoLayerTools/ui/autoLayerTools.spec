# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['autoLayerTools.py'],
             pathex=['F:\\development\\DevOnGithub\\scripts\\autoLayerTools\\ui'],
             binaries=[],
             datas=[],
             hiddenimports=['PySide.QtXml'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='autoLayerTools',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='F:\\development\\DevOnGithub\\scripts\\autoLayerTools\\ui\\icons\\autoLayerTools.ico')
