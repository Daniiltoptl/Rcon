import os
import sys
import win32com.client

def create_shortcut():
    # Путь к вашему .exe файлу (нужно указать полный путь)
    exe_path = os.path.join(os.getcwd(), "main_program.exe")  # Путь к основному .exe файлу
    desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")  # Путь к рабочему столу
    start_menu = os.path.join(os.path.join(os.environ["APPDATA"]), "Microsoft\\Windows\\Start Menu\\Programs")  # Путь к меню Пуск

    # Имя ярлыка
    shortcut_name = "Rcon Console"  # Название ярлыка

    # Создаем ярлык на рабочем столе
    desktop_shortcut = os.path.join(desktop, f"{shortcut_name}.lnk")
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(desktop_shortcut)
    shortcut.TargetPath = exe_path
    shortcut.WorkingDirectory = os.getcwd()
    shortcut.IconLocation = exe_path  # Иконка ярлыка (можно указать свой путь к .ico)
    shortcut.save()

    # Создаем ярлык в меню пуск
    start_menu_shortcut = os.path.join(start_menu, f"{shortcut_name}.lnk")
    shortcut = shell.CreateShortcut(start_menu_shortcut)
    shortcut.TargetPath = exe_path
    shortcut.WorkingDirectory = os.getcwd()
    shortcut.IconLocation = exe_path  # Иконка ярлыка
    shortcut.save()

    print("Shortcuts created on Desktop and Start Menu.")

if __name__ == "__main__":
    create_shortcut()
