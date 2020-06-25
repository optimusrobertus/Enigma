# maak hier de hele enigma machine in python :D 

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
  
  if letter not in alfabet:
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


while True:
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
  
  zin = str(input("Voer hier de zin in die u wilt encrypten of decrypten:\n"))
  encryptzin = ""



  print("\nVoer hieronder de standen voor de rotoren A, B en C in.")

  while True:
    standA = int(input("Stand rotor A: "))
    standA -=  1
    if 0 <= standA <= 25:
      break
    else:
      print("Kies een getal tussen de 1 en 26.")

  while True:
    standB = int(input("Stand rotor B: "))
    standB -=1
    if 0<= standB <= 25:
      break
    else:
      print("Kies een getal tussen de 1 en 26.")

  while True:
    standC = int(input("Stand votor C: "))
    standC -=1
    if 0<= standC <= 25:
      break
    else:
      print("Kies alstublieft een getal tussen de 1 en 26.")
 
  for letter in zin:
    Enigma()
    encrypt(letter)

  print ("\nDe nieuwe zin: "+encryptzin)

  #start the program again
  while True:
   answer = input("\nWilt u nog een bericht encrypten of decrypten? (Ja/Nee):\n")
   if answer.lower().startswith("j"):
      print("\n")
      break
   elif answer.lower().startswith("n"):
      print("Ok, bye.")
      exit() 






