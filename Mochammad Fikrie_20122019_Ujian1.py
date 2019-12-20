# # It must start with a hashtag (#).
# # • All words must have their first letter capitalized.
# # • If the final result is longer than 140 chars it must return False.
# # • If the input or the result is an empty string it must return False.

# # Hashtag(" Hello there how are you doing") //would return "#HelloThereHowAreYouDoing"
# # Hashtag(" Hello World " )//would return "#HelloWorld"
# # Hashtag("")// would return False

# def Hashtag(string):
#     x="#"
#     n=True
#     c=string.split(" ")
#     d=[]
    
#     if len(string)>140 or len(string)==0:
#         n=False
#         print(n)
#     elif len(string)>0:
#         for item in c[0::1]:
#             g=item.capitalize()
#             d.append(g)
#         z=(''.join(d))
#         print(x+z)


# Hashtag("Hello there how are you doing")
# Hashtag(" Hello World " )
# Hashtag("")

# Write a function that accepts a list of 10 integers (between 0 and 9), that returns a string
# of those numbers in the form of a phone number (10 points).

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])//would return "(123) 456-7890"

# def create_phone_number(num):
#     length=10
#     temp=[]
#     for item in num:
#         item=str(item)
#         temp.append(item)

#     if len(num)>length:
#         print(False)
#     elif len(num)<=length:
#         a="".join(temp[0:3])
#         b="".join(temp[3:6])
#         c="".join(temp[6:9])
#         d="".join(temp[-1])
#         print("({}) {}-{}{}".format(a,b,c,d))


# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0,])

# You are given a list of integers. Your task is to sort odd numbers within the list in ascending
# order, and even numbers in descending order but keep all the odds or the evens number in
# the same index group (35 Points).
# Note that zero is an even number. If you have an empty list, you need to return it.

# Sort_odd_even([5, 3, 2, 8, 1, 4]) // would return [1, 3, 8, 4, 5, 2]
# odd numbers ascending: [1, 3, 5, ] ( Odds number in the index 0, 1, and 4)
# even numbers descending: [ 8, 4, 2] (Evens number in the index 2,3, and 5)

# def Sort_odd_even(num):
#     tempeven=[]
#     poseven=[]
#     tempodd=[]
#     posodd=[]
#     newlist=[]
#     if len(num)==0:
#         print(False)
#     if len(num)>0:
#         for n,item in enumerate (num):
#             if evenchecker(item):
#                 tempeven.append(item)
#                 poseven.append(n)
#                 newlist.insert(n,item)
#             else:
#                 tempodd.append(item)
#                 posodd.append(n)
#                 newlist.insert(n,item)

    
    

#     print(b)
#     print(c)


                
# def shorting(b):
    

# def evenchecker(a):
#     if a%2==0:
#         return True
# def oddchecker(b):
#     if b%2!=0:
#         return True

# Sort_odd_even([5,3,2,8,1,4])


x = ''
y = 10
num = y//2
num1 = 1
for inc in range(y,0,-2):
    for inc1 in range(0,num):
        x += '_  '   
    for inc2 in range(0,num1):
        x += '#  '
    for inc3 in range(num+1,y,):
        x += '_ '      
    x += "\n"
    num1 += 2
    num -=1
print (x)
    
#     #ngeprint segitiga
#     z = ''
#     for num, i in zip(numbers, range(len(numbers))) :
#         for j in range(n-i) :
#             z += '  '
#         for k in range() :
#             #ljust berfungsi kayak padding, nambahin spasi di sebelah kanan huruf (jumlahnya sampai 4)
#             z += str(k).ljust(4, '*')
#         z += '\n' 
#     print(z)

#     sum_row = ''
    
#     for num in numbers[-1]:
#         if num == numbers[-1][-1]:
#             sum_row += str(num)
#         else:    
#             sum_row += str(num)
#             sum_row += ' + '
#     sum_row += ' = {}'.format(sum(numbers[-1]))       
    
#     if sum(numbers[-1]) == 1:
#         print(1)
#     else:
#         print(sum_row)    





# # rowSumOddNumbers(1)
# rowSumOddNumbers(2)
# # rowSumOddNumbers(10)

