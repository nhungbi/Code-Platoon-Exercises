import random

class BoggleBoard:
  
  def __init__(self):
    self.board = """
    ----
    ----
    ----
    ----"""

  def shake(self):
    dices = ['AAEEGN', 'ELRTTY', 'AOOTTW', 'ABBJOO', 'EHRTVW', 'CIMOTU', 'DISTTY', 'EIOSST', 'DELRVY', 'ACHOPS', 'HIMNQU', 'EEINSU', 'EEGHNW', 'AFFKPS', 'HLNNRZ', 'DEILRX']
    new_board = ''
    current_die= 0
    for r in range(4):
      for c in range(4):
        letter = random.choice(dices[current_die])
        if letter == 'Q':
          letter = 'Qu'

        new_board += letter + ' '
        current_die+=1
      new_board += '\n' #new line after each row
    
    self.board = new_board

  def __str__(self):
    return self.board


new = BoggleBoard()
new.shake()
print(new)
#print(random.choice(string.ascii_uppercase)) randomly generate a capitalized letter