from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
import controller.client as client_controller
from entities.client import Client


class ClientDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitel("Ajouter un nouveau client")

        self.lastname_label = QLabel("lastname : ")
        self.lastname_line = QLineEdit()

        self.firstname__label = QLabel("firstname: ")
        self.firstname_line = QLineEdit()

        self.gsm_label = QLabel("Gsm : ")
        self.name_line = QLineEdit
        #parametre du bouton

        self.add_button = QPushButton("Ajouter",self)
        self.add_button.clicked.connect(self.add_client)

        layout = QVBoxLayout()
        layout.addWidget(self.lastname_label)
        layout.addWidget(self.lastname_line)

        layout.addWidget(self.firstname_label)
        layout.addWidget(self.fistname_line)

        layout.addWidget(self.gsm_label)
        layout.addWidget(self.gsm_line)

        layout.addWidget(self.add_button)
        self.setLayout(layout)

    def add_client(self):
        firstname = self.firstname_line.text()
        lastname = self.lastname_line.text()
        gsm = self.gsm_line.text()

        client_controller.create_client(Client(
            nom = lastname,
            prenom = firstname,
            gsm=gsm,
        ))
