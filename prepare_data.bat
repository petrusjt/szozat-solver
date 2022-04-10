@echo off

py prepare_word_list/prepare_obvious.py
py prepare_word_list/separate_double_double.py

py prepare_word_list/convert_short_double_words.py
py prepare_word_list/convert_double_double_words.py

py prepare_word_list/concat_usable_words.py