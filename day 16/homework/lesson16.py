#1) გადაიმეორეთ ფუნქციები სოლოლეარნის გამოყენებით და გააკეთეთ თქვენი კრეატიულობით 5 ფუნქცია,
# 2 ფუნქცია რომელიც არ აბრუნებს მნიშვნელობას და 3 ფუნქცია რომელიც აბრუნებს მნიშვნელობას

import random

def randomize_list(lst):
    return random.sample(lst, len(lst))


def remove_duplicates(lst):
    return list(set(lst))


def calculate_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}


def find_maximum(lst):
    if not lst:
        return None
    return max(lst)

#2) შექმენით ფუნქცია რომელიც სიაში ლუწ ინდექსებზე მდგომ რიცხვთა ჯამს დააბრუნებს,
#შესატანი მონაცემები: [1,2,3,4,5] ---- გამოსატანი მონაცემები (შედეგი):  9

def even_num(our_list):
    list_even = ([1,2,3,4,5])
    for i in range(len(our_list)):
        if(our_list[i] % 1) == 0:
            list_even.append(our_list[i])
            return list_even



#3) შექმენით ფუნქცია რომელიც გამოითვლის კენტების და ლუწების ჯამს ცალცალკე,
#დააბრუნეთ სია სადაც იქნება ეს ჯამები ჩასმული, შესატანი მონაცემები [1,2,3,4,5] ---- გამოსატანი მონაცემები [6, 9]

def separate_odd_even_sum(numbers):
    odd_sum = 0
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return [odd_sum, even_sum]

data = [1, 2, 3, 4, 5]
result = separate_odd_even_sum(data)
print(result)


#4) შექმენით ფუნქცია რომელიც დაგიბრუნებთ სიაში მყოფ ელემენტების რაოდენობას,
#შესატანი მონაცემები: [1,2,3,4,5] ---- გამოსატანი მონაცემები (შედეგი): 5
#--------- შესატან მონაცემებში იგულისხმება ის რომ ფუნქციას გადაცეთ კონკრეტული მნიშვნელობა ----------
        
num = [1,2,3,4,5]
print(len(num))


# 5) შექმენით replace ფუნქციის კოპიო
        
def replace(num1,num2):
    result = num1 + num2
    return result

print(replace("apple" , " banana") +  " kiwi")

#6) შექმენით join ფუნქციის კოპიო, (ვიცი რომ არ იცით მაგრამ დასერჩეთ და ისწავლეთ. შემდეგ გაკვეთილზე აგიხსნით

def custom_join(delimiter, iterable):
    result = ""
    for i, item in enumerate(iterable):
        if i != 0:
            result += delimiter
        result += str(item)
    return result
