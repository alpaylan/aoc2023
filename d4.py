
def p1():
    with open("d4.input") as f:
        lines = f.read().splitlines()
        score = 0
        for line in lines:
            p2 = line.find(":")
            winners = list(filter(lambda s: s != "", line[p2+2:].split("|")[0].strip().split(" ")))
            my_nums = list(filter(lambda s: s != "", line[p2+2:].split("|")[1].strip().split(" ")))
            my_winner_nums = set(my_nums).intersection(winners)
            print(my_winner_nums)
            if len(my_winner_nums) == 0:
                score += 0
            elif len(my_winner_nums) == 1:
                score += 1
            else:
                score += 2 ** (len(my_winner_nums) - 1)

    print(score)

def p2():
    with open("d4.input") as f:
        lines = f.read().splitlines()
        score = 0
        cards = { i : 1 for i in range(1, len(lines) + 1) }
        for index, line in enumerate(lines):
            p1 = line.find(" ")
            p2 = line.find(":")
            id = int(line[p1+1:p2].strip())
            winners = list(filter(lambda s: s != "", line[p2+2:].split("|")[0].strip().split(" ")))
            my_nums = list(filter(lambda s: s != "", line[p2+2:].split("|")[1].strip().split(" ")))
            my_winner_nums = set(my_nums).intersection(winners)
            matches = len(my_winner_nums)
            print(matches, cards[id], matches * cards[id])
            score += matches * cards[id]
            for i in range(1, matches + 1):
                cards[id + i] += cards[id]
    print(sum(cards.values()))

if __name__ == "__main__":
    p2()