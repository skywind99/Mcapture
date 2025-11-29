# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['screen_ocr.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'pynput.keyboard._win32', 
        'pynput.mouse._win32',
        'PIL._tkinter_finder'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='화면OCR',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 콘솔 창 보이게 (상태 확인용)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # 아이콘 파일 있으면 'icon.ico' 추가
)
