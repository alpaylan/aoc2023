
import re

def get(matrix, x, y):
    try:
        return matrix[y][x]
    except IndexError:
        return "."

def p1():
    with open("d3.input") as f:
        all_nums = []
        summ = 0
        ops = ["*","/","+","=","@","&","%","-","#","$"]
        nonops = ["0","1","2","3","4","5","6","7","8","9", "."]
        data = f.read().splitlines()
        width = len(data[0])
        height = len(data)
        matrix = [[0 for x in range(width)] for y in range(height)]
        for index, line in enumerate(data):
            for i, char in enumerate(line):
                matrix[index][i] = char

        for index, line in enumerate(data):
            summed_nums = []
            nums = re.split('\.|\*|/|\+|=|@|&|%|-|#|\$', line)
            nums = list(filter(lambda x: x != "", nums))
            pos = 0
            for num in nums:
                if num == "27":
                    print("here")
                start = line.find(num, pos)
                end = start + len(num)
                
                summed = False
                for i in range(start-1, end+1):
                    if num == "27":
                        print(i, index-1, get(matrix, i, index - 1))
                        print(i, index+1, get(matrix, i-1, index + 1))
                    if get(matrix, i, index - 1) not in nonops or get(matrix, i, index + 1) in ops:
                        summed = True
                        break
                if not summed and get(matrix, start-1, index) not in nonops or get(matrix, end, index) in ops:
                    summed = True
                if num == "27":
                    print(summed)
                if summed:
                    summed_nums.append(num)
                    all_nums.append(num)
                    summ += int(num)
        print(summ)





def p2():
    gears = {}
    with open("d3.input") as f:
        ops = ["*","/","+","=","@","&","%","-","#","$"]
        nonops = ["0","1","2","3","4","5","6","7","8","9", "."]
        data = f.read().splitlines()
        width = len(data[0])
        height = len(data)
        matrix = [[0 for x in range(width)] for y in range(height)]
        for index, line in enumerate(data):
            for i, char in enumerate(line):
                matrix[index][i] = char

        for index, line in enumerate(data):
            nums = re.split('\.|\*|/|\+|=|@|&|%|-|#|\$', line)
            nums = list(filter(lambda x: x != "", nums))
            pos = 0
            for num in nums:
                if num == "27":
                    print("here")
                start = line.find(num, pos)
                end = start + len(num)
                pos = end
                print(num)
                for i in range(start-1, end+1):
                    if get(matrix, i, index - 1) not in nonops or get(matrix, i, index + 1) in ops:
                        if get(matrix, i, index - 1) == "*":
                            if (i, index-1) not in gears.keys():
                                gears[(i, index-1)] = [num]
                            else :
                                gears[(i, index-1)].append(num)

                        if get(matrix, i, index + 1) == "*":
                            if (i, index+1) not in gears.keys():
                                gears[(i, index+1)] = [num]
                            else :
                                gears[(i, index+1)].append(num)

                if get(matrix, start-1, index) not in nonops or get(matrix, end, index) in ops:

                    if get(matrix, start-1, index) == "*":
                        if (start-1, index) not in gears.keys():
                            gears[(start-1, index)] = [num]
                        else :
                            gears[(start-1, index)].append(num)
                        
                    if get(matrix, end, index) == "*":
                        if (end, index) not in gears.keys():
                            gears[(end, index)] = [num]
                        else :
                            gears[(end, index)].append(num)
        mull = 0
        for key in gears:
            if len(gears[key]) == 2:
                mull += int(gears[key][0]) * int(gears[key][1])
        print(mull)

p1()
p2()