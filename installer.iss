[Setup]
AppName=화면 OCR
AppVersion=1.0.0
AppPublisher=한국애니메이션고등학교
DefaultDirName={autopf}\ScreenOCR
DefaultGroupName=화면 OCR
OutputDir=Output
OutputBaseFilename=화면OCR_설치프로그램
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=admin
SetupIconFile=icon.ico

[Languages]
Name: "korean"; MessagesFile: "compiler:Languages\Korean.isl"

[Tasks]
Name: "desktopicon"; Description: "바탕화면 아이콘 만들기"; GroupDescription: "추가 아이콘:"; Flags: unchecked

[Files]
Source: "dist\화면OCR.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "tesseract\*"; DestDir: "{app}\tesseract"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\화면 OCR"; Filename: "{app}\화면OCR.exe"
Name: "{autodesktop}\화면 OCR"; Filename: "{app}\화면OCR.exe"; Tasks: desktopicon
Name: "{group}\화면 OCR 제거"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\화면OCR.exe"; Description: "화면 OCR 실행"; Flags: nowait postinstall skipifsilent

[Code]
function InitializeSetup(): Boolean;
begin
  Result := True;
  MsgBox('화면 OCR 프로그램을 설치합니다.' + #13#10 + 
         '설치 후 Ctrl+Shift+C 단축키로 사용하세요.', mbInformation, MB_OK);
end;
