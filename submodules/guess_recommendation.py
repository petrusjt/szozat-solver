import sys
from argparse import Namespace

NON_SINGLE_MSGHK = "cs dzs dz gy ly ny sz ty zs".split()
NON_SINGLE_MSGHK_MAP = {asd[1]: asd[0] for asd in enumerate(NON_SINGLE_MSGHK)}


class GuessRecommendation:
    FIRST_GUESS = "alant"

    def __init__(self, first_guess: bool, present: str, not_present: str, correct_regex: str):
        self._first_guess = first_guess
        self._present = present.split(",") if present else ""
        self._not_present = not_present.split(",") if not_present else ""
        self._correct_regex = correct_regex.split(",") if correct_regex else ""

        self._letter_list = set()

        self.__convert_input()

    def get_recommendations(self):
        if self._first_guess:
            return self.FIRST_GUESS

    def __compile_present_letters(self):
        self._letter_list += self._present
        self._letter_list += self._correct_regex

        for item in self._not_present:
            self._letter_list.discard(item)

    def __convert_input(self):
        for i in range(len(self._present)):
            for key, value in NON_SINGLE_MSGHK_MAP.items():
                self._present[i] = self._present[i].replace(key, str(value))
        for i in range(len(self._not_present)):
            for key, value in NON_SINGLE_MSGHK_MAP.items():
                self._not_present[i] = self._not_present[i].replace(key, str(value))
        for i in range(len(self._correct_regex)):
            for key, value in NON_SINGLE_MSGHK_MAP.items():
                self._correct_regex[i] = self._correct_regex[i].replace(key, str(value))
