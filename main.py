import numeron as nr

def main():
    #Numeron_ioインスタンスの生成
    game_io = nr.Numeron_io()

    #難易度選択
    difficulty = game_io.set_difficulty()

    #Numeron_gameインスタンスの生成、難易度初期化
    game = nr.Numeron_game(difficulty)

    if difficulty == 0:
        print("\n<<<ゲームを終了します。>>>\n")
        return
    else:
        print("\n<<<ゲームを開始します！>>>\n")

    #回答リスト生成
    ans_list = game.generate_ans()

    count = 1
    print(f"{count}回目：")
    num_list = game_io.num_input(game.digits)

    #メインループ部
    while not game.is_user_won(eats = game.count_eats(num_list, ans_list)):  
        eats = game.count_eats(num_list, ans_list)
        bites = game.count_bites(num_list, ans_list)

        print(f"{eats}-Eats, {bites}-Bites!")
        print("")

        count += 1
        print(f"{count}回目：")
        num_list = game_io.num_input(game.digits)

    #終了時表示
    print(nr.pycolor.GREEN + f"\n<<<YOU WON in {count} time(s)!>>>" + nr.pycolor.END)
    print(f"The answer was -> {game.jointed_ans(ans_list)}")

if __name__ == "__main__":
    main()