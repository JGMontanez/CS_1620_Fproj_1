# logic file
from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda:self.submit())

    def submit(self):
        """
        Function to write vote to csv file
        :return:
        """
        try:
            #validate id
            id = int(self.input_id.text())
            #if ID is not 5 numbers,
            if len(str(id)) !=5:
                raise ValueError
            #elif id in file #if the id is in csv file raise an error




        except ValueError:
            self.label_msg.setText(f'Invalid ID. Please enter 5 digit ID.')

        except:
            self.label_msg.setText(f'Invalid ID.')





