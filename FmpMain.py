from FmpPredictor import FmpPredictor

Predictor1 = FmpPredictor('Southampton', 'Swansea City')

print(Predictor1.get_predictions())

Predictor2 = FmpPredictor('Everton', 'Southampton')

print(Predictor2.get_predictions())
