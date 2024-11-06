import subprocess
import os

def run_scripts():
    # Пути к вашим скриптам
    script1 = os.path.join(os.getcwd(), "rcon.py")  # Ваш основной скрипт
    script2 = os.path.join(os.getcwd(), "create_shortcut.py")  # Скрипт для создания ярлыков

    # Запускаем оба скрипта с помощью subprocess
    subprocess.Popen(['python', script1])  # Запускает основной скрипт
    subprocess.Popen(['python', script2])  # Запускает скрипт для ярлыков

    print("Both scripts are now running.")

if __name__ == "__main__":
    run_scripts()
