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
        
        ans_list = []

        #生成する
        for i in range(self.digits):

            rand_num = random.randint(0,9)

            #重複を解消する
            #重複解消は関数分けたほうがいいかも
            for j in ans_list:
                while j == rand_num:
                    print(pycolor.YELLOW + f"duplicated! >>> j:{j}, rand:{rand_num}" + pycolor.END)
                    rand_num = random.randint(0, 9)
                    print(pycolor.GREEN + f"regenerated >>> rand:{rand_num}" + pycolor.END)

            ans_list.append(rand_num)
            print(f"append:{rand_num}")            

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
    count = 0

    for i in range(100):
        ans = game.generate_ans()
        print(f"{ans}")

        for j in range(len(ans)):
            for k in range(len(ans)):
                if ans[j] == ans[k] and j != k:
                    count += 1
                    print(pycolor.RED + "ERROR : 重複しています" + pycolor.END)

        print("")
        time.sleep(0.01)

    print(f"Test Complete. False:{count}")                
