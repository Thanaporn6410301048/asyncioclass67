import time
import asyncio

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24
move_pairs = 30

async def game(x):
    board_start_time = time.perf_counter()

    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f'board-{x+1} {i+1} judit make move')
        await asyncio.sleep(opponent_compute_time)
        print(f'board-{x+1} {i+1} opponent make move')
    print(f'board-{x+1} >>>>>>>>>>>> finish move in {time.perf_counter() - board_start_time} seconds')
    return round(time.perf_counter() - board_start_time)


async def main():
    tasks = []
    for i in range (opponents):
        tasks.append(asyncio.create_task(game(i)))
    await asyncio.gather(*tasks)
    print(f'board exhibit finish in {time.perf_counter() - start_game} seconds')

if __name__ == "__main__":
    start_game = time.perf_counter() ## start time
    asyncio.run(main())  # main function
    print(f'finished in {time.perf_counter() - start_game} seconds')