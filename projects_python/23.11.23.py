
import random

#Задача 1
print("\n Задача 1 \n ")
bal = int(input("Введіть бажаний бал: "))
for i in range(1, bal+1):
    print(bal)
#Задача 2 
print("\n Задача 2 \n ")
age = int(input("Введіть свій вік: "))
if(age<18):
    print("Ви не можете отримати водійскі права")
else:
    print("Ви можете отримати")
#Задача 3
print("\n Задача 3 \n ")
a = (int(input("Введіть число: ")))
if (a>=1):
    print("Число додаткове")
elif(a==0):
    print("Це нуль")
else:
    print("Число від'ємне")
#Задача 4
print("\n Задача 4 \n ")
a = (int(input("Введіть число: ")))
print("1*a=", 1*a)
print("2*a=", 2*a)
print("3*a=", 3*a)
print("4*a=", 4*a)
print("5*a=", 5*a)
print("6*a=", 6*a)
print("7*a=", 7*a)
print("8*a=", 8*a)
print("9*a=", 9*a)
print("10*a=", 10*a)
#Задача 5
print("\n Задача 5 \n ")
for i in range (1, 100+1):
        if (i%3 != 0 and i%5 !=0):
            print(i)
#Задача 6
print("\n Задача 6 \n ")
for i in range (1, 100+1):
    if (i %10 == 0 or int((i ** 0.5))):
        print(i)
#Задача 7
print("\n Задача 7 \n ")
random_num = random.randint(1,100)
attempts = 7
current_attempsts = 0
all_attempts = []
for i in range(1,100000):
    num = int(input(f"Вгадайте число, у вас {attempts} спроб: "))
    if(num == random_num):
        attempts-=1
        current_attempsts+=1
        print(f"Ви вгадали, за {current_attempsts} спроб:")
        break
    elif(num != random_num):
        attempts-=1
        current_attempsts+=1
        if (attempts == 0 or current_attempsts == 7):
            print(f"У вас закінчились спроби, правильне число було: {random_num}")
            break
        elif (num > random_num):
            if num in all_attempts:
                print("\nВи вже вводили це число!\n")
                attempts += 1
                current_attempsts -= 1
            print("\nВи не вгадали, ваше число більше ніж загадане число \n")
            all_attempts.append(num)
        elif (num < random_num):
            if num in all_attempts:
                print("\nВи вже вводили це число!\n")
                attempts += 1
                current_attempsts -= 1
                print
            print("\nВи не вгадали, ваше число менше ніж загадане число\n")
            all_attempts.append(num)
        