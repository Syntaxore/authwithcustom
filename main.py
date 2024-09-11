import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x600")
app.title("Program")


# Создаем фрейм с отступом 1 см (примерно 38 пикселей)
frame = ctk.CTkFrame(app, width=424, height=524)  # 400 - 38*2 = 324, 500 - 38*2 = 424
frame.pack(pady=38, padx=38)  # Отступ 38 пикселей

# Создаем и добавляем виджеты в фрейм
label = ctk.CTkLabel(frame, text="Sign up", font=("New-York", 23))
label.place(x=165, y=10)  # Позиция по x и y

entry1 = ctk.CTkEntry(frame, width=305, height=40, font=("New-York", 20))
entry1.place(x=10, y=160)  # Позиция по x и y

entry2 = ctk.CTkEntry(frame, width=305, height=40, font=("New-York", 20))
entry2.place(x=10, y=250)  # Позиция по x и y

label1 = ctk.CTkLabel(frame, text="Login", font=("New-York", 15))
label1.place(x=12, y=130)  # Позиция по x и y

label2 = ctk.CTkLabel(frame, text="Password", font=("New-York", 15))
label2.place(x=12, y=220)  # Позиция по x и y

btn1 = ctk.CTkButton(frame, text="Sign up", width=424, font=("New-York", 15), height=45)
btn1.place(x=0, y=480)  # Позиция по x и y

btn2 = ctk.CTkButton(frame, text="Register", width=20, font=("New-York", 15), fg_color="transparent")
btn2.place(x=10, y=300)  # Позиция по x и y


try:
    app.mainloop()
except KeyboardInterrupt:
    print("App closed!")

