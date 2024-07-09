import socket
import threading
from client_gui import ChatApp
import tkinter as tk
from tkinter import simpledialog

HOST = '127.0.0.1'
PORT = 12345

class ClientApp:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

        self.root = tk.Tk()
        self.app = ChatApp(self.root, self.send_message)

        self.auth()
        self.room()
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()

        self.root.mainloop()

    def auth(self):
        auth_choice = simpledialog.askstring("Authentication", "Enter 1 to Register or 2 to Login:", parent=self.root)
        self.client.send(auth_choice.encode('utf-8'))
        if auth_choice == '1':
            self.register()
        else:
            self.login()

    def register(self):
        username = simpledialog.askstring("Register", "Enter username:", parent=self.root)
        password = simpledialog.askstring("Register", "Enter password:", show='*', parent=self.root)
        self.client.send(f'{username},{password}'.encode('utf-8'))
        message = self.client.recv(1024).decode('utf-8')
        print(message)
        self.login()

    def login(self):
        username = simpledialog.askstring("Login", "Enter username:", parent=self.root)
        password = simpledialog.askstring("Login", "Enter password:", show='*', parent=self.root)
        self.client.send(f'{username},{password}'.encode('utf-8'))

    def room(self):
        room = simpledialog.askstring("Room", "Enter room name:", parent=self.root)
        self.client.send(room.encode('utf-8'))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.app.display_message(message)
            except:
                print("An error occurred!")
                self.client.close()
                break

    def send_message(self, message):
        self.client.send(message.encode('utf-8'))

if __name__ == "__main__":
    ClientApp()
