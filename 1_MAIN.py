from asyncio.windows_events import NULL
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog

window = Tk()

window.title("Image Sum Program")
window.geometry("640x640")
window.resizable(False, False)

# 파일 프레임 메소드
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일 선택", \
            filetypes=(("JPG 파일", "*.jpg"), ("모든파일", "*.*")), \
            initialdir="C:/Users/AwesomeTechnic/Documents/IMAGE")
    
    for file in files:
        list_box.insert(END, file)


def delete_file():
    for idx in reversed(list_box.curselection()):
        list_box.delete(idx)

# 파일 프레임

file_frame = Frame(window)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, text="파일추가", padx=10, pady=10, width=15, command=add_file)
btn_add_file.pack(side="left")
btn_delete_file = Button(file_frame, text="파일삭제", padx=10, pady=10, width=15, command=delete_file)
btn_delete_file.pack(side="right")



# 리스트 프레임
list_frame = Frame(window)
list_frame.pack(fill="both", expand=True)

scroll_bar = Scrollbar(list_frame)
scroll_bar.pack(side="right", fill="y")

list_box = Listbox(list_frame, selectmode="extended", height=20, yscrollcommand=scroll_bar.set)
list_box.pack(side="left", fill="both", expand=True)

scroll_bar.config(command=list_box.yview)


# 저장경로 메소드
def browse_desktop_folder():
    folder_seleted = filedialog.askdirectory(title="저장할 폴더를 선택하세요")
    if (folder_seleted == ""):
        return
    
    entry_desktop_path.delete(0, END)
    entry_desktop_path.insert(0, folder_seleted)
         
# 저장경로 프레임
path_frame = LabelFrame(window, text="저장경로")
path_frame.pack(fill="x", expand=True)

entry_desktop_path = Entry(path_frame)
entry_desktop_path.pack(side="left", fill="x", expand=True, ipady=5)

btn_desktop_path = Button(path_frame, text="찾아보기", width=10, command=browse_desktop_folder)
btn_desktop_path.pack(side="right")



# 옵션 프레임
opt_frame = LabelFrame(window, text="옵션")
opt_frame.pack(fill="x", expand=True, ipady=5)

# 가로넓이 옵션
lable_width = Label(opt_frame, text="가로넓이")
lable_width.pack(side="left")

opt_width = ["원본유지","1024", "800", "640"]
combobox_width = ttk.Combobox(opt_frame, state="readonly", values=opt_width, width=10)
combobox_width.current(0)
combobox_width.pack(side="left")

# 세로간격 옵션
lable_span = Label(opt_frame, text="세로간격")
lable_span.pack(side="left")

opt_span = ["없음","좁게", "보통", "넓게"]
combobox_span = ttk.Combobox(opt_frame, state="readonly", values=opt_span, width=10)
combobox_span.current(0)
combobox_span.pack(side="left")

# 파일포맷 옵션
lable_format = Label(opt_frame, text="파일포맷")
lable_format.pack(side="left")

opt_format = ["PNG","JPG", "BMP"]
combobox_format = ttk.Combobox(opt_frame, state="readonly", values=opt_format, width=10)
combobox_format.current(0)  
combobox_format.pack(side="left")

# 진행상황 프레임
progress_frame = ttk.Labelframe(window, text="진행상황")
progress_frame.pack(fill="x")

variable_progress = DoubleVar()
progressbar_progress = ttk.Progressbar(progress_frame, maximum=100, variable=variable_progress)
progressbar_progress.pack(fill="x")

# 실행 프레임
run_frame = LabelFrame(window, text="실행")
run_frame.pack(fill="x")

btn_stop = Button(run_frame, text="닫기", width=10, command=window.quit)
btn_stop.pack(side="right")

btn_start = Button(run_frame, text="시작", width=10)
btn_start.pack(side="right")


window.mainloop()