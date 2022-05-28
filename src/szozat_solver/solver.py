from pprint import pprint

from src.szozat_solver.submodules import ARGS
from src.szozat_solver.submodules.guess_recommendation import GuessRecommendation

recommendation = GuessRecommendation(ARGS.first_guess, ARGS.present, ARGS.not_present, ARGS.correct_regex)

pprint(recommendation.get_recommendations())
