# 화면 OCR 프로그램

화면의 특정 영역을 선택하여 텍스트를 인식하고 클립보드에 자동으로 복사하는 프로그램입니다.

## 주요 기능

- 🔍 화면 영역 선택 OCR
- 🇰🇷 한글 + 영어 동시 인식
- 📋 자동 클립보드 복사
- ⌨️ 전역 단축키 지원 (Ctrl+Shift+C)

## 사용 방법

### 1. 설치

GitHub Releases에서 `화면OCR_설치프로그램_v1.0.0.exe`를 다운로드하여 실행하세요.

### 2. 프로그램 실행

설치가 완료되면 바탕화면 또는 시작 메뉴에서 "화면 OCR"을 실행합니다.

### 3. OCR 사용

1. 프로그램이 실행 중일 때 `Ctrl + Shift + C` 누르기
2. 마우스로 텍스트 영역 드래그
3. 자동으로 텍스트 인식 및 클립보드 복사
4. `Ctrl + V`로 원하는 곳에 붙여넣기

### 4. 프로그램 종료

`Ctrl + Shift + Q` 누르기

## 단축키

| 단축키 | 기능 |
|--------|------|
| `Ctrl + Shift + C` | OCR 영역 선택 시작 |
| `Ctrl + Shift + Q` | 프로그램 종료 |
| `ESC` | 영역 선택 취소 |

## 개발자를 위한 정보

### 로컬에서 실행하기

#### 1. 필수 프로그램 설치

**Tesseract OCR 설치:**
1. https://github.com/UB-Mannheim/tesseract/wiki 에서 다운로드
2. 설치 시 "Additional language data"에서 **Korean** 체크
3. 설치 경로 기억하기 (기본: `C:\Program Files\Tesseract-OCR`)

**Python 라이브러리 설치:**
```bash
pip install -r requirements.txt
```

#### 2. 실행

```bash
python screen_ocr.py
```

### EXE 파일 만들기

```bash
# PyInstaller로 단일 실행 파일 생성
pyinstaller screen_ocr.spec

# 결과물: dist/화면OCR.exe
```

### 설치 프로그램 만들기

1. Inno Setup 설치 (https://jrsoftware.org/isdl.php)
2. Tesseract를 `tesseract/` 폴더에 복사
3. Inno Setup으로 컴파일:
```bash
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
```

## GitHub Actions 자동 빌드

이 프로젝트는 GitHub Actions를 통해 자동으로 빌드됩니다.

### 릴리즈 만들기

```bash
# 태그 생성
git tag v1.0.0

# 태그 푸시
git push origin v1.0.0
```

GitHub Actions가 자동으로:
1. Python 환경 설정
2. Tesseract 다운로드 및 설치
3. PyInstaller로 EXE 생성
4. Inno Setup으로 설치 프로그램 생성
5. GitHub Release에 업로드

## 프로젝트 구조

```
screen-ocr-python/
├── screen_ocr.py           # 메인 프로그램
├── screen_ocr.spec         # PyInstaller 설정
├── installer.iss           # Inno Setup 설정
├── requirements.txt        # Python 의존성
├── README.md              # 이 파일
├── .github/
│   └── workflows/
│       └── build-python.yml # GitHub Actions 워크플로우
└── tesseract/             # Tesseract OCR (로컬 빌드용)
```

## 문제 해결

### "Tesseract를 찾을 수 없습니다" 오류

Tesseract OCR이 설치되지 않았거나 경로를 찾을 수 없습니다.
1. Tesseract 설치 확인
2. 설치 경로가 다음 중 하나인지 확인:
   - `C:\Program Files\Tesseract-OCR\tesseract.exe`
   - `C:\Program Files (x86)\Tesseract-OCR\tesseract.exe`

### 한글 인식이 안 됨

1. Tesseract 설치 시 Korean 언어 데이터 선택 확인
2. `C:\Program Files\Tesseract-OCR\tessdata\kor.traineddata` 파일 존재 확인
3. 없다면 수동 다운로드:
   ```bash
   curl -L https://github.com/tesseract-ocr/tessdata/raw/main/kor.traineddata -o "C:\Program Files\Tesseract-OCR\tessdata\kor.traineddata"
   ```

### 단축키가 작동하지 않음

1. 프로그램이 관리자 권한으로 실행 중인지 확인
2. 다른 프로그램과 단축키 충돌 확인
3. 프로그램 재시작

## 라이선스

MIT License

## 제작

한국애니메이션고등학교

## 버전 히스토리

### v1.0.0 (2024-01-XX)
- 초기 릴리즈
- 기본 OCR 기능
- 한글/영어 인식
- 전역 단축키 지원
