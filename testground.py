def kakeru(num):
    return num * 2

def main():
    number = [1, 5, 5]
    num_mult = map(kakeru, number)
    return num_mult

if __name__ == "__main__":
    print(list(main()))