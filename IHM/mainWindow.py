from PyQt6.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QDialog
import controller.client
from IHM.clientDialog import ClientDialog


class MainWindow(QWidget):
    # constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reservation Restaurant")
        self.setGeometry(100, 100, 400, 300)

        #       #definition de ma list de client
        self.client_list = QListWidget(self)
        # creation button
        self.button_add_client = QPushButton("Ajouter un client ")
        # creation du comportment
        self.button_add_client.clicked.connect(self.open_dialog_create_client)

        layout = QVBoxLayout()
        layout.addWidget(self.client_list)
        layout.addWidget(self.button_add_client)
        self.setLayout(layout)

    def open_dialog_create_client(self):
        dialog = ClientDialog()
        if dialog.exec() == QDialog.accepted:
            print("c'est ajouter ! ")
