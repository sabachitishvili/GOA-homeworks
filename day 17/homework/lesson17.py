#1) შექმენით ფუნქცია, რომელშიც გააერთიანებთ იმ ფუნქციებს რაც დღეს ვისწავლეთ (lower(), upper(), capitalize(), find())

def my_function(fname,sum,gum):
  print(fname.upper() + sum.lower() + gum.capitalize())

my_function("saba","SABA","SABA")


def name(num):
    name = num.find("b")
    return name
print(name("sabasaaasa"))


#2) შექმენით ფუნქცია რომელსაც გადაეცემა list = ["name1" , "name2" , "name3"....]
#შემდეგ მომხმარებელს კითხეთ რომელი ინდექსის შეცვლა სურს და ამის მიხედვით შეცვალეთ ის კონკრეტული ინდექსი თქვენი სასურველი სტრინგით და ბოლოს შეაერთეთ join() ფუნქციის მეშვეობით 

list = ["name1" , "name2" , "name3"]
lists_ = (input("wich index do you want to change: "))

for i in lists_:
    if lists_ == 1 or 2 or 3 or 4:
        list.pop()
new_list = " ".join(list)
print(list)

#3) დეტალურად, კომენტარის სახით ახსენით split() და join() ფუნქციები,
#შეეცადეთ ახსნათ chad-ურად, წარმოიდგინეთ რომ მეგობარს უხსნით ვინც პროგრამირებაზე არაფერი იცის

#1

txt = "welcome to the jungle"

x = txt.split()

print(x)

#ოცდა მეცხრე ხაზზე შვქმენით ცვლადი სახელად txt და მივანიჭეთ მნიშვნელობა "welcome to the jungle" შემდეგ split() სპლიტ ფუნქციით დავანაწილეთ და გამოვყავით
#ერთმანეთისგან და საბოლოოდ მივიგებთ ['welcome', 'to', 'the', 'jungle'].

#2

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#ორმოცდამეორე ხაზზე შევქმენით ცვლადი სახელად "myTuple" და მივანიჭეთ მნიშვნელობა "John", "Peter", "Vicky"
#შემდეგ join ფუნქციას მივანიჭეთ "#" რომელსაც შეიყვანს join ფუნქცია "myTuple"-ში გადაუვლის მნიშვნელობებს და ჩასვავს # ყოველი მნიშვნელობის შუაშ
#ასე უნდა გამოიყურებოდეს John#Peter#Vicky