# credito.py

# Import list:
import os
import time
import threading
import ctypes
from pathlib import Path

class Credito:
    def __init__(self):
        self.config_file = None
        self.credits = ""

    def config(self, config_file):
        self.config_file = config_file
        self.load_credits()

    def load_credits(self):
        if not self.config_file or not Path(self.config_file).exists():
            print("Configuration file not found.")
            return
        with open(self.config_file, 'r') as file:
            self.credits = file.read()

    def show_credits(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.credits)
        time.sleep(10)
        # Clear console again after delay
        os.system('cls' if os.name == 'nt' else 'clear')

credito = Credito()

# Deffently handles stuff
def handler():
    if credito.config_file:
        credito.show_credits()

# Listens for keypresses
def listen_for_keypress():
    # The following code uses a low-level API to capture global key presses
    # On Windows, ctypes is used to capture keyboard events.
    # On other systems, you may need different methods like editing this because I am not doing that.
    while True:
        user_input = ctypes.windll.kernel32.GetAsyncKeyState(0x4F)  # O key
        ctrl_pressed = ctypes.windll.user32.GetAsyncKeyState(0x11)  # CTRL key
        
        if user_input & 0x8000 and ctrl_pressed & 0x8000:
            handler()


# Runs at the start of script
if __name__ == "__main__":
    # Run the keypress listener in a separate thread
    threading.Thread(target=listen_for_keypress, daemon=True).start()
    # Keep the script running to listen for keypresses
    input("Press Enter to exit...\n")
