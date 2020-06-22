alphabet = "abcdefghijklmnopqrstuvwxyz"
translatedText = []
rotors = []

class Enigma:
  def __init__(self, rotors):
    self.rotors = rotors
    
# function that makes the rotors turn
def rotorTurn(turns, rotor):
  rotor = (rotor[-turns:] + rotor)[0: 26]
  return 

#function that puts a letter, given by the user, through the rotors
def letterThroughRotors(inputLetter):
  if alphabet.find(inputLetter) == -1:
    return inputLetter
  #through rotors 1, 2, 3 (in that order)
  for n in enigma.rotors:
    inputLetter = n[0][alphabet.index(inputLetter)]

  #inverts alphabet
  inputLetter = alphabet[::-1][alphabet.index(inputLetter)]

  #through rotors 3, 2, 1 (in that order)
  inputLetter = alphabet[enigma.rotors[2][0].index(inputLetter)]
  inputLetter = alphabet[enigma.rotors[1][0].index(inputLetter)]
  inputLetter = alphabet[enigma.rotors[0][0].index(inputLetter)]
  #rotor 1 moves one letter
  enigma.rotors[0][0] = rotorTurn(1, rotors[0][0])
  enigma.rotors[0][1] += 1

  #If rotor 1 has made one full turn, rotor 2 moves 1/26th of a turn
  if enigma.rotors[0][1] % 26 == 0:
    enigma.rotors[0][1] = 0
    enigma.rotors[1][0] = rotorTurn(1, rotors[1][0])
    enigma.rotors[1][1] += 1
    #if rotor 2 has amde one full turn, rotor 3 moves 1/26th of a turn
    if enigma.rotors[1][1] % 26 == 0:
      enigma.rotors[1][1] = 0
      enigma.rotors[2][0] = rotorTurn(1, rotors[2][0])
      enigma.rotors[2][1] += 1
  return inputLetter 

#This function is used to set up the positions of the rotors
def rotorSettings():
  print("Please give the positions for the rotors:")
  for x in range(3):
    while True:
      print("Position rotor {}:".format(x+1))
      try:
        rotors.append([alphabet,int(input())])
        break
      except:
        print("For setting up the positions of the rotors, only numbers are allowed.") 