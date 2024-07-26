import time
import asyncio

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 3
move_pairs = 30

def game(x):
    board_start_time = time.perf_counter()

    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f'board-{x+1} {i+1} judit make move')
        time.sleep(opponent_compute_time)
        print(f'board-{x+1} {i+1} opponent make move')
    print(f'board-{x+1} >>>>>> finish move in {time.perf_counter() - board_start_time} seconds')
    return round(time.perf_counter() - board_start_time)

if __name__ == "__main__":
    start_game = time.perf_counter() ## start time
    board_time = 0
    for board in range(opponents):
        board_time+= game(board)

    print(f'board exhibition finish in {board_time} seconds')
    print(f'finished in {round(time.perf_counter() - start_game)} seconds')