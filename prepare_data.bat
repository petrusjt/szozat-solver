@echo off

py prepare_obvious.py
py separate_double_double.py

py convert_short_double_words.py
py convert_double_double_words.py

py concat_usable_words.py