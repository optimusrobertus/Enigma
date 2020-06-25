# maak hier de hele enigma machine in python :D yoyoyo
alfabet = "abcdefghijklmnopqrstuvwxyz"
RotorA =  "vwxyzabcdefghijklmnopqrstu"
RotorB =  "qrstuvwxyzabcdefghijklmnop"
RotorC =  "lmnopqrstuvwxyzabcdefghijk"
#reflector
reflector = alfabet[::-1]

A=-1
B=0 
C=0
a=0
b=0
c=0

zin = str(input("Welke zin: "))
encryptzin = ""

standA = int(input("welke stand voor rotor A: "))
standA -=1

standB = int(input("welke stand voor rotor B: "))
standB -=1

standC = int(input("welke stand voor rotor C: "))
standC -=1

def encrypt(letter):
  global encryptzin
  global standA
  global standB
  global standC
  global A
  global B
  global C
  global a
  global b
  global c
  

  
  
  elif letter not in alfabet:
    encryptzin = encryptzin + letter

  else:
    indexA = alfabet.index(letter)+standA+A
    testA = indexA//26
    a = testA*26
    letterdoorA = RotorA[alfabet.index(letter)+standA+A-a]

    indexB = alfabet.index(letterdoorA)+standB+B
    testB = indexB//26
    b = testB*26
    letterdoorB = RotorB[alfabet.index(letterdoorA)+standB+B-b]

    indexC = alfabet.index(letterdoorB)+standC+C
    testC = indexC//26
    c = testC*26
    letterdoorC = RotorC[alfabet.index(letterdoorB)+standC+C-c]

    letterdoorR = reflector[alfabet.index(letterdoorC)]

    indexC = alfabet.index(letterdoorR)+standC
    testC = indexC//26
    c = testC*26
    letterdoorC = RotorC[alfabet.index(letterdoorR)-c]

    indexB = alfabet.index(letterdoorC)+standB
    testB = indexB//26
    b = testB*26
    letterdoorB = RotorB[alfabet.index(letterdoorC)-b]

    indexA = alfabet.index(letterdoorB)+standA
    testA = indexA//26
    a = testA*26
    letterdoorA = RotorA[alfabet.index(letterdoorB)-a]

    encryptzin += str(letterdoorA)



def Enigma():
  global A
  global B
  global C
  A = A+1
  B = A//26
  C = B//26





for letter in zin:
  Enigma()
  encrypt(letter)


print ("De nieuwe zin: "+encryptzin)

