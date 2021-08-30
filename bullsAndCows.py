import random

# Bulls and Cows is a number guessing game.
# Player need to guess auto-defined 4 digit numbers.
# Bull means correct num with correct position
# Cow means correct num but wrong position

def getValidInput():
    guess= str (input ("Enter your guess (4 digits): "))

    validate = False
    while validate == False:
        isnumber = False
        while isnumber == False:
            if guess.isdecimal():
                isnumber = True
            else:
                print ("Error: Enter number only.")
                guess= str (input ("Try again (4 digits): "))
        if len(guess) != 4 or guess[0] == "0":
            print ( "Error: Your guess is out of range.")
            guess= str (input ("Try again (4 digits): "))
        else:
            count = 1
            for i in range (4):
                for j in range (i+1, 4):
                    if guess[i] == guess[j]:
                        count += 1
            if count > 1:
                print ("Error: duplicated number.")
                guess= str (input ("Try again (4 digits): "))
            else:
                validate = True

    return guess

exclude = []
digit = ''
for i in range(4):
    if i == 0:
        answer = str(random.randint(1, 9))
    else:   
        answer = str(random.randint(0, 9))
    while answer in exclude:
        answer = str(random.randint(0, 9))
    digit = digit + answer
    exclude.append(answer)

answer = digit

guess= getValidInput()

correct = False
while correct == False:
    strikeCounter = 0
    ballCounter = 0
    if answer == guess:
        correct= True
        break
    for i in range (len(answer)):
        if answer[i] == guess [i]:
            strikeCounter += 1
    print (strikeCounter, "Bulls") #Correct num, correct position
    
    for i in range(len(answer)):
        if answer [i] in guess and answer[i] != guess[i]:
            ballCounter += 1
    print (ballCounter, "Cows") #Correct num, wrong position
    guess = getValidInput()

print ("Well Done!")



