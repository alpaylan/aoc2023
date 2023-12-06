

def p1():
    with open("d6.input") as f:
        lines = f.read().splitlines()
        faketimes =  [7,15,30]
        fakedistances = [9, 40, 200]

        times = [40829166] 
        distances = [277133813491063]


        mull = 1
        for index, time in enumerate(times):
            count = 0
            for i in range(time):
                if (i * (time - i) > distances[index]):
                    count += 1
                # print (i * (time - i) > fakedistances[index])
            print(count)
            mull *= count
        print(mull)

       

def p2():
    with open("d6.input") as f:
        time = 40829166
        distance = 277133813491063
        top = int(distance ** 0.5)
        bot = 0
        mid = 0
        while True:
            mid = (top + bot) // 2
            if top == mid or bot == mid:
                break

            if mid * (time - mid) > distance:
                top = mid
            elif mid * (time - mid) < distance:
                bot = mid
            
        print(bot, mid, top)
        bot = int(distance ** 0.5)
        top = time
        mid = 0

        while True:
            mid = (top + bot) // 2
            if top == mid or bot == mid:
                break

            if mid * (time - mid) > distance:
                top = mid
            elif mid * (time - mid) < distance:
                bot = mid

        print(bot, mid, top)


       
      

if __name__ == "__main__":
    p1()
    