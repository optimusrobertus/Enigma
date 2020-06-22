alphabet = "abcdefghijklmnopqrstuvwxyz"
translatedText = []
rotors = []

class Enigma:
  def __init__(self, rotors):
    self.rotors = rotors
    
# function that makes the rotors turn
def rotorTurn(turns, rotor):
  rotor = (rotor[-turns:] + rotor)[0: 26]
  return rotor