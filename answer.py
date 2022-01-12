#1 - answer 
def add(number, another_number):
    return number + another_number

#2 - answer
import random
def main_function():
    first_number = get_random(0, 99)
    result = add(first_number)
    print(result)
def get_random(start, end):
    random_number = random.randint(start, end)
    return random_number
def add(number):
    return number 
main_function()
#3 - answer
times_4 = ("today, I am outstanding in every way")
print(times_4*4)
#4 - answer
times_200 = ("I become what I think about most of the time")
print(times_200*200)
#5 - answer
name = input("Enter your name: ")
print("you look good today", name)
#6 - answer
alphabet = "abcdefghifklmnopqrstuvwxyz"
alphabet_length = len(alphabet)
print(alphabet_length)
#7 - answer
alphabet = "abcdefghijklmnopqrstuvwxyz"
position_of_letter_j = alphabet.index("j")
print(position_of_letter_j + 1)
#8 - answer
from array import array 
test_scores = array("i", [96, 80, 92, 60, 91, 37, 87 ])
for score in test_scores:
    print(score)
#9 - anwer
test_scores.append(56)

#10 -answer
length = len(test_scores)
print("length of the array(number of scores):", length)
#11 -answer
people_in_computer_class = ["Howard", "Barbie", "Rain", "Yujing", "Angelina", "Arsalon"]
print(people_in_computer_class)
#12 -answer
people_in_computer_class.remove("Arsalon")
print(people_in_computer_class)
#13 -answer
people_in_computer_class.sort()
print(people_in_computer_class)
#14 -answer
exam_scores = dict( Barbie=[96, 95,99], Arsalon=[99, 100, 99], Howard=[98, 96, 97])
print(exam_scores)
#15- answer
Arsalon_score = exam_scores.get("Arsalon")
print("Arsalon's score is", Arsalon_score)