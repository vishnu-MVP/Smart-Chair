import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from sklearn import svm
import numpy as np
from bluedot.btcomm import BluetoothServer
from signal import pause

def data_received(data):
    print(data)
    s.send(data)

s = BluetoothServer(data_received)
pause()
X_train = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
y_train = np.array([0, 1, 2, 3, 4, 5])
clf = svm.SVC()
clf.fit(X_train, y_train)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Smart Chair Control')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        btn_current_position = QPushButton('Current Position', self)
        btn_current_position.clicked.connect(self.show_current_position)
        layout.addWidget(btn_current_position)

        btn_remote_access = QPushButton('Remote Access', self)
        btn_remote_access.clicked.connect(self.remote_access)
        layout.addWidget(btn_remote_access)

        btn_see_logs = QPushButton('See Logs', self)
        btn_see_logs.clicked.connect(self.see_logs)
        layout.addWidget(btn_see_logs)

        self.lbl_position = QLabel('Position:', self)
        layout.addWidget(self.lbl_position)

        self.setLayout(layout)
        self.setStyleSheet(
            "QWidget {"
            "   background-color: #f0f0f0;"
            "   color: #333;"
            "   font-family: Arial, sans-serif;"
            "   border: 2px solid #555;"
            "   border-radius: 5px;"
            "   padding: 10px;"
            "}"
            "QPushButton {"
            "   background-color: #007bff;"
            "   color: white;"
            "   padding: 5px 10px;"
            "   border: none;"
            "   border-radius: 3px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #0056b3;"
            "}"
        )
        self.show()

    def show_current_position(self):
        # Code to receive data from Raspberry Pi and classify using SVM
        # Dummy data for demonstration
        data = np.array([[4, 5]])  #Should fetch from Raspberry Pi 
        position = clf.predict(data)[0]
        self.lbl_position.setText(f'Position: {position}')

    def remote_access(self):
        # Code for remote access functionality
        pass

    def see_logs(self):
        # Code to display logs
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
