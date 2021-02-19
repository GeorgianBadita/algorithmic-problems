def tournamentWinner(competitions, results):

    scores = {}

    for i in range(len(results)):
        winner = competitions[i][0] if results[i] == 1 else competitions[i][1]
        current_score = scores.get(winner, 0)
        scores[winner] = current_score + 3

    max_score = max(scores.values())
    for key, value in scores.items():
        if value == max_score:
            return key
