# logic file
from PyQt6.QtWidgets import *
from gui import *
import os.path
import csv

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
            # validate id
            voter_id: int = int(self.input_id.text())
            vote :str = ''
            # if ID is not 5 numbers,
            if len(str(voter_id)) != 5:
                raise ValueError
            # elif id in file #if the id is in csv file raise an error
            # get candidate vote
            if self.radio_cand1.isChecked():
                vote = self.radio_cand1.text()
            elif self.radio_cand2.isChecked():
                vote = self.radio_cand2.text()
            else: # if no candidate selected raise an error
                raise VoteError
            self.label_msg.setText(f'voted {vote}')
            self.write_csv(voter_id,vote)

        except ValueError:
            self.label_msg.setText(f'Invalid ID. Please enter 5 digit ID.')

        except Exception as VoteError:
            self.label_msg.setText(f'Please Select a candidate')

    def write_csv(self,vote_id,candidate):
        """

        :param vote_id:
        :param candidate:
        :return:
        """
        if os.path.isfile('data.csv'):
            with open('data.csv', 'a') as output_csv:
                contents = csv.writer(output_csv)
        else:
            with open('data.csv', 'w',newline = '') as output_csv:
                contents = csv.writer(output_csv)
                contents.writerow(['Voter ID', 'Vote'])

    def clear(self):
        self.input_id.setText('')
        self.radio_cand1.setChecked(False)
        self.radio_cand2.setChecked(False)
        self.label_msg.setText('')
