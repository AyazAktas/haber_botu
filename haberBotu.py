import feedparser
from tkinter import *
import tkinter as tk
import webview
from datetime import datetime

root = tk.Tk()

def update_datetime():
    now = datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    btn_Saat.config(text=formatted_time)
    formatted_date = now.strftime("%d %B %Y")
    btn_tarih.config(text=formatted_date)
    root.after(1000, update_datetime)  # 1000ms (1 saniye) sonra tekrar güncelle


son_dk_url=[
    "https://www.milliyet.com.tr/rss/rssnew/sondakikarss.xml",
    "https://www.cnnturk.com/feed/rss/all/news",
    "https://www.ahaber.com.tr/rss/son24saat.xml"
]

bilim_url=[
    "https://www.milliyet.com.tr/rss/rssnew/teknolojirss.xml",
    "https://www.trthaber.com/bilim_teknoloji_articles.rss",
    "https://www.ahaber.com.tr/rss/teknoloji.xml"
]

dunya_url=[
    "https://www.milliyet.com.tr/rss/rssnew/dunyarss.xml",
    "https://www.cnnturk.com/feed/rss/dunya/news",
    "https://www.ahaber.com.tr/rss/dunya.xml"
]

saglik_url=[
    "https://www.ahaber.com.tr/rss/saglik.xml",
    "https://www.cnnturk.com/feed/rss/saglik/news",
    "https://www.sozcu.com.tr/rss/saglik.xml"
]

ekonomi_url=[
    "https://www.milliyet.com.tr/rss/rssnew/ekonomirss.xml",
    "https://www.cnnturk.com/feed/rss/ekonomi/news",
    "https://www.ahaber.com.tr/rss/ekonomi.xml"
]



def default_color_button():
    btn_bilim.configure(bg="lightblue")
    btn_ekonomi.configure(bg="lightblue")
    btn_saglik.configure(bg="lightblue")
    btn_dunya.configure(bg="lightblue")
    btn_sonDk.configure(bg="lightblue")




def clear():
    for widget in fr_haberler.winfo_children():
        widget.destroy()


def open_url(event):
    webview.create_window(event.widget.cget("text"),event.widget.cget("text"))
    webview.start()

def addHaberler(haberler):
    haber_sayisi=0
    for haber in haberler.entries:
        haber_sayisi=haber_sayisi+1
        if haber_sayisi>3:
            break

        lbl_title = tk.Label(fr_haberler, text=haber.title, anchor="w", font=('Helvetica Bold', 14))
        lbl_title.pack(side="top", fill="x")

        lbl_link = tk.Label(fr_haberler, text=haber.link, anchor="w", font=('Helvetica Bold', 14), fg="blue",
                            cursor="hand2")
        lbl_link.pack(side="top", fill="x")
        lbl_link.bind("<Button-1>", open_url)

        lbl_separator = tk.Label(fr_haberler, text="-", anchor="c", bg="pink")
        lbl_separator.pack(side="top", fill="x")


def son_dk_command():
    clear()
    default_color_button()
    btn_sonDk.configure(bg="teal")
    for url in son_dk_url:
        print(url,datetime.now().time())
        haberler=feedparser.parse(url)
        print(url,datetime.now().time())
        addHaberler(haberler)

def dunya_command():
    clear()
    default_color_button()
    btn_dunya.configure(bg="teal")
    for url in dunya_url:
        print(url,datetime.now().time())
        haberler=feedparser.parse(url)
        print(url,datetime.now().time())
        addHaberler(haberler)
def ekonomi_command():
    clear()
    default_color_button()
    btn_ekonomi.configure(bg="teal")
    for url in ekonomi_url:
        print(url,datetime.now().time())
        haberler=feedparser.parse(url)
        print(url,datetime.now().time())
        addHaberler(haberler)
def saglik_command():
    clear()
    default_color_button()
    btn_saglik.configure(bg="teal")
    for url in saglik_url:
        print(url,datetime.now().time())
        haberler=feedparser.parse(url)
        print(url,datetime.now().time())
        addHaberler(haberler)

def bilim_command():
    clear()
    default_color_button()
    btn_bilim.configure(bg="teal")
    for url in bilim_url:
        print(url,datetime.now().time())
        haberler=feedparser.parse(url)
        print(url,datetime.now().time())
        addHaberler(haberler)





root.title("Haber Botu-2023")
root.geometry("1000x690")

fr_haberler=Frame(root,height=690)
fr_buttons=Frame(root,relief=RAISED,bg="pink",bd=2)
fr_tarih=Frame(root,relief=RAISED,bg="pink",bd=2)





btn_sonDk=Button(fr_buttons,text="Son Dakika",font=('Helveticabold',14),bg="lightblue",command=son_dk_command)
btn_dunya=Button(fr_buttons,text="Dünya Haberleri",font=('Helveticabold',14),bg="lightblue",command=dunya_command)
btn_ekonomi=Button(fr_buttons,text="Ekonomi",font=('Helveticabold',14),bg="lightblue",command=ekonomi_command)
btn_saglik=Button(fr_buttons,text="Sağlık Haberleri",font=('Helveticabold',14),bg="lightblue",command=saglik_command)
btn_bilim=Button(fr_buttons,text="Bilim-Teknoloji Haberleri",font=('Helveticabold',14),bg="lightblue",command=bilim_command)
btn_Saat=Button(fr_tarih,text="Saat:",font=('Helveticabold',14),bg="lightblue")
btn_tarih=Button(fr_tarih,text="Tarih:",font=('Helveticabold',14),bg="lightblue")

btn_sonDk.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_dunya.grid(row=1,column=0,sticky="ew",padx=5,pady=5)
btn_ekonomi.grid(row=2,column=0,sticky="ew",padx=5,pady=5)
btn_saglik.grid(row=3,column=0,sticky="ew",padx=5,pady=5)
btn_bilim.grid(row=4,column=0,sticky="ew",padx=5,pady=5)

btn_Saat.grid(row=6,column=0,sticky="ew",padx=20,pady=5)
btn_tarih.grid(row=5,column=0,sticky="ew",padx=20,pady=5)

fr_tarih.grid(row=0,column=0,sticky="ews")
fr_buttons.grid(row=0,column=0,sticky="ns")
fr_haberler.grid(row=0,column=1,sticky="nsew")


update_datetime()
root.mainloop()