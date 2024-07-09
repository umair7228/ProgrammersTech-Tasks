import socket
import threading
import hashlib

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}
rooms = {}

def broadcast(message, room):
    for client in rooms[room]:
        client.send(message)

def handle(client, room):
    while True:
        try:
            message = client.recv(1024)
            if message.decode('utf-8').startswith("PRIVATE:"):
                recipient, msg = message.decode('utf-8')[8:].split(':')
                if recipient in clients:
                    clients[recipient].send(msg.encode('utf-8'))
            else:
                broadcast(message, room)
        except:
            rooms[room].remove(client)
            client.close()
            break

def register_user(client):
    client.send('REGISTER'.encode('utf-8'))
    credentials = client.recv(1024).decode('utf-8').split(',')
    username, password = credentials[0], hashlib.sha256(credentials[1].encode()).hexdigest()
    with open('users.txt', 'a') as f:
        f.write(f'{username},{password}\n')
    client.send('Registered successfully!'.encode('utf-8'))

def authenticate_user(client):
    client.send('LOGIN'.encode('utf-8'))
    credentials = client.recv(1024).decode('utf-8').split(',')
    username, password = credentials[0], hashlib.sha256(credentials[1].encode()).hexdigest()
    with open('users.txt', 'r') as f:
        users = f.readlines()
        for user in users:
            stored_username, stored_password = user.strip().split(',')
            if stored_username == username and stored_password == password:
                return username
    return None

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('AUTH'.encode('utf-8'))
        auth_choice = client.recv(1024).decode('utf-8')
        if auth_choice == '1':
            register_user(client)
        nickname = authenticate_user(client)
        if nickname:
            clients[nickname] = client

            client.send('ROOM'.encode('utf-8'))
            room = client.recv(1024).decode('utf-8')
            if room not in rooms:
                rooms[room] = []
            rooms[room].append(client)

            print(f'Nickname of the client is {nickname} in room {room}!')
            broadcast(f'{nickname} joined the chat!'.encode('utf-8'), room)
            client.send('Connected to the server!'.encode('utf-8'))

            thread = threading.Thread(target=handle, args=(client, room))
            thread.start()
        else:
            client.send('Authentication failed!'.encode('utf-8'))
            client.close()

print('Server is listening...')
receive()
