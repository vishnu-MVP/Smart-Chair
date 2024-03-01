import socket
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
import sys
server_address = "E4:5F:01:CD:3D:D6"  # Replace with the actual Bluetooth address of the server
port = 1  # RFCOMM port number
client_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client_socket.connect((server_address, port))
data = client_socket.recv(1024)
while True:
    print(f"Received: {data.decode()}")
client_socket.close()
'''
if __name__ == "__main__":
    app = QApplication([])
    window = BluetoothClient()
    window.show()
    app.exec_()
'''
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BluetoothClient()
    sys.exit(app.exec_())
'''