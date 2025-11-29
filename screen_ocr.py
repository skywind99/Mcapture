import pyautogui
import pytesseract
from PIL import Image, ImageGrab
import tkinter as tk
import pyperclip
from pynput import keyboard
import sys
import os

# Tesseract 경로 자동 설정
def get_tesseract_path():
    """Tesseract 경로 찾기"""
    possible_paths = [
        r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
        os.path.join(os.path.dirname(sys.executable), 'tesseract', 'tesseract.exe'),
        os.path.join(os.path.dirname(__file__), 'tesseract', 'tesseract.exe'),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None

tesseract_path = get_tesseract_path()
if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    print("❌ Tesseract를 찾을 수 없습니다!")
    sys.exit(1)

class ScreenOCR:
    def __init__(self):
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.rect = None
        
    def select_area(self):
        """영역 선택 UI"""
        root = tk.Tk()
        root.attributes('-alpha', 0.3)
        root.attributes('-fullscreen', True)
        root.attributes('-topmost', True)
        root.configure(background='black')
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        canvas = tk.Canvas(root, cursor="cross", bg='black', highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        info_text = canvas.create_text(
            screen_width // 2, 30,
            text="마우스로 드래그하여 영역을 선택하세요 (ESC: 취소)",
            fill='white', font=('맑은 고딕', 14, 'bold')
        )
        
        def on_press(event):
            self.start_x = event.x
            self.start_y = event.y
            if self.rect:
                canvas.delete(self.rect)
            self.rect = canvas.create_rectangle(
                self.start_x, self.start_y, 
                self.start_x, self.start_y, 
                outline='red', width=3
            )
        
        def on_drag(event):
            if self.rect:
                canvas.coords(
                    self.rect, 
                    self.start_x, self.start_y, 
                    event.x, event.y
                )
        
        def on_release(event):
            self.end_x = event.x
            self.end_y = event.y
            root.quit()
            root.destroy()
        
        def on_escape(event):
            self.start_x = None
            self.start_y = None
            self.end_x = None
            self.end_y = None
            root.quit()
            root.destroy()
        
        canvas.bind("<ButtonPress-1>", on_press)
        canvas.bind("<B1-Motion>", on_drag)
        canvas.bind("<ButtonRelease-1>", on_release)
        root.bind("<Escape>", on_escape)
        
        root.mainloop()
        
    def capture_and_ocr(self):
        """캡처 및 OCR 실행"""
        try:
            self.select_area()
            
            if self.start_x is None or self.end_x is None:
                return
            
            x1 = min(self.start_x, self.end_x)
            y1 = min(self.start_y, self.end_y)
            x2 = max(self.start_x, self.end_x)
            y2 = max(self.start_y, self.end_y)
            
            if abs(x2 - x1) < 10 or abs(y2 - y1) < 10:
                return
            
            screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            
            text = pytesseract.image_to_string(
                screenshot, 
                lang='kor+eng',
                config='--psm 6'
            )
            
            text = text.strip()
            
            if text:
                pyperclip.copy(text)
                print("=" * 50)
                print("✅ 텍스트 인식 완료! 클립보드에 복사되었습니다.")
                print("=" * 50)
                print(text)
                print("=" * 50)
            else:
                print("⚠️ 텍스트를 인식하지 못했습니다.")
                
        except Exception as e:
            print(f"❌ 오류 발생: {e}")

def on_activate():
    """단축키 눌렀을 때 실행"""
    print("\n🔍 OCR 영역 선택 모드 시작...")
    ocr = ScreenOCR()
    ocr.capture_and_ocr()

def on_exit():
    """프로그램 종료"""
    print("\n👋 프로그램을 종료합니다.")
    sys.exit(0)

def main():
    print("=" * 60)
    print("🚀 화면 OCR 프로그램 시작!")
    print("=" * 60)
    print("📌 단축키: Ctrl + Shift + C  →  영역 선택 후 텍스트 인식")
    print("📌 종료: Ctrl + Shift + Q")
    print("=" * 60)
    print("\n대기 중...")
    
    with keyboard.GlobalHotKeys({
            '<ctrl>+<shift>+c': on_activate,
            '<ctrl>+<shift>+q': on_exit
        }) as h:
        h.join()

if __name__ == "__main__":
    main()
