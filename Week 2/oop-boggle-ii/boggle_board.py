# You should re-use and modify your old BoggleBoard class to support the new requirements
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
            dice_index_available = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            new_board = []
            for r in range(4):
                  new_row = []
                  for c in range(4):
                        current_die = random.choice(dice_index_available)
                        dice_index_available.remove(current_die) #so don't repreat die
                        letter = random.choice(dices[current_die])
                        if letter == 'Q':
                              letter = 'Qu'
                  
                        new_row.append(letter)
                  new_board.append(new_row) 
            
            self.board = new_board
      
      def words_on_board(self):
            #look at the top row, check all direction of each cell
            words = set()
            for col in range(4):
                  #across
                  word = ''
                   #down
                  word_down = ''
                  for i in range(4):
                        word += self.board[col][i] #row stay same, col change
                        word_down += self.board[i][col] #col stay same, row change
                  words.update({word, word[::-1]}) #reverse: start from bottom
                  words.update({word_down, word_down[::-1]})

            #diagonal
            word1 = ''
            word2 = ''
            for i in range(4):
                  word1 += self.board[i][i] #diagonal so each row with column is the same eg, 00, 11, 22, 33
                  word2 += self.board[-(i+1)][-(i+1)] #other end, -1-1,-2-2,
            words.update({word1,word2, word1[::-1], word2[::-1]})

            self.words_on_board = words

      def include_word(self, word):
            if word.islower():
                  word.upper() #turn into upper to check 
                  
            if word in self.words_on_board:
                  return True
            return False
      
test1 = BoggleBoard()
test1.shake()
print(test1.board)
test1.words_on_board()
print(test1.words_on_board)
print(test1.include_word('pear')) # False
print(test1.include_word('HFZD'))