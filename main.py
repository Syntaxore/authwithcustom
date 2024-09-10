import customtkinter as ctk

# Создаем главное окно
app = ctk.CTk()

# Устанавливаем размер окна
app.geometry("500x600")
app.title("Program")

# Запрещаем изменение размера окна
app.resizable(False, False)

# Создаем фрейм с отступом 1 см (примерно 38 пикселей)
frame = ctk.CTkFrame(app, width=424, height=524)  # 400 - 38*2 = 324, 500 - 38*2 = 424
frame.pack(pady=38, padx=38)  # Отступ 38 пикселей

# Создаем и добавляем виджеты в фрейм
label = ctk.CTkLabel(frame, text="Sign up", font=("New-York", 23))
label.place(x=15, y=10)  # Позиция по x и y

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

#btn2 = ctk.CTkButton(frame, text="Региистрация", width=210, font=("New-York", 15))
#btn2.place(x=215, y=495)  # Позиция по x и y


app.mainloop()
