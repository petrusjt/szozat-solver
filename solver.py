from pprint import pprint

from submodules.argparser import ARGS
from submodules.guess_recommendation import GuessRecommendation

# TODO minden fájlra külön logika kell -> usable_words.txt nem használható
#   - átgondolni, hogy lehet-e egységesíteni
#       - maybe dzs dz sorrend? <- usable_words.txt most ilyen, jó így? - így marad, ha nem jó, módosul
recommendation = GuessRecommendation(ARGS.first_guess, ARGS.present, ARGS.not_present, ARGS.correct_regex)

pprint(recommendation.get_recommendations())
