from PyQt6.QtWidgets import QApplication , QWidget
import sys

from IHM.mainWindow import MainWindow
from config.database import Base, engine, session

from entities.restaurant import Restaurant
from entities.restaurantCreneau import RestaurantCreneau
from entities.reserver import Reserver
from entities.plat import Plat
from entities.creneau import Creneau
from entities.client import Client
from entities.categorie import Categorie
from entities.cartePlat import CartePlat
from entities.carte import Carte


# This is  sample Python script
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #creation de la vue (la page )
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

    #creation de la vue (la page )
    # window =QWidget()
    # window.setWindowTitle("Reservation Restaurant")
    # window.setGeometry(100,100,400,300)
    #
    # window.show()
    # sys.exit(app.exec())


    #BD
    Base.metadata.create_all(bind=engine)
    nouveau_restaurant = Restaurant(
        capacite_max_midi=15,
        capacite_max_soir=20,
        horaire_midi="8h-15h",
        horaire_soir="15h-18"
    )

    session.add(nouveau_restaurant)
    session.commit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
