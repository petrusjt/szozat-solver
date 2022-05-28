import argparse

__parser = argparse.ArgumentParser()
__parser.add_argument("--first-guess", action="store_true", help="Első tipp")
__parser.add_argument("--present")
__parser.add_argument("--not-present")
__parser.add_argument("--correct-regex")

ARGS = __parser.parse_args()
