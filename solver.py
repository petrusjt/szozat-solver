import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--first-guess", action="store_true", help="Első tipp")
parser.add_argument("--present")
parser.add_argument("--correct-regex")
# TODO minden fájlra külön logika kell -> usable_words.txt nem használható
#   - átgondolni, hogy lehet-e egységesíteni
#       - maybe dzs dz sorrend? <- usable_words.txt most ilyen, jó így? - így marad, ha nem jó, módosul

args = parser.parse_args()

if args.first_guess:
    print("alant")
    sys.exit(0)

NON_SINGLE_MSGHK = "cs dzs dz gy ly ny sz ty zs".split()
