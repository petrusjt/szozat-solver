import re
from typing import List, Optional

NON_SINGLE_MSGHK = "cs dzs dz gy ly ny sz ty zs".split()
NON_SINGLE_MSGHK_MAP = {asd[1]: asd[0] for asd in enumerate(NON_SINGLE_MSGHK)}


class GuessRecommendation:
    FIRST_GUESS = "etióp"

    def __init__(self, first_guess: bool, present: List[str], not_present: List[str], correct_regex: List[str], lang: str = "hu"):
        self._first_guess = first_guess
        self._present = present.split(",") if present else set()
        self._not_present = not_present.split(",") if not_present else set()
        self._correct_regex = correct_regex.split(",") if correct_regex else set()
        self._wordlist_name = f"usable_words_{lang}.txt"

        self._letter_list = set()

        self.__convert_input()
        self.__compile_present_letters()

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

    def __compile_present_letters(self):
        for item in self._present:
            self._letter_list.add(item)
        for item in self._correct_regex:
            if item != ".":
                if self.__is_all_alnum(item):
                    self._letter_list.add(item)

        for item in self._not_present:
            self._letter_list.discard(item)

    def __is_all_alnum(self, word):
        for char in word:
            if not char.isalnum():
                return False
        return True

    def get_recommendations(self):
        values = self.__get_recommendations()
        if values is str:
            for key, value in NON_SINGLE_MSGHK_MAP.items():
                values = values.replace(str(value), key)
            return values
        else:
            new_list = []
            for item in values:
                for key, value in NON_SINGLE_MSGHK_MAP.items():
                    item = item.replace(str(value), key)
                new_list.append(item)
            return new_list

    def __get_recommendations(self):
        if self._first_guess:
            return self.FIRST_GUESS

        if self._correct_regex:
            return self.__get_list_of_usable_words(self.__get_regex_matches_from_file())
        else:
            return self.__get_list_of_usable_words(None)

    def __get_regex_matches_from_file(self):
        regex = re.compile("".join(self._correct_regex))
        with open(self._wordlist_name) as file:
            return [line.strip() for line in file if regex.match(line.strip())]

    def __get_list_of_usable_words(self, wordlist: Optional[List[str]]):
        if wordlist:
            return self.__filter_wordlist(wordlist)
        else:
            return self.__filter_file()

    def __filter_wordlist(self, wordlist: List[str]):
        return [word for word in wordlist
                if self.__contains_all(word, self._letter_list) and self.__contains_none(word, self._not_present)]

    def __filter_file(self):
        with open(self._wordlist_name) as file:
            return [line.strip() for line in file
                    if self.__contains_all(line.strip(), self._letter_list)
                    and self.__contains_none(line.strip(), self._not_present)]

    def __contains_all(self, word, letters):
        for value in letters:
            if value not in word:
                return False
        return True

    def __contains_none(self, word, letters):
        for value in letters:
            if value in word:
                return False
        return True
