import sys
import os
import base64
import tkinter as tk
from tkinter import Toplevel
from tkinter import filedialog
from tkinter import messagebox
from tkinter import PhotoImage, Label
from PIL import Image, ImageTk

def encode_decode(action):
    messagebox.showwarning("Warning", "DRM 보안해제를 잊지마세요.")

    input_path = filedialog.askopenfilename()
    if not input_path:  # Check if a file is selected
        messagebox.showwarning("Warning", "파일 선택을 취소합니다.")
        return

    output_path = filedialog.asksaveasfilename()
    if not output_path:  # Check if a save location is selected
        messagebox.showwarning("Warning", "파일 저장을 취소합니다.")
        return

    with open(input_path, 'rb') as file:
        data = file.read()
        if action == '인코드(Encode)':
            converted_data = base64.b64encode(data)
        elif action == '디코드(Decode)':
            converted_data = base64.b64decode(data)

    with open(output_path, 'wb') as file:
        file.write(converted_data)

    messagebox.showinfo("안내", f"파일을 성공적으로 [{action}]해서 저장했습니다.")

def create_tooltip(widget, text):
    tip_window = None

    def show_tip():
        nonlocal tip_window
        x, y, _, _ = widget.bbox("insert")
        x += widget.winfo_rootx() + 5
        y += widget.winfo_rooty() - 30
        tip_window = Toplevel(widget)
        tip_window.wm_overrideredirect(True)
        tip_window.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tip_window, text=text, background="#000000", relief='solid', borderwidth=1, font=("Malgul Gothic", "13", "normal"), padx=5, pady=5)
        label.pack()

    def hide_tip():
        nonlocal tip_window
        if tip_window:
            tip_window.destroy()
            tip_window = None

    widget.bind("<Enter>", lambda e: show_tip())
    widget.bind("<Leave>", lambda e: hide_tip())

root = tk.Tk()
root.title("라이언의 인(디)코딩 앱 (2023)")

# Open the image file
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_path, 'ryanyang_profile.png')
img = Image.open(image_path)

# Resize the image
img = img.resize((320, 320))

# Convert to PhotoImage
photo = ImageTk.PhotoImage(img)

# Create and pack the label with the image
image_label = Label(root, image=photo)
image_label.image = photo  # Keep a reference to avoid garbage collection
image_label.pack()

# Now pack your buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encode_button = tk.Button(root, text="내보내기(Encode)", command=lambda: encode_decode('인코드(Encode)'))
decode_button = tk.Button(root, text="가져오기(Decode)", command=lambda: encode_decode('디코드(Decode)'))

encode_button.pack(side=tk.LEFT, padx=10, in_=button_frame)
decode_button.pack(side=tk.LEFT, padx=10, in_=button_frame)

create_tooltip(encode_button, "[인코딩] = 파일을 내부(외부)로 내보낼 때 사용합니다.")
create_tooltip(decode_button, "[디코딩] = 파일을 내부(외부)로 가져올 때 사용합니다.")

root.mainloop()