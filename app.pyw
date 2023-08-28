import tkinter as tk
from tkinter import filedialog
import os
import sys

class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget
        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.insert('1.0', text) # write text to textbox
            # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass
def do_something():
        root.after(1000, do_something)

def readChap():
    global chap
    f = open("./chapSave.txt", "r")
    line = f.readline()
    if line:
        chap = int(line)
    f.close()
def saveChap():
    global chap
    f = open("./chapSave.txt", "w")
    f.write(str(chap))
    f.close()
def open_file():
    global chap
    if len(chapList) == chap:
        return
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r",encoding='utf-8') as file:
            chap = chapList.index(int(file.name.split("/")[-1].replace(".txt", "")))
            content = file.read()
            title = str(content.split('\n')[0])
            var.set(title)
            content = content.split('\n', 1)[-1].replace("— QUẢNG CÁO —", "\n")
            text_widget.delete("1.0", tk.END)  # Clear previous content
            text_widget.insert("1.0", content)
            print(title)  
            saveChap()

def clickNext(event):
    next()
def clickPre(event):
    pre()
def next():
    global chap
    chap = chap + 1
    if len(chapList) == chap:
        chap = chap - 1
        return
    file_path = path + str(chapList[chap]) + ".txt"
    try:
        if file_path:
            with open(file_path, "r",encoding='utf-8') as file:
                content = file.read()
                title = str(content.split('\n')[0])
                var.set(title)
                content = content.split('\n', 1)[-1].replace("— QUẢNG CÁO —", "\n\n")
                text_widget.delete("1.0", tk.END)  # Clear previous content
                text_widget.insert("1.0", content)
                print(title)  
    except:
        chap = chap - 1
    saveChap()

def pre():
    global chap
    chap = chap - 1
    if chap <= 0: 
        chap = 0
    file_path = path + str(chapList[chap]) + ".txt"
    if len(chapList) == chap:
        return
    if file_path:
        with open(file_path, "r",encoding='utf-8') as file:
            content = file.read()
            title = str(content.split('\n')[0])
            var.set(title)
            content = content.split('\n', 1)[-1].replace("— QUẢNG CÁO —", "\n\n")
            text_widget.delete("1.0", tk.END)  # Clear previous content
            text_widget.insert("1.0", content)
            print(title)  
            saveChap()
def load():
    readChap()
    global chap
    if len(chapList) == chap:
        return
    file_path = path + str(chapList[chap]) + ".txt"
    if file_path:
        with open(file_path, "r",encoding='utf-8') as file:
            content = file.read()
            title = str(content.split('\n')[0])
            var.set(title)
            content = content.split('\n', 1)[-1].replace("— QUẢNG CÁO —", "\n\n")
            text_widget.delete("1.0", tk.END)  # Clear previous content
            text_widget.insert("1.0", content)
            print(title)  
            saveChap()
def touchpad_events(event):
    if event.num==5:
        next()
    elif event.num==4:
        pre()
    return "break"
def up_events(event):
    print("up")
def down_events(event):
    print("down")
def on_mouse_wheel(event):
    print(str(event))
    print(str(event))
    # text_widget.yview_scroll(-1 * (event.delta // 120), "units")
def scroll_down(event):
    text_widget.yview_scroll(1, "units")
def scroll_up(event):
    text_widget.yview_scroll(-1, "units")













chapList = []
path = "./dttt/"

for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path, filename)):
        chapList.append(int(filename.split('.txt')[0]))
chapList.sort()
chap = chapList[0]

# Create the main application window
root = tk.Tk()
root.title("App Đọc truyện của Tính:>")
photo = tk.PhotoImage(file = 'icon.png')
root.wm_iconphoto(False, photo)
root.configure(background='white', )
root.geometry("800x800")
root.minsize(800, 800)
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(side=tk.BOTTOM, fill = tk.BOTH)

load_button = tk.Button(root, text="Load", command=load)
load_button.pack(side=tk.BOTTOM, fill = tk.BOTH)


# Create a text widget to display file content
# root.bind('<Button>', touchpad_events)
text_widget = tk.Text(root, wrap=tk.WORD, font=("Times New Roman", 18), border=0, highlightcolor='white', padx=20, takefocus=0)
scrollbar = tk.Scrollbar(root, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)
# Bind key 'a' to scroll down
root.bind("w", scroll_up)
root.bind("<Up>", scroll_up)
root.bind("W", scroll_up)
root.bind("s", scroll_down)
root.bind("<Down>", scroll_down)
root.bind("S", scroll_down)
root.bind("d", clickNext)  # Bind Right arrow key to next_page function
root.bind("<Right>", clickNext)  # Bind Right arrow key to next_page function
root.bind("D", clickNext)  # Bind Right arrow key to next_page function
root.bind("a", clickPre) 
root.bind("<Left>", clickPre) 
root.bind("A", clickPre) 
text_widget.bind("<Key>", lambda e: root.focus_set())
text_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx = 20, pady = 10)

# Create an "Open File" button

next_button = tk.Button(root, text="Next", command=next)
next_button.pack(side=tk.RIGHT)
pre_button = tk.Button(root, text="Pre", command=pre)
pre_button.pack(side=tk.LEFT)
var = tk.StringVar()
chapNumberLabel = tk.Label(root, textvariable=var, font=("Times New Roman", 24), fg='red', bg='white')
chapNumberLabel.pack()
root.focus_set()
root.unbind_all('<<NextWindow>>') 
load()
root.attributes('-topmost', 'true')
# t = tk.Text()
# t.pack()
# pl = PrintLogger(t)
# sys.stdout = pl
# root.after(1000, do_something)
# x = threading.Thread(target=thread_function, args=())
# x.start()
# Start the tkinter main loop
root.mainloop()
