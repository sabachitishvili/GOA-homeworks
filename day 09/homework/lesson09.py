#number 1
#შეამომწმოთ იყოფა თუ არა მომხმარებლის მიერ შემოტანილი რიცხვი 2 ზე და 4ზე ზუსტად


num1 = int(input("put number"))

print(num1 % 2 == 0 and num1 % 4 == 0)


#number 2
#გააკეთეთ 10 მაგალითი შედარების ოპერატორებზე რომლებიც არის (>, <,>=,<=,==,!=) 


num1 = int(input("put number"))
num2 = int(input("put second number"))

print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)

#number 3
#გააკეთეთ 10 მაგალითი and ოპერატორზე

num1 = int(input("put number"))
print(num1 % 5 == 0 and num1 % 10 == 0)

print(num1 / 10 == 0 and num1 * 5 == 0)

print(num1 > 5 and num1 < 10)

print(num1 <= 5 and num1 >= 10)

print(num1 != 10 and num1 == 20)

print(num1 == 10 and num1 % 15 == 0)

print(num1 >= 50 and num1 < 100)

print(num1 % 100 == 1 and num1 % 50 == 5)

print(num1 > 400 and num1 <= 1000)

print(num1 % 1000 == 10 and num1 % 10000 == 0)