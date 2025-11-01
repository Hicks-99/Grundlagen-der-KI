visited_nodes = 0

class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_tree):
        self.children.append(child_tree)
        
    def is_leaf(self):
        return len(self.children) == 0
    
    def get_value(self):
        return self.value
    
class TicTacToe:
    def __init__(self, board):
        self.board = board or [' ' for _ in range(9)]
        
    def move(self, position, player):
        new_board = self.board[:]
        new_board[position] = player
        return TicTacToe(new_board)
    
    def free_positions(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def is_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(self.board[i] == player for i in combo) for combo in winning_combinations)
         

def minimax(position, is_maximizing_player):
    global visited_nodes
    visited_nodes += 1
    if position.is_leaf():
        return position.get_value()

    if is_maximizing_player:
        max_eval = float('-inf')
        for child in position.children:
            evaluation = minimax(child, False)
            max_eval = max(max_eval, evaluation)
        return max_eval
    else:
        min_eval = float('inf')
        for child in position.children:
            evaluation = minimax(child, True)
            min_eval = min(min_eval, evaluation)
        return min_eval
    
    
def build_game_tree(tic_tac_toe, current_player):
    if tic_tac_toe.is_winner('X'):
        return Tree(1)  # X wins
    elif tic_tac_toe.is_winner('O'):
        return Tree(-1)  # O wins
    elif not tic_tac_toe.free_positions():
        return Tree(0)  # Draw

    tree = Tree(None)
    for position in tic_tac_toe.free_positions():
        next_player = 'O' if current_player == 'X' else 'X'
        child_board = tic_tac_toe.move(position, current_player)
        child_tree = build_game_tree(child_board, next_player)
        tree.add_child(child_tree)
    
    return tree

if __name__ == "__main__":
    initial_board = TicTacToe(None)
    game_tree = build_game_tree(initial_board, 'X')
    best_value = minimax(game_tree, True)
    print("Best value for X:", best_value)
    print("Visited nodes:", visited_nodes)
    visited_nodes = 0