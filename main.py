# remake of lab 01
from logic import *


# TODO: create gui window that displays vote menu
# TODO: create logic file

def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
