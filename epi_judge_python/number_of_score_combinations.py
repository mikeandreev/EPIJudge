from test_framework import generic_test

# DONE

def num_combinations_for_final_score(final_score, individual_play_scores):
    Ns = len(individual_play_scores)
    scores = [[1]*Ns] + [ [0]*Ns for _ in range(1, final_score+1)] # DP cache
    for i in range(1, final_score+1):
        for k, s in enumerate(individual_play_scores):
            j = i-s
            if j >= 0: scores[i][k] += scores[j][k]
            if k > 0: scores[i][k] += scores[i][k-1]
    return scores[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
