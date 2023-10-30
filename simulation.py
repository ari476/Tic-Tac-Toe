from gui import TicTacToeGUI

def simulate_games(num_simulations):
    ai_wins = 0
    random_wins = 0
    ties = 0

    for _ in range(num_simulations):
        game_instance = TicTacToeGUI()
        winner = game_instance.simulate_single_game()

        if winner == "AI":
            ai_wins += 1
        elif winner == "Player X":
            random_wins += 1
        else:
            ties += 1

    print(f"AI wins: {ai_wins}")
    print(f"Random wins: {random_wins}")
    print(f"Ties: {ties}")