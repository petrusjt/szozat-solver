import sys
from typing import List

from PyQt5.QtWidgets import QApplication, QMainWindow

from src.szozat_solver.submodules.guess_recommendation import GuessRecommendation
from szozat_gui import Ui_MainWindow


class Controller:
    def __init__(self):
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.ui.btn_present.clicked.connect(self.btn_present_clicked)
        self.ui.btn_not_present.clicked.connect(self.btn_not_present_clicked)
        self.ui.btn_search.clicked.connect(self.search_clicked)

        self.main_window.show()

        self.present_letters: List[str] = []
        self.not_present_letters: List[str] = []
        self.regex: List[str] = []

    def btn_present_clicked(self):
        present = self.ui.txt_present.text().strip()

        if len(present) > 0:
            self.present_letters.append(present)
            self.ui.lst_present.addItem(present)
            self.ui.txt_present.clear()

    def btn_not_present_clicked(self):
        not_present = self.ui.txt_not_present.text().strip()

        if len(not_present) > 0:
            self.not_present_letters.append(not_present)
            self.ui.lst_not_present.addItem(not_present)
            self.ui.txt_not_present.clear()

    def search_clicked(self):
        joined_regex = (f"{self.ui.txt_regex1.text()},{self.ui.txt_regex2.text()},{self.ui.txt_regex3.text()},"
                        f"{self.ui.txt_regex4.text()},{self.ui.txt_regex5.text()}")
        recommendation = GuessRecommendation(False,
                                             ",".join(self.present_letters),
                                             ",".join(self.not_present_letters),
                                             joined_regex)

        self.ui.lst_usable_words.clear()
        self.ui.lst_usable_words.addItems(recommendation.get_recommendations())


app = QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec_())
