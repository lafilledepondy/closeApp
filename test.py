# WORKING ON #

import os
import tkinter as tk
import threading
import pyautogui
import time

w = 150
h = 150
size = str(w)+"x"+str(h)


def countdown_and_close(process_name):
    countdown_window = tk.Tk()
    countdown_window.title("Tata")
    countdown_window.geometry(size)

    x = (countdown_window.winfo_screenwidth() - w) // 2  
    y = (countdown_window.winfo_screenheight() - h) // 2 

    countdown_window.geometry(size + "+" + str(x) + "+" + str(y))

    countdown_label = tk.Label(countdown_window, text="", font=("Helvetica", 40), fg="#A52A2A")
    countdown_label.pack(padx=20, pady=40)

    def update_countdown_label(count):
        countdown_label.config(text=str(count))

    for i in range(3, 0, -1):
        update_countdown_label(i)
        countdown_window.update()
        countdown_window.after(1000) 

    countdown_window.destroy()
    close_process(process_name)

    # Give some time for the application to close before attempting to click
    time.sleep(3) 

    # Simulate clicking on the "drop call" button
    drop_call_button = pyautogui.locateCenterOnScreen('drop_call_button.png')
    if drop_call_button:
        pyautogui.click(drop_call_button)
        print("Call dropped successfully.")
    else:
        print("Drop call button not found.")


def close_process(process_name):
    command = f"pgrep {process_name}"
    pid = os.popen(command).read().strip()

    if pid:
        os.system(f"kill {pid}")
        print(f"Closed {process_name}")
    else:
        print(f"Process {process_name} not found")


def main():
    process_name = "telegram"
    countdown_thread = threading.Thread(target=countdown_and_close, args=(process_name,))
    countdown_thread.start()

if __name__ == "__main__":
    main()
