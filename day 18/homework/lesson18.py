#მომხმარებელს შემოატანინეთ სახელი. თქვენი დავალებაა, რომ შეადაროთ სახელი მის lowercase ვარიანტთან == ოპერატორის გამოყენებით.

# def func(index):
#     index = (input("enter name :"))
#     for i in index:
#         index == index.lower()
#     return index

# print(func)

#მომხმარებელს შემოატანინეთ სიტყვა. for ციკლის გამოყენებით შეამოწმეთ მისი თითოეული ასო და თუ რომელიმე იქნება lowercase, მაშინ მომხმარებელს შემოატანინეთ სიტყვა თავიდან.
#ასევე დაბეჭდეთ თუ რამდენჯერ მოუწია მომხმარებელს სიტყვის შემოტანა - counter.

# index = input("enter name in uppercase : ")
# for i in (index):
#     if index != index.upper:
#         print("welldone")

#     elif index.lower == index:
#         print("try again")

#მომხმარებელს შემოატანინეთ სიტყვა. თქვენი დავალებაა, რომ ლუწ ინდექსებზე მყოფი ასოები გარდაქმნათ uppercase-ად,
# ხოლო კენტ ინდექსებზე მყოფები lowecase-ად, საბოლოოდ კი დაბეჭდოთ შედეგი.

# index = input("enter word")
# for i in range(0,2):
    

#ცვლადში შეინახეთ თქვენი სახელი. თუ მისი სიგრძე აღემატება ხუთს,
# გარდაქმენით მთლიანი სიტყვა uppercase-ად, სხვა შემთხვევაში კი lowecase-ად. საბოლოოდ კი დაბეჭდეთ გარდაქმნილი სახელი.

#სიაში შეინახეთ თქვენი სახელი და გვარი. capitalize მეთოდის გამოყენებით მასივის ყველა ელემენტზე მოახდინეთ მუშაობა და ბოლოს დაბეჭდეთ უკვე შეცვლილი სია.

list ="saba chitishvili"

x = list.capitalize()

print(x)

#მომხმარებელს შემოატანინეთ სახელი, შემდეგ კი გვარი. შეინახეთ ისინი სიაში და წინა დავალების მსგავსად იმუშავეთ ყველა ელემენტზე capitalize მეთოდით. თქვენი დავალებაა,
#რომ გამოიტანოთ მომხმარებლის ინიციალები სთრინგის სახით. test case: input) "Data", "Tezelashvili" -> output: "D.T"

x = input("enter your name: ")
i = input("enter your lastname: ")

list = [x,i]

index = x.capitalize()
list(x[0:1])

index = i.capitalize()
list(x[0:1])

print(index)

