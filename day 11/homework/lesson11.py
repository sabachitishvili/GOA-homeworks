#davaleba 1
#შექმენით სია სადაც გადასცემთ 10 ინტეგერს, შემდეგ გადაუარეთ ამ სიას და თითოეული მათგანი გაამრავლეთ/გაყეთ/დაუმატეთ/გამოაკელით ერთმანეთს. (ექსპერიმენტებიც გააკეთეთ)

list = [0,1,2,3,4,5,6,7,8,9,10,11,12]

for i in list:
    print(list[i]*2)

for i in list:
    print(list[i]/2)

for i in list:
    print(list[i]+2)

for i in list:
    print(list[i]-2)    

#davaleba 2
#შექმენით სია, სადაც გამოიტანთ სათითაოდ მნიშვნელობებს და ასევე ჩაანაცვლებთ სხვა მნიშვნელობებით.

list = ['dog', 'cat', 'hamster']

list[0] ="lion"
list[1] = "tiger"
list[2] = "crocodile"

print(list)
for x in list:
    print(x)


#davaleba 3
#შექმენით სია და მომხმარებელს აარჩევინეთ სასურველი მნიშვნელობა

list = ["orange","apple","lime"]

second_list = int(input("enter a number:"))

print(list[second_list])

