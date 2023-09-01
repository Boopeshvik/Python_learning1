player_score = {}
with open("Score.csv","r") as f:
        for line in f:
                player,score = line.split(',')
                score =int(score)
                if player in player_score:
                        player_score[player].append(score)
                else:
                        player_score[player] = [score]
for player, score_list in player_score.items():
        min_score = min(score_list)
        max_score = max(score_list)
        avg_score = sum(score_list)/len(score_list)
        print(f"{player} ==> Min: {min_score}, Max: {max_score}, Avg: {avg_score}")




