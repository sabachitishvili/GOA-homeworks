#DAVALEBA 1
#მომხმარებელს შემოატანინეთ სახელი, გვარი, ასაკი და საცხოვრებელი ადგილი. თითოეული მათგანი append-ის გამოყენებით დაამატეთ სიაში.

name = input("enter your name")
lastname = input("enter your lastname")
age = input("enter your age")
adress = input("enter your living adress")


list =[]

list.append(name)
list.append(lastname)
list.append(age)
list.append(adress)

print(list)
#1: სახელი, გვარი
print(name)
print(lastname)
#2: გვარი, ასაკი
print(lastname)
print(age)
#3: სახელი, გვარი, ასაკი
print(name)
print(lastname)
print(age)
#4: გვარი, ასაკი, საცხოვრებელი ადგილი
print(lastname)
print(age)
print(adress)


#DAVALEBA 2
#მომხმარებელს შემოატანინეთ უარყოფითი რიცხვი. ამ რიცხვიდან 0-მდე არსებული ყველა უარყოფითი რიცხვი დაამატეთ სიაში და საბოლოოდ დაბეჭდეთ სია.

num = input("enter negative number")

list = []

list.append(num)

print(list)


#DAVALEBA 3
#ცვლადში შეინახეთ თქვენი სახელი და გვარი. Slicing-ის გამოყენებით ჯერ სახელი, შემდეგ კი გვარი დაბეჭდეთ.

name_lastname = "saba chitishvili"

print(name_lastname[0:4])
print(name_lastname[5:16])


#DAVALEBA 4
#სიაში შეინახეთ მინიმუმ 5 საყვარელი ფილმი. გამოიყენეთ Slicing და  დაბეჭდეთ რამდენიმე კომბინაციით. Bonus (არ არის აუცილებელი): იგივე კომბინაციები დაბეჭდეთ უარყოფითი ინდექსების გამოყენებით.


list = ["fightclub","intersteral","joker","wolf of wallstreet","batman"]

print(list[1:3])
print(list[1:4])
print(list[2:4])
print(list[-0:-2])
print(list[-0:-4])
print(list[-6:-1])


#DAVALEBA 5
#მომხმარებელს შემოატანინეთ აკადემიის სახელი. თუ ის "G"-თი იწყება, დაუპრინტეთ რომ გოა არის საუკეთესო არჩევანი. სხვა შემთხვევაში დაუპრინტეთ, რომ არასწორი გადაწყვეტილება მიიღო.


academy_name = input("enter best academy:")

if academy_name[0] == "G" or academy_name[0] == "g":
    print("goa is the best")

else:
    print("wrong answer")