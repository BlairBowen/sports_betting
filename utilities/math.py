def convert_ml_to_prob(odds):
    if odds == "EVEN":
        odds = 100
    if isinstance(odds, str):
        odds = float(odds)
    if odds > 0:
        odds = (100 / (odds + 100)) * 100
    else:
        odds = abs(odds)
        odds = (odds / (odds + 100)) * 100
    return odds


def convert_ml_to_dec(odds):
    if odds == "EVEN":
        odds = 100
    if isinstance(odds, str):
        odds = float(odds)
    if odds > 0:
        odds = 1 + (odds / 100)
    else:
        odds = 1 - (100 / odds)
    return odds


def find_parlay_odds(odds=[]):
    final_odds = 1
    for odd in odds:
        final_odds *= convert_ml_to_dec(odd)
    return final_odds
