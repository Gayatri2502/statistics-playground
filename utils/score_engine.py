def calculate_score(user_answers, scenarios):

    score = 0

    for i, answer in enumerate(user_answers):

        if answer == scenarios[i]["answer"]:
            score += 1

    return score