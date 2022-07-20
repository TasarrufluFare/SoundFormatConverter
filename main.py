import tkinter as tk
from tkinter import filedialog as fd
from tkinter import font
from pydub import AudioSegment


form = tk.Tk(screenName="Ses Format Dönüştürücü")
form.title("Ses Format Dönüştürücü")
form.geometry("500x250")
form.minsize(500,250)
form.maxsize(850,425)
form.configure(background="navy blue")
myFont1 = font.Font(family='Courier', size=14, weight='bold')
myFont2 = font.Font(family='Courier', size=10, weight='bold')

label = tk.Label(form, text="Yapacağınız Dönüşüm İşlemini Seçin", font=myFont1)
label.pack()
secilen = tk.StringVar()
dosya_yolu_global = ""
def donustur():
    mod = secilen.get()
    global dosya_yolu_global
    if mod == "Value 2":
        dosya_adi = dosya_yolu_global.split("/")[-1]
        yeni_dosya_adi = dosya_adi.split(".")[0]

        sound = AudioSegment.from_file(dosya_yolu_global, format="wav")
        file_handle = sound.export("C:/Users/Nezih/Music/Looper/" + yeni_dosya_adi + ".mp3", format="mp3")
        label['text'] = yeni_dosya_adi+".mp3 oluşturuldu."
        b2.config(state="disabled")
        dosya_yolu_global = ""

    elif mod == "Value 1":
        dosya_adi =dosya_yolu_global.split("/")[-1]
        yeni_dosya_adi = dosya_adi.split(".")[0]

        sound = AudioSegment.from_file(dosya_yolu_global, format="mp3")
        file_handle = sound.export("C:/Users/Nezih/Music/Looper/"+yeni_dosya_adi+".wav", format="wav")
        label['text'] = yeni_dosya_adi + ".mp3 oluşturuldu."
        b2.config(state="disabled")
        dosya_yolu_global = ""


def secimyap():
    mod = secilen.get()
    global dosya_yolu_global
    if mod == "Value 2":
        dosya_yolu = fd.askopenfilename(filetypes=[("Wav files", "*.Wav")])
        dosya_yolu_global = dosya_yolu
        if dosya_yolu != "":
            b2.config(state="normal")
            r1.config(state="disabled")
            r2.config(state="disabled")


    elif mod == "Value 1":
        dosya_yolu = fd.askopenfilename(filetypes=[("Mp3 files", "*.mp3")])
        dosya_yolu_global = dosya_yolu
        if dosya_yolu != "":
            b2.config(state="normal")
            r1.config(state="disabled")
            r2.config(state="disabled")


r1 = tk.Radiobutton(form, text='Wav to MP3', activebackground="green", value='Value 2', variable=secilen,font=myFont2)
r1.pack()
r2 = tk.Radiobutton(form, text='MP3 to Wav', activebackground="red", value='Value 1', variable=secilen,font=myFont2)
r2.pack()


b1 = tk.Button(form, text="Dosya Seç", command=secimyap,padx=24,pady=3)
b1.pack()
b2 = tk.Button(form, text="Dönüştür", command=donustur,padx=26,pady=3,state="disabled")
b2.pack()
form.mainloop()



