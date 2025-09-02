import numpy as np
import os
import time

NUM_COUNT = 100_000_000
MAX_NUM = 99_999
FILE_NAME = "numbers.txt"
CHUNK_SIZE = 1_000_000

def generate_with_numpy():
    print(f"Generating {NUM_COUNT:,} random numbers using NumPy...")
    start_time = time.time()
    with open(FILE_NAME, "w") as f:
        f.write("[")
        for i in range(0, NUM_COUNT, CHUNK_SIZE):
            current_chunk_size = min(CHUNK_SIZE, NUM_COUNT - i)
            numbers = np.random.randint(0, MAX_NUM + 1, size=current_chunk_size, dtype=np.int32)
            chunk_str = np.array2string(numbers, separator=', ')[1:-1].replace('\n', '')
          
            if i == 0:
                f.write(chunk_str)
            else:
                f.write(f", {chunk_str}")

        f.write("]")
    end_time = time.time()
    file_size_mb = os.path.getsize(FILE_NAME) / (1024 * 1024)
    print(f"Successfully created '{FILE_NAME}'.")
    print(f"File size: {file_size_mb:.2f} MB")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    generate_with_numpy()
