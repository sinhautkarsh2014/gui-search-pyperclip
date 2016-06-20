import sys
from Tkinter import *
import webbrowser
import pyperclip
 
App=Tk()
App.geometry("400x200")
l1=Label(App,text='Your search query(type cpaste if you want to paste from clipboard):').pack()
e = Entry(App)
e.pack()

e.delete(0, END)
e.insert(0, "Life")

l2=Label(App,text='Your browser:').pack()

f = Entry(App)
f.pack()

f.delete(0, END)
f.insert(0, "bing")

def callback():
    search_string=e.get()
    print search_string
    engine = f.get()
    print engine
    if search_string.lower() == "cpaste":
        search_string = pyperclip.paste()
        search_string = search_string.replace(' ', '+')
        
    if engine.lower() == "google":
        url = 'https://www.google.com/search?q=' + search_string
    if engine.lower() == "bing":
        url = 'http://www.bing.com/search?q=' + search_string
    if engine.lower() == "hotbot":
        url = 'http://www.hotbot.com/search/web?q=' + search_string
    if engine.lower() == "lycos":
        url = 'http://search.lycos.com/web/?q=' + search_string
    webbrowser.open_new_tab(url)

b = Button(App, text="Search", width=10, command=callback)
b.pack()


l3=Label(App,text='Copy to clipboard:').pack()
g = Entry(App)
g.pack()

g.delete(0, END)
g.insert(0, "copied text")
def callback1():
    s=g.get()
    App.clipboard_clear()
    App.clipboard_append(s)
    
c = Button(App, text="Copy", width=10, command=callback1)
c.pack()



App.mainloop()
