import random

def get_attacking_pairs(board):
    # Count the number of attacking pairs of queens on the board
    n = len(board)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                count += 1
    return count

def print_solution(board):
    # Print the board as a chessboard with queens represented by 'Q'
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()

def hill_climbing(initial_state):
    board = initial_state
    score = get_attacking_pairs(board)
    print(f"Heuristic value for initial state: {score}")

    while True:
        neighbors = []
        for i in range(8):
            for j in range(8):
                if board[i] != j:
                    neighbor = list(board)
                    neighbor[i] = j
                    neighbors.append(neighbor)

        best_neighbor = board
        best_score = score
        for neighbor in neighbors:
            neighbor_score = get_attacking_pairs(neighbor)
            if neighbor_score < best_score:
                best_neighbor = neighbor
                best_score = neighbor_score

        if best_score >= score:
            print(f"Final heuristic value: {score}")
            return board

        board = best_neighbor
        score = best_score
        print(f"Heuristic value: {score}")

# Generate a random initial state and run the hill climbing algorithm from it
initial_state = [random.randint(0, 7) for _ in range(8)]
print(f"Initial State : {initial_state}")
print_solution(initial_state)
print("\n")

solution = hill_climbing(initial_state)

print(f"\nSolution : {solution}")
print_solution(solution)