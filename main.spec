# -*- mode: python ; coding: utf-8 -*-

a = Analysis(['main.py'],
             datas=[('edit this', 'edit this')]
)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ProgressSheetUpdater.exe',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True,
          icon='icon.ico')
