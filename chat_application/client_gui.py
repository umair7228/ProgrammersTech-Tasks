import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog, simpledialog
import emoji

class ChatApp:
    def __init__(self, root, send_callback):
        self.root = root
        self.send_callback = send_callback
        self.root.title("Desktop Chat Application")

        # Set background color
        self.root.configure(bg="#2c3e50")

        # Create header
        self.header = tk.Label(root, text="Desktop Chat Application", font=("Helvetica", 16, "bold"), bg="#34495e", fg="#ecf0f1")
        self.header.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        # Chat history
        self.chat_history = scrolledtext.ScrolledText(root, state='disabled', width=60, height=20, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 12))
        self.chat_history.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Message input
        self.msg_entry = tk.Entry(root, width=40, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 12))
        self.msg_entry.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.msg_entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message, bg="#1abc9c", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
        self.send_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # Emoji button
        self.emoji_button = tk.Button(root, text="😊", command=self.add_emoji, bg="#f39c12", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
        self.emoji_button.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

        # File attachment button
        self.file_button = tk.Button(root, text="Attach File", command=self.attach_file, bg="#3498db", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
        self.file_button.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

    def send_message(self, event=None):
        message = self.msg_entry.get()
        if message:
            self.display_message(f"You: {message}")
            self.send_callback(message)
            self.msg_entry.delete(0, tk.END)

    def add_emoji(self):
        emoji_list = [":smile:", ":laughing:", ":blush:", ":heart_eyes:", ":kissing_heart:"]
        emoji_choice = simpledialog.askstring("Choose Emoji", "Enter emoji code:")
        if emoji_choice in emoji_list:
            self.msg_entry.insert(tk.END, emoji.emojize(emoji_choice))

    def attach_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.display_message(f"You sent a file: {file_path}")
            self.send_callback(f"FILE:{file_path}")

    def display_message(self, message):
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.config(state='disabled')
        self.chat_history.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root, None)
    root.mainloop()
