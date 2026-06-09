def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        opponent_history.clear()
        return "R"

    opponent_history.append(prev_play)
    n = 3 

    if len(opponent_history) > n:
        pattern = "".join(opponent_history[-(n + 1):])
        play_order[pattern] = play_order.get(pattern, 0) + 1

    last_n_moves = "".join(opponent_history[-n:])
    
    prediction = max(
        ["R", "P", "S"], 
        key=lambda move: play_order.get(last_n_moves + move, 0)
    )

    ideal_response = {"R": "P", "P": "S", "S": "R"}
    
    return ideal_response[prediction]