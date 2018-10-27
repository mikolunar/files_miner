"""
Toolbox
- 
"""

import math
import os
import random
import re
import sys
from collections import defaultdict
from fileinput import filename
from pylint.test.functional.duplicate_dict_literal_key import correct_dict


#Longest word function

def longestWord(sentence):

    # sentence="this is sentence with some different items 12345678"
    words=sentence.split()
    max_len = len(max(words, key=len))
    for word in words:
        if len (word)==max_len:
            return word


def longestWords(sentence):
    
    # sentence="this is sentence with some different items 12345678"
    words=sentence.split()
    max_len = len(max(words, key=len))
    return [word for word in words if len (word)==max_len]


def wordReverse(word):
    return word[::-1]


def letterChange(sentence):
    
    words=sentence.split()
    mod_words=[]
    vowels = ('a','e','i','o','u','A','E','I','O','U')

    for word in words:
        word=word+' '
        word=word.lower()
        for letter in word:
        

            if letter!=' ':
                if letter.isalpha():
                    asci=ord(letter)
                    if asci==122:
                        new_letter='A'
                     
                    elif asci==90:
                        new_letter='A'
                    else:
                        new_letter=chr(asci+1)
                        if new_letter in vowels:
                            new_letter=new_letter.capitalize()
                else:
                    new_letter=letter
            else:
                new_letter=letter

            mod_words.append(new_letter)

    return ''.join(mod_words)


# adding numbers

def numAdding(number):
    return number*(number+1)/2


def capitalWords(sentence):
    words=sentence.split()
    modified=[]
    
    for word in words:
        char_list=list(word)
        #possible to use str.capitalize() too
        char_list[0]=char_list[0].upper()
        char_list.append(' ')
        
        modified.append(''.join(char_list))
    return ''.join(modified)


def charPatternRecognition(string):

    index=0
    valid=False


    for char in string:
        
        if char.isalpha():
            print(char)
            if string[index-1]=='+' and string[index+1]=='+':
                valid=True
            elif valid==True:
                return False
            else:
                return False
         

        index=index+1
    
    return valid


#Converts minutes to hours:minutes
def timeConverter(minutes):


    hours=int(minutes/60)
    rest_minutes=minutes%60
    return str(hours)+':'+str(rest_minutes)

#sorting characters in string
def charSorter(string):
    return ''.join(sorted(string))


#Kaprekar's constant

def kaprekars(number):
       
    def iterCount(number, counter):

        digits=[int(digit) for digit in str(number)]
            
        low_number=int(''.join(map(str, sorted(digits))))
            
        hi_number=int(''.join(map(str, sorted(digits, reverse=True))))
        if hi_number<1000:
            hi_number=hi_number*10
        product=hi_number-low_number
        print(product)
        if product!=6174:
            return iterCount(product, counter+1)
        else:
            return counter
        
    counter=1
    
            
    if number !=6174:
        return iterCount(number,counter)
    else:
        return counter
    

def recursiveCount(number):
    if number>0:
        print(number)
        recursiveCount(number-1)

    return number


def questionMarks(string):
        if len(string)>0:
            indeks1=0
            indeks2=0
            for i in range (len(string)-1):
                for j in range(i+1, len(string)):
                    if string[i].isnumeric() and string[j].isnumeric() and int(string[i])+int(string[j])==10:
                        print(string[i], string[j])
                        indeks1=i
                        indeks2=j
                        marks=string[indeks1+1:indeks2+1]
                        if marks.count('?')==3:
                            if questionMarks(string[indeks2:len(string)])==True:
                                return True
                            else:
                                return False
                        
            return False


#determine if the characters "a" and "b" are separated by exactly 3 places anyware in the string. 
def abCheck(string):
    for a in range(len(string)-1):
        if string[a]=='a':
            for b in range(a, len(string)):
                print(string[a], string[b])
                if string[a]=='a' and string[b]=='b':
                    print (string[a+1:b])
                    if len(string[a+1:b])==3:
                        return True
                    
    return False

#returns integer and floating devision a/b
def printDivision(a,b):
    if b>0:
        int_div=int(a/b)
        float_div=a/b
        print(int_div)
        print(float_div)
    else:
        print("can divide by 0")


def sqareIntegers(integer):
    for i in range (0,integer):
        print (i*i)


def isLeapYear(year):

    print(year,'%4', year%4)
    print(year,'%100',year%100)
    print (year,'%400',year%400)
    if (year%100)==0:
        if (year%400)==0:
            return True
        else:
            return False
    else:
        if year%4==0:
           return True
        else:
            return False

def printNumbers(n):
    
    lista=[]
    for i in range (1,n):
        lista.append(str(i))
    return ''.join(lista)


def sorter(nm):
    nm = input("Input n m: ").split()   
    n=int(nm[0])
    m=int(nm[1])
    print ('n=', n, ' ', 'm=',m)


    arr=[]

    for i in range(n):
        arr.append(map (int, input(str(i)+" 0<=K<=M atrributes :").rstrip().split()))
    
   
    k=int(input("K:").rstrip())

    lista=[]

    for i in range(len(arr)):
        arr[i]=list(arr[i])
    
    print (arr)
    arr.sort(key=lambda x: x[k])

    for i in range(len(arr)):
        print(*arr[i])
    
    return (k)


def miniSorter():

    x= [[8, 9, 7],
        [1, 2, 3],
        [5, 4, 3],
        [4, 5, 6]]

    # x=[4,8,7,1]
    # 
    #   
    print(x)
    
    for i in range (0,len(x[0])-1):
        print(i)
        x.sort(key=lambda z: z[i])
        print(x)
    

    return True


def iterations(limit):
    x=0
    while x<limit:
        x+=1
        yield x
    

def anyOrAll():

    numbers=input().rstrip().split()
    print(numbers)
    print(all(number!='0' for number in numbers))

    # for i in range (0,len(numbers)-1):
    #     print (numbers[i], numbers[i][::-1])
    #     print (numbers[i]==numbers[i][::-1])

    print(any(numbers[i]==numbers[i][::-1] for i in range(0, len(numbers)-1)))
    return'END'
    

def strSorter(string):

    letters=[c for c in string if c.isalpha()]
    odd_digits=[c for c in string if c.isdigit() and int(c)%2!=0]
    even_digits=[c for c in string if c.isdigit() and int(c)%2==0]


    letters.sort(key=lambda x: (not x.islower(),x))
    odd_digits.sort()
    even_digits.sort()
    final=letters+odd_digits+even_digits
    
      
    return final


def studentMarks():

    n=int(input())
    students={}
    average=0
    if 2<=int(n)<=10:
        for i in range(n):
            name, *line=input().split()
            scores=list(map(float, line))
            students[name]=scores

        print(students)
        target=input()

        if target in students:
            record =students[target]
            y=0
            for x in record:
                y=x+y

            average =y/3 
        else:
            average=0

        print("%.2f" % average)
    else:
        print("0")
    return average




def checkDict():
    return 'END'


########################################3


def file_2_list(filename):

    f=open(filename)
    lines=f.read().splitlines()

    return lines

def file_2_dict(filename):

    f=open(filename)
    lines=f.read().splitlines()
    
    
    result_dict=defaultdict()
    
    for i in range(len(lines)):
        result_dict[i]=lines[i].split()
    return result_dict

def compare_list(list1, list2):
    if len(list1)!=len(list2):
        return False

    for i in range(list1):
        if list1[i]!=list2[i]:
            return False

    return True

def compare_dict():
    return True

def checkAB(n,m):

    dict1=defaultdict(list)
    input_list=file_2_list('input01.txt')
   

    input_list.pop(0)
    list1=input_list[0:10000]

    print('Input: list1: ',len(list1))

    print(input_list[0])


    list2=input_list[10000:10100]
    print('Input: list2: ',len(list2))


    for item in range(len(list2)):
        exist=False
        for i, words in enumerate(list1):
            if list2[item] in words:
                exist=True
                dict1[words].append(str(i+1))
            
        if exist==False:
            dict1[list2[item]].append('-1')

    print('Result dict: ',len(dict1))


    correct_dict=file_2_dict('output01.txt')
    print('Correct dict: ',len(correct_dict))
    
    counter=0
    for i, word in enumerate(list2):
        if len(dict1[word])!=len(correct_dict[i]):
            counter+=1
            print(str(i),' ',word, ' ', len(dict1[word]),' -----> ',len(correct_dict[i]))  
        
    print('incorrect counter', counter)
# n, m= input().split()
# n=10000
# m=100


#filename=input()
checkAB(10000,100)