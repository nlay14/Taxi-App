import tkinter as tk
from tkinter import ttk, Frame
from PIL import Image,ImageTk
import sqlite3
from numpy import random
import re
from pygame import mixer
from tkinter import messagebox
import random



bgColour = "#404040"
def clear_widgets(frame):
	for widget in frame.winfo_children():
		widget.destroy()
def TaksiDataBase(): #ÜRÜNLERİ RASTGELE DEĞİŞTİRME
    connection = sqlite3.connect("data/your_database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT Taksileri.Plaka, Taksileri.Durak,Taksileri.AdSoyad, Taksileri.BakimDurumu, Taksileri.BosMu, Taksileri.DilSeviyesi, Taksileri.EngelliDestegi, Taksileri.Kapasite, Taksileri.KartOdeme, Taksileri.MesafeTipi FROM Taksileri")
    data = cursor.fetchall()
    idx = random.randint(0, len(data) - 1)
    data = data[idx]
    print(data)
    return data


    connection.commit()
    connection.close()

def Insert(entry_Plaka,entry_Durak,entry_AdSoyad,entry_BakimDurumu,entry_BosMu,entry_DilSeviyesi,entry_EngelliDestegi,entry_Kapasite,entry_KartOdeme,entry_MesafeTipi):
    connection = sqlite3.connect("data/your_database.db")
    cursor = connection.cursor()

    Plaka=entry_Plaka.get()
    Durak=entry_Durak.get()
    AdSoyad=entry_AdSoyad.get()
    BakımDurumu=entry_BakimDurumu.get()
    BosMu=entry_BosMu.get()
    DilSeviyesi=entry_DilSeviyesi.get()
    EngelliDestegi=entry_EngelliDestegi.get()
    Kapasite=entry_Kapasite.get()
    KartOdeme=entry_KartOdeme.get()
    MesafeTipi=entry_MesafeTipi.get()

    sql= 'Insert Into Taksileri (Plaka, Durak, AdSoyad, BakimDurumu,BosMu,DilSeviyesi,EngelliDestegi,Kapasite, KartOdeme, MesafeTipi) values (?,?,?,?,?,?,?,?,?,?);'
    values = (Plaka,Durak,AdSoyad,BakımDurumu,BosMu,DilSeviyesi,EngelliDestegi,Kapasite, KartOdeme, MesafeTipi)
    cursor.execute(sql,values)

    connection.commit()
    connection.close()
    print("EKLEME İŞLEMİ BAŞARILI!")

def Update( entry_Durak, entry_AdSoyad, entry_BakimDurumu, entry_BosMu,entry_DilSeviyesi, entry_EngelliDestegi, entry_Kapasite, entry_KartOdeme,entry_MesafeTipi):
    connection = sqlite3.connect("data/your_database.db")
    cursor = connection.cursor()
    """Plaka = entry_Plaka.get()"""
    Durak=entry_Durak.get()
    AdSoyad=entry_AdSoyad.get()
    BakimDurumu=entry_BakimDurumu.get()
    BosMu=entry_BosMu.get()
    DilSeviyesi=entry_DilSeviyesi.get()
    EngelliDestegi=entry_EngelliDestegi.get()
    Kapasite=entry_Kapasite.get()
    KartOdeme=entry_KartOdeme.get()
    MesafeTipi=entry_MesafeTipi.get()


    sql = 'Update Taksileri Set Durak=?,AdSoyad=?,BakimDurumu= ?, BosMu= ?, DilSeviyesi=?, EngelliDestegi=?, Kapasite=?, KartOdeme=? where MesafeTipi=? '
    values=(Durak,AdSoyad,BakimDurumu,BosMu, DilSeviyesi,EngelliDestegi,Kapasite, KartOdeme, MesafeTipi)
    cursor.execute(sql,values)


    connection.commit()
    connection.close()
    LoadFrame4()


    print("DEĞİŞTİRME İŞLEMİ BAŞARILI!")


def Select():
    connection = sqlite3.connect("data/your_database.db")
    cursor = connection.cursor()

    cursor.execute('select Taksileri.Plaka, Taksileri.Durak, Taksileri.AdSoyad, Taksileri.BakimDurumu, Taksileri.BosMu, Taksileri.DilSeviyesi, Taksileri.EngelliDestegi, Taksileri.Kapasite, Taksileri.KartOdeme, Taksileri.MesafeTipi FROM Taksileri')
    data= cursor.fetchall()

    connection.commit()
    connection.close()
    return data
    print("EKLEME İŞLEMİ BAŞARILI!")




def save_feedback(feedback_text, selected_taxi):
    try:
        with open("data/dilek_sikayet.txt", "a", encoding="utf-8") as file:
            file.write(f"TAKSİ: {selected_taxi}\n")
            file.write(f"GERİ BİLDİRİM: {feedback_text}\n")
            file.write("-" * 30 + "\n")
        messagebox.showinfo("Bilgi", "Dilek ve şikayetleriniz kaydedildi!")
    except Exception as e:
        messagebox.showerror("Hata", f"Kaydetme sırasında bir hata oluştu: {str(e)}")



def view_feedbacks():
    try:
        with open("data/dilek_sikayet.txt", "r", encoding="utf-8") as file:
            feedbacks = file.read()
        messagebox.showinfo("Dilek ve Şikayetler", feedbacks)
    except FileNotFoundError:
        messagebox.showinfo("Bilgi", "Dilek ve şikayet kaydı bulunamadı.")
    except Exception as e:
        messagebox.showerror("Hata", f"Görüntüleme sırasında bir hata oluştu: {str(e)}")


def IndexChangedUpdate(event):
    selected_item = event.widget.get()
    print("Düzensiz Değerler:", selected_item)
    pattern = re.compile(r'\{([^}]*)\}|([^{}]*)')
    matches = pattern.findall(selected_item)
    selected_item = [match[0] if match[0] else match[1] for match in matches]
    selected_item = [item.strip() for item in selected_item if item.strip()]

    print("Dizi Olarak Değerler:", selected_item)

    #Durak
    label_Durak = tk.Label(frameMain7, text="Durak:")
    label_Durak.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    entry_Durak = tk.Entry(frameMain7, width=40)
    entry_Durak.insert(0, selected_item[1])
    entry_Durak.grid(row=2, column=1, padx=5, pady=5)

    #AdSoyad
    label_AdSoyad = tk.Label(frameMain7, text="Adı Soyadı:")
    label_AdSoyad.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    entry_AdSoyad =tk.Entry(frameMain7, width=40)
    entry_AdSoyad.insert(0, selected_item[2])
    entry_AdSoyad.grid(row=3, column=1, padx=5, pady=5)

    #BakimDurumu
    label_BakimDurumu = tk.Label(frameMain7, text="Taksi Bakım Durumu:")
    label_BakimDurumu.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    entry_BakimDurumu = tk.Entry(frameMain7, width=40)
    entry_BakimDurumu.insert(0, selected_item[3])
    entry_BakimDurumu.grid(row=4, column=1, padx=5, pady=5)

    #BosMu
    Label_BosMu = tk.Label(frameMain7, text="Taksi Doluluk Durumu:")
    Label_BosMu.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
    entry_BosMu = tk.Entry(frameMain7, width=40)
    entry_BosMu.insert(0, selected_item[4])
    entry_BosMu.grid(row=5, column=1, padx=5, pady=5)

    #DilSeviyesi
    label_DilSeviyesi = tk.Label(frameMain7, text="Yabancı Dil Durumu:")
    label_DilSeviyesi.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
    entry_DilSeviyesi = tk.Entry(frameMain7, width=40)
    entry_DilSeviyesi.insert(0, selected_item[5])
    entry_DilSeviyesi.grid(row=6, column=1, padx=5, pady=5)

    #EngelliDestegi
    label_EngelliDestegi = tk.Label(frameMain7, text="Engelli Desteği Durumu:")
    label_EngelliDestegi.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
    entry_EngelliDestegi = tk.Entry(frameMain7, width=40)
    entry_EngelliDestegi.insert(0, selected_item[6])
    entry_EngelliDestegi.grid(row=7, column=1, padx=5, pady=5)

    # Kapasite
    label_Kapasite = tk.Label(frameMain7, text="Kapasite:")
    label_Kapasite.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)
    entry_Kapasite = tk.Entry(frameMain7, width=40)
    entry_Kapasite.insert(0, selected_item[7])
    entry_Kapasite.grid(row=8, column=1, padx=5, pady=5)

    # KartOdeme
    label_KartOdeme = tk.Label(frameMain7, text="Ödeme Seçeneği:")
    label_KartOdeme.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)
    entry_KartOdeme = tk.Entry(frameMain7, width=40)
    entry_KartOdeme.insert(0, selected_item[8])
    entry_KartOdeme.grid(row=9, column=1, padx=5, pady=5)

    # MesafeTipi
    label_MesafeTipi = tk.Label(frameMain7, text="Mesafe Tipi:")
    label_MesafeTipi.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)
    entry_MesafeTipi = tk.Entry(frameMain7, width=40)
    entry_MesafeTipi.insert(0, selected_item[9])
    entry_MesafeTipi.grid(row=10, column=1, padx=5, pady=5)



    # değiştir düğmesi
    tk.Button(
        frameMain7,
        text="TAKSİYİ DEĞİŞTİR",
        font=("TkHeadingFont", 16),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: [Update(
            entry_Durak, entry_AdSoyad, entry_BakimDurumu, entry_BosMu, entry_DilSeviyesi, entry_EngelliDestegi,
            entry_Kapasite, entry_KartOdeme, entry_MesafeTipi
        ), messagebox.showinfo("Başarı", "Taksi başarıyla güncellendi!")]
        ).grid(row=15, column=1, columnspan=2, pady=10)


def dil_seviyesine_gore_ayir(di_DilSeviyesi):
    connection = sqlite3.connect("data/your_database.db")
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM DİL WHERE di_DilSeviyesi=?", (di_DilSeviyesi,))
    Taksici = cursor.fetchall()

    connection.close()

    return Taksici

def buton_callback(di_DilSeviyesi):

    for widget in veri_cerceve.winfo_children():
        widget.destroy()

    Taksicil = dil_seviyesine_gore_ayir(di_DilSeviyesi)


    if Taksicil:
        for DİL in Taksicil:
            # Verileri içeren etiketleri çerçeve içine ekle
            isim_plaka = f"Taksi İsmi: {DİL[1]}, Plaka: {DİL[0]}, Taksici Dil Seviyesi :{DİL[2]}"
            tk.Label(veri_cerceve, text=isim_plaka).pack()

    else:
        print("Belirtilen dil seviyesine uygun sürücü bulunamadı.")




def engelli_gore_ayir(en_EngelliDestegi):
    connection = sqlite3.connect("data/your_database.db")
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM Engelliii WHERE en_EngelliDestegi=?", (en_EngelliDestegi,))
    Taksici = cursor.fetchall()

    connection.close()

    return Taksici

def buton_call(en_EngelliDestegi):

    for widget in veri_cerceve.winfo_children():
        widget.destroy()

    Taksici = engelli_gore_ayir(en_EngelliDestegi)

    if Taksici:
        for Engelliii in Taksici:
            # Verileri içeren etiketleri çerçeve içine ekle
            isim_plaka = f"Taksici İsmi: {Engelliii[1]}, Plaka: {Engelliii[0]}, Engelli Desteği Durumu: {Engelliii[2]}"
            tk.Label(veri_cerceve, text=isim_plaka).pack()

    else:
        print("Belirtilene uygun sürücü bulunamadı.")


def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def dondur():
    indirimler = ["10 TL İNDİRİM", "20 TL İNDİRİM", "30 TL İNDİRİM", "50 TL İNDİRİM", "100 TL İNDİRİM"]
    secilen_indirim = random.choice(indirimler)

    # ekkkrana çıkan yazıyı bastır
    print(f"Çark döndü! Kazandığınız indirim: {secilen_indirim}")


    ekstra_kutucuk.config(text=f"KAZANDIĞINIZ İNDİRİM : {secilen_indirim}", fg="black",font=("TkItalicfont", 16, "bold"))


def boyuta_gore_ayir(ka_Kapasite):
    connection = sqlite3.connect("data/your_database.db")
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM kapasite WHERE ka_Kapasite=?", (ka_Kapasite,))
    Taks = cursor.fetchall()

    connection.close()

    return Taks

def buton_cal(ka_Kapasite):

    for widget in veri_cerceve.winfo_children():
        widget.destroy()

    Taks = boyuta_gore_ayir(ka_Kapasite)


    if Taks:
        for kapasite in Taks:
            # Verileri içeren etiketleri çerçeve içine ekle
            isim_plaka = f"Taksici İsmi: {kapasite[1]},  Plaka: {kapasite[0]},  Kapasite: {kapasite[2]}"
            tk.Label(veri_cerceve, text=isim_plaka).pack()

    else:
        print("Belirtilene uygun sürücü bulunamadı.")


def odeme_gore_ayir(od_KartOdeme):
    connection = sqlite3.connect("data/your_database.db")
    cursor = connection.cursor()


    cursor.execute("SELECT * FROM odeme WHERE od_KartOdeme=?", (od_KartOdeme,))
    Taks = cursor.fetchall()

    connection.close()

    return Taks

def buton_ca(od_KartOdeme):

    for widget in veri_cerceve.winfo_children():
        widget.destroy()

    Taks = odeme_gore_ayir(od_KartOdeme)


    if Taks:
        for odeme in Taks:
            # Verileri içeren etiketleri çerçeve içine ekle
            isim_plaka = f"Taksici İsmi: {odeme[1]},  Plaka: {odeme[0]}, Ödeme Seçeneği: {odeme[2]}"
            tk.Label(veri_cerceve, text=isim_plaka).pack()

    else:
        print("Belirtilene uygun sürücü bulunamadı.")


def MesafeTipi_gore_ayir(me_MesafeTipi):
    connection = sqlite3.connect("data/your_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mesafe WHERE me_MesafeTipi=?", (me_MesafeTipi,))
    Taks = cursor.fetchall()

    connection.close()

    return Taks


def buton_c(me_MesafeTipi):
    for widget in veri_cerceve.winfo_children():
        widget.destroy()

    Taks = MesafeTipi_gore_ayir(me_MesafeTipi)

    if Taks:
        for mesafe in Taks:
            # Verileri içeren etiketleri çerçeve içine ekle
            isim_plaka = f"Taksici İsmi: {mesafe[1]},  Plaka: {mesafe[0]}, Mesafe Tipi: {mesafe[2]}"
            tk.Label(veri_cerceve, text=isim_plaka).pack()

    else:
        print("Belirtilene uygun sürücü bulunamadı.")


def acil_durum_callback():
    yanip_son_effekti()

    messagebox.showinfo("Acil Durum", "POLİS EKİPLERİ BULUNDUĞUNUZ KONUMA YÖNLENDİRİLİYOR!")

def yanip_son_effekti():
    if frameMain13.cget("bg") == "red":
        frameMain13.configure(bg='black')
    else:
        frameMain13.configure(bg='red')

    frameMain13.after(500, yanip_son_effekti)


class YildizDegerlendirme(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Şoförü Değerlendir")
        self.geometry("300x200")

        self.puan = tk.IntVar()
        self.puan.set(0)

        self.yildizlar_frame = tk.Frame(self)
        self.yildizlar_frame.pack(pady=20)

        for i in range(5):
            yildiz = tk.Label(self.yildizlar_frame, text="⭐", font=("Arial", 20), cursor="hand2")
            yildiz.grid(row=0, column=i, padx=5)
            yildiz.bind("<Button-1>", lambda event, i=i+1: self.degerlendir(i))

        self.puan_label = tk.Label(self, text="Puanınız: 0", font=("Arial", 16))
        self.puan_label.pack()

        kapat_dugmesi = tk.Button(self, text="Kapat", command=self.kapat)
        kapat_dugmesi.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.kapat)

    def degerlendir(self, puan):
        self.puan.set(puan)
        self.puan_label.config(text=f"Puanınız: {puan}")
        messagebox.showinfo("Değerlendirme", f"Şoföre {puan} yıldız verdiniz!")
        self.kapat()

    def kapat(self):
        self.destroy()
        self.master.deiconify()

def LoadFrame1():
    clear_widgets(frameMain2)
    frameMain.tkraise()
    frameMain.pack_propagate(False)
    # logo widget
    imge = Image.open("assets/commerce.png").resize((300, 175))
    imgLogo = ImageTk.PhotoImage(imge)
    logoWidget = tk.Label(frameMain, image=imgLogo, bg=bgColour)
    logoWidget.image = imgLogo
    logoWidget.pack()
    tk.Label(
        frameMain,
        text="TAKSİM",
        bg=bgColour,
        fg="white",
        font=("TkItalicfont", 23, "bold")
    ).pack()

    button_width = 30,

    frame1 = tk.Frame(frameMain, bg=bgColour)
    frame1.pack(side="left", padx=10)

    frame2 = tk.Frame(frameMain, bg=bgColour)
    frame2.pack(side="right", padx=10)


    kesfet = tk.Button(
        frame1,
        text="TAKSİ İNCELE",
        font=("TkHeadingFont", 13, "bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        width=button_width,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame2()
    )
    kesfet.pack(side="top", pady=10)

    ekle = tk.Button(
        frame1,
        text="  TAKSİ EKLE   ",
        font=("TkCustomFont", 13, "bold"),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        width=button_width,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame3()
    )
    ekle.pack(side="top", pady=10)

    duzenle = tk.Button(
        frame1,
        text="BİLGİLERİ DÜZENLE",
        font=("TkHeadingFont", 13, "bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        width=button_width,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame4()
    )
    duzenle.pack(side="top", pady=10)

    dilekSikayet = tk.Button(
        frame1,
        text="   DİLEK VE ŞİKAYETLER   ",
        font=("TkHeadingFont", 13, "bold"),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        width=button_width,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame5()
    )
    dilekSikayet.pack(side="top", pady=10)

    bosluk0 = tk.Button(
        frame1,
        text="DİLEK VE ŞİKAYETLERİ İNCELE",
        font=("TkCustomFont", 13, "bold"),
        width=button_width,
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame6()
    )
    bosluk0.pack(side="top", pady=10)

    bosluk1 = tk.Button(
        frame1,
        text="ŞOFÖRÜN DİL SEVİYESİ",
        font=("TkCustomFont", 13, "bold"),
        width=button_width,
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame7()
    )
    bosluk1.pack(side="top", pady=10)

    bosluk2 = tk.Button(
        frame1,
        text="ENGELLİ DESTEĞİ",
        font=("TkHeadingFont", 13, "bold"),
        width=button_width,
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame8()
    )
    bosluk2.pack(side="top", pady=10)

    bosluk3 = tk.Button(
        frame2,
        text="PROMOSYON KODU",
        font=("TkCustomFont", 13, "bold"),
        width=button_width,
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame9()
    )
    bosluk3.pack(side="top", pady=10)

    bosluk4 = tk.Button(
        frame2,
        text="TAKSİ BOYUTU",
        font=("TkCustomFont", 13, "bold"),
        width=button_width,
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame10()
    )
    bosluk4.pack(side="top", pady=10)

    bosluk5 = tk.Button(
        frame2,
        text="ÖDEME SEÇENEKLERİ",
        font=("TkCustomFont", 13, "bold"),
        width=button_width,
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame11()
    )
    bosluk5.pack(side="top", pady=10)

    bosluk6 = tk.Button(
        frame2,
        text="YOLCULUK MESAFESİ",
        font=("TkCustomFont", 13, "bold"),
        width=button_width,
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame12()
    )
    bosluk6.pack(side="top", pady=10)

    bosluk7 = tk.Button(
        frame2,
        text="ACİL YARDIM BUTONU",
        font=("TkCustomFont", 13, "bold"),
        width=button_width,
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame13()
    )
    bosluk7.pack(side="top", pady=10)

    bosluk8 = tk.Button(
        frame2,
        text="ŞOFÖRÜ DEĞERLENDİR",
        font=("TkCustomFont", 13, "bold"),
        width=button_width,
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame14()
    )
    bosluk8.pack(side="top", pady=10)

    def play_sound():
        sound_file = r"C:\Users\Nilay\PycharmProjects\pythonProjectdeneme2\data\usman1.mp3"
        mixer.init()
        mixer.music.load(sound_file)
        mixer.music.play()

    def exit_confirmation():
        play_sound()
        result = messagebox.askyesno("Çıkış Onayı", "Emin misiniz?")
        if result:
            if mixer.get_init():
                mixer.music.stop()
                mixer.quit()
            if root:
                root.destroy()



    cikis_buton = tk.Button(
        frame2,
        text="ÇIKIŞ",
        font=("TkCustomFont", 13, "bold"),
        width=button_width,
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=exit_confirmation
    )
    cikis_buton.pack(side="top", pady=10)


    root.mainloop()

def LoadFrame2():
    clear_widgets(frameMain2)
    clear_widgets(frameMain)
    frameMain2.tkraise()

    data =TaksiDataBase()

    imgLogo = ImageTk.PhotoImage(file=r"assets/commerce.png")
    logoWidget = tk.Label(frameMain2, image=imgLogo, bg=bgColour)
    logoWidget.image = imgLogo
    logoWidget.pack(pady=5)

    tk.Label(
        frameMain2,
        text=data[0],
        bg=bgColour,
        fg="white",  # text colour
        font=("TkHeadingFont", 22)
    ).pack(pady=25)

    data= data[1:]
    for i in data:
        tk.Label(
            frameMain2,
            text=i,
            bg=bgColour,
            fg="white",  # text colour
            font=("Shanti", 14)
        ).pack(fill="both", padx=25)

    def play_sound():
        sound_file = r"C:\Users\Nilay\PycharmProjects\pythonProjectdeneme2\data\düt.mp3"
        mixer.init()
        mixer.music.load(sound_file)
        mixer.music.play()

    tk.Button(
        frameMain2,
        text="DEĞİŞTİR",
        font=("TkHeadingFont", 16, "bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: [LoadFrame2(), play_sound()]
    ).pack(pady=20)

    tk.Button(
        frameMain2,
        text="GERİ",
        font=("TkHeadingFont", 16,"bold"),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame1()
    ).pack(pady=20)
def LoadFrame3():
    clear_widgets(frameMain)
    frameMain3.tkraise()
    #PLAKA
    label_Plaka = tk.Label(frameMain3, text="Plaka:")
    label_Plaka.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    entry_Plaka = tk.Entry(frameMain3)
    entry_Plaka.grid(row=0, column=1, padx=5, pady=5)

    #DURAK
    label_Durak = tk.Label(frameMain3, text="Taksi Durağı:")
    label_Durak.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W) #widget hizalama
    entry_Durak = tk.Entry(frameMain3)
    entry_Durak.grid(row=1, column=1, padx=5, pady=5)

    #TAKSİCİNİNADISOYADI
    label_AdSoyad = tk.Label(frameMain3, text="Taksicinin Adı Soyadı:")
    label_AdSoyad.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    entry_AdSoyad = tk.Entry(frameMain3)
    entry_AdSoyad.grid(row=2, column=1, padx=5, pady=5)

    #BakımDurumu
    label_BakımDurumu = tk.Label(frameMain3, text="Taksinin Bakım Durumu:")
    label_BakımDurumu.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    entry_BakımDurumu = tk.Entry(frameMain3)
    entry_BakımDurumu.grid(row=3, column=1, padx=5, pady=5)


    #TaksiBosMu
    label_BosMu = tk.Label(frameMain3, text="Taksi Boş MU:")
    label_BosMu.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    entry_BosMu = tk.Entry(frameMain3)
    entry_BosMu.grid(row=4, column=1, padx=5, pady=5)

    #TaksiciDilSeviyesi
    label_DilSeviyesi = tk.Label(frameMain3, text="Taksicinin Yabancı Dil Durumu:")
    label_DilSeviyesi.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
    entry_DilSeviyesi = tk.Entry(frameMain3)
    entry_DilSeviyesi.grid(row=5, column=1, padx=5, pady=5)

    #EngelliDestegi
    label_EngelliDestegi = tk.Label(frameMain3, text="Takside Engelli Desteği Var Mı:")
    label_EngelliDestegi.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
    entry_EngelliDestegi = tk.Entry(frameMain3)
    entry_EngelliDestegi.grid(row=6, column=1, padx=5, pady=5)

    #Kapasite
    label_Kapasite= tk.Label(frameMain3, text="Taksinin Kapasitesi:")
    label_Kapasite.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
    entry_Kapasite = tk.Entry(frameMain3)
    entry_Kapasite.grid(row=7, column=1, padx=5, pady=5)

    #KartOdeme
    label_KartOdeme= tk.Label(frameMain3, text="Ödeme Şekli:")
    label_KartOdeme.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)
    entry_KartOdeme = tk.Entry(frameMain3)
    entry_KartOdeme.grid(row=8, column=1, padx=5, pady=5)

    #MesafeTipi
    label_MesafeTipi= tk.Label(frameMain3, text="Mesafe Tipi:")
    label_MesafeTipi.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)
    entry_MesafeTipi = tk.Entry(frameMain3)
    entry_MesafeTipi.grid(row=9, column=1, padx=5, pady=5)



    button_ekle = tk.Button(
     frameMain3,
     text="TAKSİ EKLE",
    font=("TkHeadingFont", 16,"bold"),
    bg="#FFD100",
    fg="black",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:[Insert(entry_Plaka,entry_Durak,entry_AdSoyad,entry_BakımDurumu,entry_BosMu,entry_DilSeviyesi,entry_EngelliDestegi,entry_Kapasite,entry_KartOdeme,entry_MesafeTipi),messagebox.showinfo("EKLENDİ!", "Taksi başarıyla EKLENDİ!")])
    button_ekle.grid(row=11, column=0, columnspan=2, pady=10)

    btn_geri=tk.Button(
        frameMain3,
        text="GERİ",
        font=("TkHeadingFont", 16,"bold"),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1())
    btn_geri.grid(row=12, column=0, columnspan=2, pady=10)
def LoadFrame4():
    clear_widgets(frameMain)
    frameMain7.tkraise()

    listObjects= Select()

    combo_var = tk.StringVar()

    combo = tk.Label(frameMain7, text="Taksi seç")
    combo.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    combo = ttk.Combobox(frameMain7, values= listObjects)
    combo.grid(row=0, column=1, padx=5, pady=15)


    combo.bind('<<ComboboxSelected>>', IndexChangedUpdate)


    btn_geri = tk.Button(
        frameMain7,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()).grid(row=13, column=0, columnspan=2, pady=10)


def LoadFrame5():
    clear_widgets(frameMain)
    frameMain4.tkraise()

    listObjects = Select()

    combo_var = tk.StringVar()
    combo = tk.Label(frameMain4, text="Dilek veya Şikayette Bulunacağınız Taksiyi seçin")
    combo.grid(row=0, column=0, padx=5, pady=10, sticky=tk.W)
    combo = ttk.Combobox(frameMain4, values=listObjects)
    combo.grid(row=0, column=1, padx=5, pady=15)

    combo.bind('<<ComboboxSelected>>', lambda event, combo=combo: IndexChangedUpdate(event, combo))

    label_dilek_sikayet = tk.Label(frameMain4, text="Dilek veya Şikayetler:")
    label_dilek_sikayet.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    entry_dilek_sikayet = tk.Text(frameMain4, height=5, width=50)
    entry_dilek_sikayet.grid(row=1, column=1, padx=5, pady=5)

    btn_kaydet = tk.Button(
        frameMain4,
        text="KAYDET",
        font=("TkHeadingFont", 16),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: save_feedback(entry_dilek_sikayet.get("1.0", "end-1c"), combo.get())
    )
    btn_kaydet.grid(row=2, column=0, columnspan=2, pady=10)

    btn_geri = tk.Button(
        frameMain4,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()
    )
    btn_geri.grid(row=3, column=0, columnspan=2, pady=10)

def LoadFrame6():

    button_width = 30
    clear_widgets(frameMain)
    frameMain5.tkraise()
    btn_goruntule = tk.Button(
        frameMain5,
        text="Dilek ve Şikayetleri Görüntüle",
        font=("TkHeadingFont", 16),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        width=button_width,
        activebackground="#badee2",
        activeforeground="black",
        command=view_feedbacks
    )
    btn_goruntule.grid(row=8, column=1, columnspan=2, pady=10)


    btn_geri = tk.Button(
        frameMain5,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        width=button_width,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()
)
    btn_geri.grid(row=9, column=0, columnspan=2, pady=10)


def LoadFrame7():
    clear_widgets(frameMain)
    frameMain6.tkraise()
    button_width = 20

    global veri_cerceve

    veri_cerceve = tk.Frame(frameMain6)
    veri_cerceve.grid(row=10, column=0, columnspan=2, pady=10)


    buton_turkce = tk.Button(
        frameMain6,
        text="Taksici yalnızca Türkçe biliyor",
        font=("TkHeadingFont", 14,"bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        width=50,
        command=lambda: buton_callback("Taksici yalnızca Türkçe biliyor")
    )
    buton_turkce.grid(row=9, column=0, columnspan=2, pady=10)

    buton_ingilizce = tk.Button(
        frameMain6,
        text="Taksici hem İngilizce hem Türkçe biliyor",
        font=("TkHeadingFont", 14,"bold"),
        bg="#87CEEB",
        fg="black",
        cursor="hand2",
        width=50,
        command=lambda: buton_callback("Taksici hem İngilizce hem Türkçe biliyor")
    )
    buton_ingilizce.grid(row=12, column=0, columnspan=2, pady=10)


    btn_geri = tk.Button(
        frameMain6,
        text="GERİ",
        font=("TkHeadingFont", 14,"bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        width=button_width,
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()
    )
    btn_geri.grid(row=19, column=0, columnspan=2, pady=35)


def LoadFrame8():
    clear_widgets(frameMain)
    frameMain8.tkraise()

    global veri_cerceve

    veri_cerceve = tk.Frame(frameMain8)
    veri_cerceve.grid(row=10, column=0, columnspan=2, pady=10)


    engelli = tk.Button(
        frameMain8,
        text="ENGELLİ DESTEĞİ OLAN TAKSİLER",
        font=("TkHeadingFont", 15, "bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        width=50,
        command=lambda: buton_call("Engelli desteği var")
    )
    engelli.grid(row=5, column=0, columnspan=2, pady=5)

    engellii = tk.Button(
        frameMain8,
        text="ENGELLİ DESTEĞİ OLMAYAN TAKSİLER",
        font=("TkHeadingFont", 15,"bold"),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        width=50,
        command=lambda: buton_call("Engelli desteği yok")
    )
    engellii.grid(row=7, column=0, columnspan=2, pady=5)


    btn_geri = tk.Button(
        frameMain8,
        text="GERİ",
        font=("TkHeadingFont", 14,"bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()
    )
    btn_geri.grid(row=19, column=0, columnspan=2, pady=35)


def LoadFrame9():
    clear_widgets(frameMain)
    frameMain9.tkraise()

    btn_goruntule = tk.Button(
        frameMain9,
        text="DÖNDÜR",
        font=("TkHeadingFont", 17),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=dondur
    )

    btn_goruntule.grid(row=11, column=1, columnspan=2, pady=10)


    global ekstra_kutucuk
    ekstra_kutucuk = tk.Label(
        frameMain9,
        text="İNDİRİM KAZANMAK İÇİN DÖNDÜR BUTONUNA TIKLAYINIZ ",
        font=("TkHeadingFont", 16,"bold"),
        fg="black"
    )
    ekstra_kutucuk.grid(row=9, column=1, columnspan=2, pady=10)

    btn_geri = tk.Button(
        frameMain9,
        text="GERİ",
        font=("TkHeadingFont", 17),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()
    )
    btn_geri.grid(row=13, column=1, columnspan=2, pady=10)


def LoadFrame10():
    clear_widgets(frameMain)
    frameMain10.tkraise()

    global veri_cerceve

    veri_cerceve = tk.Frame(frameMain10)
    veri_cerceve.grid(row=10, column=0, columnspan=2, pady=10)


    BOYUT = tk.Button(
        frameMain10,
        text="EN FAZLA 4 KİŞİLİK TAKSİLER",
        font=("TkHeadingFont", 15, "bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        width=50,
        command=lambda: buton_cal("Maksimum 4 kişilik")
    )
    BOYUT.grid(row=5, column=0, columnspan=2, pady=5)

    BOYUTT = tk.Button(
        frameMain10,
        text="EN FAZLA 10 KİŞİLİK TAKSİLER",
        font=("TkHeadingFont", 15,"bold"),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        width=50,
        command=lambda: buton_cal("Maksimum 10 kişilik")
    )
    BOYUTT.grid(row=7, column=0, columnspan=2, pady=5)


    btn_geri = tk.Button(
        frameMain10,
        text="GERİ",
        font=("TkHeadingFont", 14,"bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()
    )
    btn_geri.grid(row=19, column=0, columnspan=2, pady=35)


def LoadFrame11():
    clear_widgets(frameMain)
    frameMain11.tkraise()

    global veri_cerceve

    veri_cerceve = tk.Frame(frameMain11)
    veri_cerceve.grid(row=10, column=0, columnspan=2, pady=10)


    nakit = tk.Button(
        frameMain11,
        text="YALNIZCA NAKİT KABUL EDEN TAKSİLER",
        font=("TkHeadingFont", 13, "bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        width=55,
        command=lambda: buton_ca("Nakit")
    )
    nakit.grid(row=5, column=0, columnspan=2, pady=5)

    kart = tk.Button(
        frameMain11,
        text="HEM NAKİT HEM KART SEÇENEĞİ OLAN TAKSİLER",
        font=("TkHeadingFont", 13,"bold"),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        width=55,
        command=lambda: buton_ca("Kart")
    )
    kart.grid(row=7, column=0, columnspan=2, pady=5)


    btn_geri = tk.Button(
        frameMain11,
        text="GERİ",
        font=("TkHeadingFont", 14,"bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()
    )
    btn_geri.grid(row=19, column=0, columnspan=2, pady=35)


def LoadFrame12():
    clear_widgets(frameMain)
    frameMain12.tkraise()

    global veri_cerceve

    veri_cerceve = tk.Frame(frameMain12)
    veri_cerceve.grid(row=10, column=0, columnspan=2, pady=10)


    nakit = tk.Button(
        frameMain12,
        text="YAKIN MESAFE YOLCULUĞU DA KABUL EDEN TAKSİLER",
        font=("TkHeadingFont", 13, "bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        width=55,
        command=lambda: buton_c("Yakın Mesafe")
    )
    nakit.grid(row=5, column=0, columnspan=2, pady=5)

    kart = tk.Button(
        frameMain12,
        text="YALNIZCA UZAK MESAFE YOLCULUK KABUL EDEN TAKSİLER",
        font=("TkHeadingFont", 13,"bold"),
        bg="black",
        fg="#FFD100",
        cursor="hand2",
        width=55,
        command=lambda: buton_c("Uzak Mesafe")
    )
    kart.grid(row=7, column=0, columnspan=2, pady=5)


    btn_geri = tk.Button(
        frameMain12,
        text="GERİ",
        font=("TkHeadingFont", 14,"bold"),
        bg="#FFD100",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()
    )
    btn_geri.grid(row=19, column=0, columnspan=2, pady=35)




def LoadFrame13():
    global btn_acil_durum
    clear_widgets(frameMain)
    frameMain13.tkraise()

    def play_sound():
        sound_file = r"C:\Users\Nilay\PycharmProjects\pythonProjectdeneme2\data\polis.mp3"
        mixer.init()
        mixer.music.load(sound_file)
        mixer.music.play()

    def stop_sound():
        mixer.music.stop()



    btn_acil_durum = tk.Button(
        frameMain13,
        text="ACİL DURUM",
        font=("TkHeadingFont", 30),
        bg="black",
        fg="red",
        width=30,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: [acil_durum_callback(), play_sound()]
    )
    btn_acil_durum.grid(row=15, column=0, columnspan=2, pady=20)


    btn_geri = tk.Button(
        frameMain13,
        text="GERİ",
        font=("TkHeadingFont", 20),
        bg="red",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: [LoadFrame1(),stop_sound()]
    )
    btn_geri.grid(row=100, column=0, columnspan=2, pady=250)


def LoadFrame14():
    global btn_sofor_degerlendir
    clear_widgets(frameMain)
    frameMain14.tkraise()

    def soforu_degerlendir():
        yeni_pencere = YildizDegerlendirme(frameMain14)
        yeni_pencere.transient(frameMain14)
        yeni_pencere.grab_set()


    btn_sofor_degerlendir = tk.Button(
        frameMain14,
        text="ŞOFÖRÜ DEĞERLENDİR",
        font=("TkHeadingFont", 20),
        bg="yellow",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=soforu_degerlendir
    )
    btn_sofor_degerlendir.grid(row=15, column=0, columnspan=2, pady=20)


    btn_geri = tk.Button(
        frameMain14,
        text="GERİ",
        font=("TkHeadingFont", 20),
        bg="red",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()
    )
    btn_geri.grid(row=16, column=0, columnspan=2, pady=25)


root = tk.Tk()
root.title("Taksim De Taksim")


frameMain = tk.Frame(root, width=700, height=750, bg=bgColour)
frameMain2 = tk.Frame(root, bg=bgColour)
frameMain3 = tk.Frame(root, bg=bgColour)
frameMain4 = tk.Frame(root, bg=bgColour)
frameMain5 = tk.Frame(root, bg=bgColour)
frameMain6 = tk.Frame(root, bg=bgColour)
frameMain7 = tk.Frame(root, bg=bgColour)
frameMain8 = tk.Frame(root, bg=bgColour)
frameMain9 = tk.Frame(root, bg=bgColour)
frameMain10 = tk.Frame(root, bg=bgColour)
frameMain11 = tk.Frame(root, bg=bgColour)
frameMain12 = tk.Frame(root, bg=bgColour)
frameMain13 = tk.Frame(root, bg=bgColour)
frameMain14 = tk.Frame(root, bg=bgColour)

for frame in (frameMain, frameMain2, frameMain3, frameMain4, frameMain5, frameMain6, frameMain7, frameMain8,frameMain9,frameMain10,frameMain11,frameMain12,frameMain13,frameMain14):
    frame.grid(row=0, column=0)


LoadFrame1()
#your_database()
# run app
root.mainloop()