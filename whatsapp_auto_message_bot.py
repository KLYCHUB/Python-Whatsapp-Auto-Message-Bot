from tkinter import Button, Entry, Frame, Label, StringVar, Tk, messagebox
import webbrowser
from pyautogui import LEFT, RIGHT
import pyautogui
import pywhatkit as kit

root = Tk()
root.title('KLYC MEDYA Whatsapp Auto Message') # Üst Gezinme Çubuğunun Başlığı
root.configure(bg="#008080") # Arka plan rengi
root.resizable(False, False) # Ekronın yeniden boyutlandırılmasını engeller

# Üst gezinme çubuğunu gizler
root.overrideredirect(True)

# uygulama Boyutları
app_width = 600
app_height = 200

# Ekran boyutunu al
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Ortalıyoruz
x = (width - app_width) / 2
y = (height - app_height) / 2

# Formu ekranın ortasına konumlandır
root.geometry("%dx%d+%d+%d" % (app_width, app_height, x, y))

# Eren KALAYCI
my_label = Label(root, text="Produced By Eren Kalaycı", font=('Pacifico',15),bg="#008080")
my_label.pack(pady=18)

# Frame oluşturma
spam_frame = Frame(root)
spam_frame.pack(pady=5)

# Tam sayı kontrolü
def validate_int(text):
    if text.isdigit():
        return True
    return False

# Birinci giriş kutusu ve etiketi
number = StringVar()
label1 = Label(spam_frame, text="Phone Num", font=("Signika", 10), bg="#f0f0f0")
label1.pack(side="left", padx=5)
numberEntry = Entry(spam_frame, textvariable=number,width=14)
numberEntry.pack(side="left", padx=5)

# İkinci giriş kutusu ve etiketi
message = StringVar()
label2 = Label(spam_frame, text="Message", font=("Signika", 10), bg="#f0f0f0")
label2.pack(side="left", padx=5)
messageEntry = Entry(spam_frame, textvariable=message)
messageEntry.pack(side="left", padx=5)

# Üçüncü giriş kutusu ve etiketi
hour = StringVar()
label3 = Label(spam_frame, text="Hour", font=("Signika", 10), bg="#f0f0f0")
label3.pack(side="left", padx=5)
validate_int_cmd = spam_frame.register(validate_int)
hourEntry = Entry(spam_frame, textvariable=hour, validate="key", validatecommand=(validate_int_cmd, '%S'),width=3)
hourEntry.pack(side="left", padx=5)

# Dördüncü giriş kutusu ve etiketi
minute = StringVar()
label4 = Label(spam_frame, text="Minute", font=("Signika", 10), bg="#f0f0f0")
label4.pack(side="left", padx=5)
validate_int_cmd = spam_frame.register(validate_int)
minuteEntry = Entry(spam_frame, textvariable=minute, validate="key", validatecommand=(validate_int_cmd, '%S'),width=3)
minuteEntry.pack(side="left", padx=5)
    
# Otomatik mesaj yollama fonksiyonumuz
def autoSend():
    try:
        kit.sendwhatmsg(number.get(), message.get(), int(hour.get()), int(minute.get()))
        
    except Exception as e:
        print(e)
        
# Pencereyi kapatmak için
def close_application():
    result = messagebox.askyesno("Application Close", "Are you sure you want to close the application?")
    if result:
        root.destroy()
        
# Düğmeleri tutmak için bir çerçeve oluşturun
button_frame = Frame(root)
button_frame.pack(pady=10)

# Send button
myButton = Button(button_frame, text="Send", command=autoSend, fg='white', bg='#eb3d34', pady=5,padx=50,)
myButton.pack(side=LEFT)

# Application Close button
close_applicationButton = Button(button_frame, text="Close", command=close_application, fg='white', bg='#eb3d34', pady=5,padx=50)
close_applicationButton.pack(side=RIGHT)

# Linki Açar
def tutorial():
    webbrowser.open("https://github.com/KLYCHUB/python_whatsapp_auto_message_bot/")
    
# Linki Açar
def open_web():
    webbrowser.open("https://klychub.github.io//")

# Link Butonu
tutorial_button = Button(button_frame, text="Tutorial", command=tutorial, fg='white', bg='#eb3d34', pady=5,padx=42)
tutorial_button.pack(side=LEFT)

# Link Butonu
web_button = Button(button_frame, text="Web Site", command=open_web, fg='white', bg='#eb3d34', pady=5,padx=42)
web_button.pack(side=RIGHT)

root.mainloop()

