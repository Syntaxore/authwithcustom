import customtkinter as ctk


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x600")
        self.root.title("Program")

        # Создаем фрейм с отступом 1 см (примерно 38 пикселей)
        self.frame = ctk.CTkFrame(self.root, width=424, height=524)
        self.frame.pack(pady=38, padx=38)

        self.create_signup_frame()
        self.create_register_frame()

        # Показываем фрейм регистрации по умолчанию
        self.show_signup_frame()

    def create_signup_frame(self):
        # Создаем и добавляем виджеты в фрейм
        label = ctk.CTkLabel(self.frame, text="Sign up", font=("New-York", 23))
        label.place(x=165, y=10)

        self.entry1 = ctk.CTkEntry(self.frame, width=305, height=40, font=("New-York", 20))
        self.entry1.place(x=10, y=160)

        self.entry2 = ctk.CTkEntry(self.frame, width=305, height=40, font=("New-York", 20))
        self.entry2.place(x=10, y=250)

        label1 = ctk.CTkLabel(self.frame, text="Login", font=("New-York", 15))
        label1.place(x=12, y=130)

        label2 = ctk.CTkLabel(self.frame, text="Password", font=("New-York", 15))
        label2.place(x=12, y=220)

        btn1 = ctk.CTkButton(self.frame, text="Sign up", width=424, font=("New-York", 15), height=45)
        btn1.place(x=0, y=480)

        # Кнопка "Register", которая переключает на фрейм регистрации
        btn2 = ctk.CTkButton(self.frame, text="Register", width=20, font=("New-York", 15), fg_color="transparent",
                             command=self.show_register_frame)
        btn2.place(x=10, y=300)

    def create_register_frame(self):
        # Создаем содержимое фрейма регистрации
        self.register_frame = ctk.CTkFrame(self.root, width=424, height=524)

        register_label = ctk.CTkLabel(self.register_frame, text="Register", font=("New-York", 23))
        register_label.place(x=165, y=10)

        self.register_entry1 = ctk.CTkEntry(self.register_frame, width=305, height=40, font=("New-York", 20))
        self.register_entry1.place(x=10, y=160)

        self.register_entry2 = ctk.CTkEntry(self.register_frame, width=305, height=40, font=("New-York", 20))
        self.register_entry2.place(x=10, y=250)

        register_label1 = ctk.CTkLabel(self.register_frame, text="Login", font=("New-York", 15))
        register_label1.place(x=12, y=130)

        register_label2 = ctk.CTkLabel(self.register_frame, text="Password", font=("New-York", 15))
        register_label2.place(x=12, y=220)

        register_btn = ctk.CTkButton(self.register_frame, text="Submit", width=424, font=("New-York", 15), height=45)
        register_btn.place(x=0, y=480)

        # Кнопка для возврата на страницу входа
        back_btn = ctk.CTkButton(self.register_frame, text="Back to Sign Up", command=self.show_signup_frame, fg_color="transparent", font=("New-York", 15))
        back_btn.place(x=10, y=300)

    def show_signup_frame(self):
        self.register_frame.pack_forget()  # Скрываем страницу регистрации
        self.frame.pack(pady=38, padx=38)  # Показываем страницу входа

    def show_register_frame(self):
        self.frame.pack_forget()  # Скрываем страницу входа
        self.register_frame.pack(pady=38, padx=38)  # Показываем страницу регистрации


if __name__ == "__main__":
    app = ctk.CTk()
    my_app = App(app)
    app.mainloop()
