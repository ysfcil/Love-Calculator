numbers = []
yourLoveRate = 0
LoverName = str(input("Your lover's name: "))

def GetNumbers(LoverName):
    numbers_ = []
    yourName = str(input("Your name: "))
    combined = yourName + LoverName
    letters_counted = []
    number_of_occur = 0
    for x in combined:
        if x not in letters_counted:
            number_of_occur = combined.count(x)
            numbers_.append(number_of_occur)
        letters_counted.append(x)
    return numbers_


numbers = GetNumbers(LoverName)

def calculate_love_rate(numbers):
    
    while True:
        numbers1 = []
        if len(numbers) > 2:
            for x in range(0, int(len(numbers)/2)):
                numbers1.append(0)
                numbers1[x] += numbers[x] + numbers[-(x+1)]
            if len(numbers) % 2 != 0:
                numbers1.append(numbers[int(len(numbers)/2) + 1]) 
            print(numbers)
        if len(numbers1) == 2:
            yourLoveRate = ''.join(str(e) for e in numbers1)
            print(numbers1)
            break
        else:
            numbers = numbers1
            continue
    return yourLoveRate

yourLoveRate = calculate_love_rate(numbers)

def Print_Love(yourLoveRate):
    yourLoveR = int(yourLoveRate)
    if yourLoveR < 25:
        print("Your love rate with {} is just %{}. But this a stupid internet test go ask them out".format(LoverName, yourLoveR))
    elif yourLoveR < 45:
         print("Your love rate with {} is just %{}. It is possible".format(LoverName, yourLoveR))
    elif yourLoveR < 50:
         print("Your love rate with {} is just %{}. You should definetly go to a date".format(LoverName, yourLoveR))
    elif yourLoveR > 50:
         print("Your love rate with {} is just %{}. They are in love".format(LoverName, yourLoveR))   

Print_Love(yourLoveRate)




    
