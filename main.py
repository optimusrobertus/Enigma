# maak hier de hele enigma machine in python :D yoyoyo
alfabet = "abcdefghijklmnopqrstuvwxyz"
RotorA = "vwxyzabcdefghijklmnopqrstu"
RotorB = "qrstuvwxyzabcdefghijklmnop"
RotorC = "lmnopqrstuvwxyzabcdefghijk"

zin = str(input("Welke zin "))


def encrypt(letter):
    newletter = RotorA[alfabet.index(letter)]
    print(newletter)


# alfabet.index(letter)
# print(alfabet.index(letter))

# alfabet[1]
for index, letter in enumerate(zin):
    # if de output is niet index is iets en letter is een spatie dan for letter in zin encrypt(letter)
    print(index, letter)

for letter in zin:
    encrypt(letter)

# standB += standA//25
# standC += standB//25
