import time
import random

random.seed(time.time())

def main():
    for i in range(5):
        num = random.randint(0,9)
        print(f"{i+1}回目:{num}")

if __name__ == "__main__":
    main()