; 화면 OCR 설치 프로그램 스크립트
; Inno Setup 6.0 이상 필요

[Setup]
; 기본 정보
AppName=화면 OCR
AppVersion=1.0.0
AppPublisher=한국애니메이션고등학교
AppPublisherURL=https://koreaanim.hs.kr
DefaultDirName={autopf}\ScreenOCR
DefaultGroupName=화면 OCR
OutputDir=Output
OutputBaseFilename=화면OCR_설치프로그램_v1.0.0
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=admin

; 설치 관련
AllowNoIcons=yes
DisableProgramGroupPage=yes
DisableWelcomePage=no

; UI
WizardStyle=modern
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\화면OCR.exe

[Languages]
Name: "korean"; MessagesFile: "compiler:Languages\Korean.isl"

[Tasks]
Name: "desktopicon"; Description: "바탕화면에 아이콘 만들기"; GroupDescription: "추가 아이콘:"; Flags: unchecked
Name: "startupicon"; Description: "Windows 시작 시 자동 실행"; GroupDescription: "추가 옵션:"; Flags: unchecked

[Files]
; 실행 파일
Source: "dist\화면OCR.exe"; DestDir: "{app}"; Flags: ignoreversion

; Tesseract OCR 엔진 및 언어 데이터
Source: "tesseract\*"; DestDir: "{app}\tesseract"; Flags: ignoreversion recursesubdirs createallsubdirs

; 추가 파일 (있다면)
; Source: "README.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; 시작 메뉴
Name: "{group}\화면 OCR"; Filename: "{app}\화면OCR.exe"; Comment: "Ctrl+Shift+C로 화면 텍스트 인식"
Name: "{group}\화면 OCR 제거"; Filename: "{uninstallexe}"

; 바탕화면 아이콘
Name: "{autodesktop}\화면 OCR"; Filename: "{app}\화면OCR.exe"; Tasks: desktopicon

; 시작 프로그램
Name: "{userstartup}\화면 OCR"; Filename: "{app}\화면OCR.exe"; Tasks: startupicon

[Run]
; 설치 완료 후 실행 옵션
Filename: "{app}\화면OCR.exe"; Description: "화면 OCR 바로 실행"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
; 제거 시 삭제할 파일
Type: filesandordirs; Name: "{app}\tesseract"

[Code]
// 설치 시작 전 메시지
function InitializeSetup(): Boolean;
begin
  Result := True;
  if MsgBox('화면 OCR 프로그램을 설치합니다.' + #13#10 + #13#10 + 
            '이 프로그램은 화면의 텍스트를 인식하여 클립보드에 복사합니다.' + #13#10 + 
            '설치 후 Ctrl+Shift+C 단축키로 사용할 수 있습니다.' + #13#10 + #13#10 +
            '계속하시겠습니까?', 
            mbConfirmation, MB_YESNO) = IDNO then
  begin
    Result := False;
  end;
end;

// 설치 완료 후 메시지
procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    MsgBox('설치가 완료되었습니다!' + #13#10 + #13#10 + 
           '사용 방법:' + #13#10 + 
           '1. 프로그램을 실행하세요' + #13#10 + 
           '2. Ctrl+Shift+C를 눌러 영역을 선택하세요' + #13#10 + 
           '3. 인식된 텍스트가 자동으로 클립보드에 복사됩니다' + #13#10 + 
           '4. Ctrl+V로 붙여넣기 하세요', 
           mbInformation, MB_OK);
  end;
end;
