
def p1():
    with open("d2.input") as f:
        summ = 0
        data = f.read().splitlines()
        for line in data:
            p1 = line.find(":")
            id = line[5:p1]
            games = list(map(lambda s: s.strip(), line[p1+1:].split(";")))
            valid_games = []
            for game in games:
                sacks = list(map(lambda s: s.strip(), game.split(",")))
                sack_dict = {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                }
                for sack in sacks:
                    [count, name] = sack.split(" ")
                    sack_dict[name] = int(count)
                print(id, sack_dict)
                if sack_dict["red"] <= 12 and sack_dict["green"] <= 13 and sack_dict["blue"] <= 14:
                    valid_games.append(id)
            if len(valid_games) == len(games):
                print("Valid games for {}: {}".format(id, valid_games))
                summ += int(id)
        print(summ)


def p2():
    with open("d2.input") as f:
        summ = 0
        data = f.read().splitlines()
        for line in data:
            p1 = line.find(":")
            id = line[5:p1]
            games = list(map(lambda s: s.strip(), line[p1+1:].split(";")))
            sack_dict = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for game in games:
                sacks = list(map(lambda s: s.strip(), game.split(",")))
                for sack in sacks:
                    [count, name] = sack.split(" ")
                    if sack_dict[name] < int(count):
                        sack_dict[name] = int(count)
            summ += sack_dict["red"] * sack_dict["green"] * sack_dict["blue"]
        print(summ)

p2()