import random
import time

random.seed(time.time())

class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'

class Numeron:
    def __init__(self, mode:int) -> None:
        #Easy:1, Normal:2, Hard:3
        self.mode = mode

        #桁数の決定
        if self.mode == 1: #Easy
            self.digits = 2

        elif self.mode == 2: #Normal
            self.digits = 3

        elif self.mode == 3: #Hard
            self.digits = 4

    def generate_ans(self) -> list:
        
        ans_list = random.sample(range(0,10), self.digits)               

        return ans_list           

    def jointed_ans(self, ans_list:list) -> int:
        ans = "".join(map(str, ans_list))

        return int(ans)

    def count_eats(self, num_list:list, ans_list:list) -> int:
        eats = 0

        for i in range(self.digits):
            if num_list[i] == ans_list[i]:
                eats += 1

        return eats

    def count_bites(self, num_list:list, ans_list:list) -> int:
        bites = 0

        for i in range(self.digits):
            for j in range(self.digits):

                if (i != j 
                    and num_list[i] == ans_list[j]
                    and num_list[i] != ans_list[i]
                    ):

                    bites += 1

        return bites        



if __name__ == "__main__":
    game = Numeron(2)

