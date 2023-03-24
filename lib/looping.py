#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    int_list = [int_list * int_list for int_list in int_list]
    return int_list
    
square_integers([1,2,3,4,5])

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            continue
        elif num % 3 == 0:
            print("Fizz")
            continue
        elif num % 5 == 0:
            print("Buzz")
            continue
        else:
            print(num)

fizzbuzz()    

#List Comprehension:
#player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
#inch_heights = [height * 7920 for height in player_heights]
#print(inch_heights)