from pprint import pprint

from submodules.argparser import ARGS
from submodules.guess_recommendation import GuessRecommendation

recommendation = GuessRecommendation(ARGS.first_guess, ARGS.present, ARGS.not_present, ARGS.correct_regex)

pprint(recommendation.get_recommendations())
