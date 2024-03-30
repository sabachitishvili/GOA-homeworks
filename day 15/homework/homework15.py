#1
#შექმენით ფუნქცია, რომელსაც გადასცემთ თქვენ სახელს და გვარს.
#გამოიყენეთ split,indexing და დაბეჭდეთ თქვენი ინიციალები. test case: input) David Tezelashvili -> output) D.T

def name_lastname(name):
    print(name[0:1] + "." + name[5:6])

name_lastname("Saba Chitishvili")


#2
#შექმენით ფუნქცია, რომელსაც გადასცემთ სიას. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის საშუალო არითმეტიკული (ჯამი / სიგრძე)


def list(num):
    print(num + num + num + num)

list(10)
list(20)
list(40)
list(50)


#3
#შექმენით ფუნქცია, რომელსაც გადასცემთ სიტყვას და შემოწმდება არის თუ არა ის პალინდრომი (პალინდრომია სიტყვა, თუ მისი შებრუნებულიც იგივე გამოდის, მაგ: level)

def palidrom_(word):
    reversed_word = " "

    for i in range(len(word) - 1, -1, -1):
        reversed_word = reversed_word + word[i]

    print(reversed_word)

palidrom_("level")


#4
#შექმენით ფუნქცია, რომელსაც გადასცემთ სთრინგს. თქვენი დავალებაა, რომ ამ სთრინგს მოაშოროთ ყველა სფეისი - space და დაბეჭდოთ ამ სახით test case: input) "     Goal-   Oriented   Academy    " -> output) "Goal-OrientedAcademy"

str1 = "Goal-   Oriented   Academy"

str2 = " "
for i in str1:
    if i !=" ":
        str2 = str2 + i
print(str2)


#5
#შექმენით ფუნქცია, რომელსაც გადასცემთ სიას. ამ სიაში უნდა გქონდეთ როგორც დადებითი, ასევე უარყოფითი რიცხვები. თქვენი დავალებაა, რომ გამოიტანოთ უარყოფითი რიცხვების რაოდენობა და დადებითი რიცხვების ჯამი (გამოიყენეთ for ციკლი ორივეზე)

def func(numlist):
    sum = 0
    quanitity = 0

    for num in numlist:
        if num >= 0:
            sum = sum + num
        else:
            quanitity = quanitity
    print(sum,quanitity)

func([1,2,3,-1,-2,-3])