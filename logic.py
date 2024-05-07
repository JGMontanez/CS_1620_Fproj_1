# logic file
from PyQt6.QtWidgets import *
from gui import *
import os.path
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda: self.submit())

    def submit(self) -> None:
        """
        method validate data for writing
        :return:
        """
        try:
            voter_id = int(self.input_id.text())
            vote = ''
            if len(str(voter_id)) != 5:
                raise ValueError
            # get candidate vote
            if self.radio_cand1.isChecked():
                vote = self.radio_cand1.text()
            elif self.radio_cand2.isChecked():
                vote = self.radio_cand2.text()
            else:  # if no candidate selected raise an error
                raise KeyError

            self.label_msg.setText(f'voted {vote}')
            self.write_csv(str(voter_id), vote)

        except ValueError:
            self.label_msg.setText("<font color='red'> Invalid ID. Please enter 5 digit ID.")
            self.clear()
        except NameError:
            self.label_msg.setText("<font color='red'> Invalid ID. Already voted.")
            self.clear()
        except KeyError:
            self.label_msg.setText("<font color='red'> Please select a candidate.")
            self.clear()

    def write_csv(self, vote_id: str, candidate: str) -> None:
        """
        method to create/update data file
        :param vote_id: 5 digit number
        :param candidate: string
        :return: none
        """
        if os.path.isfile('data.csv'):  # write to file
            with open('data.csv', 'r+', newline="") as data_csv:
                data_reader = csv.reader(data_csv, delimiter=",")
                content = csv.writer(data_csv)
                # to prevent repeat votes look for id
                for line in data_reader:
                    if line[0] == vote_id:
                        raise NameError

                content.writerow([vote_id, candidate])

        else:  # set up file
            with open('data.csv', 'w', newline='') as data_csv:
                content = csv.writer(data_csv)
                content.writerow(['Voter ID', 'Vote'])

                content.writerow([vote_id, candidate])

    def clear(self) -> None:
        """
        method to clear inputs
        :return: none
        """
        self.input_id.setText('')
        self.radio_group.setExclusive(False)
        for button in self.radio_group.buttons():
            button.setChecked(False)
        self.radio_group.setExclusive(True)
