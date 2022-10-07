"""
print(emojize(":thumbs_up:"))
print(emojize(":thumbs_down:"))
"""



import random
number=(random.randint(1,100))
from emoji import emojize

counter=0
while True:
    print(emojize("Guess the number	:red_question_mark:"))
    guessed_number=int(input(""))
    if guessed_number>number:
        print(emojize(":down_arrow:"))
        counter=counter+1
    elif guessed_number<number:
        print(emojize(":up_arrow:"))
        counter=counter+1
    elif guessed_number==number:
        print(emojize("Good Job :thumbs_up:"))
        print("you tried",counter,"times")
        if counter== 1:
            print(emojize(":one_o’clock:")
        if counter == 2:
            print(emojize(":two_o’clock:")
        if counter == 3:
            print(emojize(":three_o’clock:")
        if counter == 4:
            print(emojize(":four_o’clock:")
        if counter == 5:
            print(emojize(":five_o’clock:")
        if counter == 6:
            print(emojize(":six_o’clock:")
        if counter == 7:
            print(emojize(":seven_o’clock:")
        if counter == 8:
            print(emojize(":eight_o’clock:")
        if counter == 9:
            print(emojize(":nine_o’clock:")
        if counter == 10:
            print(emojize(":ten_o’clock:")
        if counter == 11:
            print(emojize(":eleven_o’clock:")
        if counter == 12:
            print(emojize(":twelve_o’clock:")
        break

































































