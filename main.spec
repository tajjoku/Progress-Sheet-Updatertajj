# -*- mode: python ; coding: utf-8 -*-

a = Analysis(['main.py'],
             datas=[('C:\Users\space\AppData\Local\Programs\Python\Python310\Lib\site-packages\google_api_python_client-2.65.0.dist-info\\*', 'google_api_python_client-2.65.0.dist-info')]
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
