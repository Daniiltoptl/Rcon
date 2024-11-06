import tkinter as tk
from tkinter import messagebox
from mcrcon import MCRcon

class RconApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RCON Minecraft Console")
        
        # Инициализация переменных
        self.host = tk.StringVar()
        self.port = tk.IntVar(value=25575)
        self.password = tk.StringVar()
        self.rcon = None

        # Фрейм для подключения
        self.connection_frame = tk.Frame(self.root)
        self.connection_frame.pack(padx=10, pady=10)

        # Фрейм для команд
        self.command_frame = tk.Frame(self.root)
        self.command_frame.pack(padx=10, pady=10)

        self.create_connection_frame()
        self.create_command_frame()

    def create_connection_frame(self):
        # Ввод данных подключения
        tk.Label(self.connection_frame, text="IP-адрес сервера:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.connection_frame, textvariable=self.host).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.connection_frame, text="Порт (по умолчанию 25575):").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self.connection_frame, textvariable=self.port).grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.connection_frame, text="Пароль RCON:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(self.connection_frame, textvariable=self.password, show="*").grid(row=2, column=1, padx=5, pady=5)
        
        self.apply_button = tk.Button(self.connection_frame, text="Применить", command=self.apply_connection)
        self.apply_button.grid(row=3, column=0, columnspan=2, pady=10)

    def create_command_frame(self):
        # Ввод и выполнение команд
        tk.Label(self.command_frame, text="Введите команду:").grid(row=0, column=0, padx=5, pady=5)
        self.command_input = tk.Entry(self.command_frame, width=50)
        self.command_input.grid(row=1, column=0, padx=5, pady=5)
        
        self.command_button = tk.Button(self.command_frame, text="Отправить команду", command=self.send_command)
        self.command_button.grid(row=2, column=0, pady=10)

        self.output_text = tk.Text(self.command_frame, height=10, width=50)
        self.output_text.grid(row=3, column=0, padx=5, pady=5)

    def apply_connection(self):
        # Обработчик для кнопки "Применить"
        host = self.host.get()
        port = self.port.get()
        password = self.password.get()

        try:
            self.rcon = MCRcon(host, password, port)
            # Пробуем подключиться к серверу
            self.rcon.connect()
            messagebox.showinfo("Успех", "Подключение установлено успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось подключиться: {e}")

    def send_command(self):
        if not self.rcon:
            messagebox.showerror("Ошибка", "Не подключено к серверу!")
            return

        command = self.command_input.get()

        if command:
            try:
                response = self.rcon.command(command)
                self.output_text.insert(tk.END, f"Команда: {command}\nОтвет: {response}\n\n")
            except Exception as e:
                self.output_text.insert(tk.END, f"Ошибка: {e}\n\n")
        else:
            messagebox.showwarning("Предупреждение", "Введите команду для выполнения.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RconApp(root)
    root.mainloop()
