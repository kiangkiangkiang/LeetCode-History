from collections import defaultdict, deque
from copy import deepcopy
from typing import List

class Solution:
    def connect(self, row_index, col_index, current_word_pointer):
        if current_word_pointer == len(self.word):
            return True
        
        if row_index >= len(self.board) or col_index >= len(self.board[row_index]) or self.board[row_index][col_index] != self.word[current_word_pointer]
            return False
        
        if (self.connect(row_index + 1, col_index, current_word_pointer + 1) or 
            self.connect(row_index, col_index + 1, current_word_pointer + 1)):
            pass
            
        
            

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        for row_index in range(len(board)):
            for col_index in range(board[col_index]):
                if self.connect(row_index, col_index, 0):
                    return True
        return False

# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCCED"
# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "SEE"
# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCB"
board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word = "AAB"  # True
a = Solution()
print(a.exist(board, word))
