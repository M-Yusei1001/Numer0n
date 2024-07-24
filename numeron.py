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

class Numeron_game:
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

    def is_user_won(self, eats:int) -> bool:
        if eats == self.digits:
            return True
        else:
            return False        

class Numeron_io:

    def set_difficulty(self) -> int:
        print("難易度を選択してください：")
        print("Easy：1, Normal：2, Hard：3, 終了：0")
        difficulty = input(">")

        if difficulty.isdigit():
            while int(difficulty) < 0 or 3 < int(difficulty):
                print("正しい数を入力してください")
                difficulty = input(">")

        elif not difficulty.isdigit():
            while not difficulty.isdigit():
                print("数を入力してください")
                difficulty = input(">")

        return int(difficulty)

    def is_duplicated(num_list:list) -> bool:
        for i in range(len(num_list)):
            for j in range(len(num_list)):
                
                #重複があればTrueを返す
                if num_list[i] == num_list[j] and i != j:
                    return True
                
        return False        

    def num_input(self, digits:int) -> list:

        print(f"{digits}ケタの数を入力してください。")
        print(pycolor.CYAN + "<ルール>：重複なし" + pycolor.END)

        input_line = input(">")

        #必要なこと
        #1.入力が数字のみか判定
        #2.入力のケタ数が合っているか判定
        #3.入力に重複がないか判定

        if input_line.isdigit():
            while (len(input_line) != digits
                    or Numeron_io.is_duplicated(input_line)):
                    print(pycolor.YELLOW + "正しく入力してください" + pycolor.END)
                    input_line = input(">")

        elif not input_line.isdigit():
            while not input_line.isdigit():
                print(pycolor.YELLOW + "数を入力してください" + pycolor.END)
                input_line = input(">")            

        num_list=[]
        for num in input_line:
            num_list.append(int(num))

        return num_list    
                
                

if __name__ == "__main__":
    game = Numeron_game(2)
    game_io = Numeron_io

    numlist = game_io.num_input(game_io, 3)

    print(numlist)

    for num in numlist:
        print(type(num))

