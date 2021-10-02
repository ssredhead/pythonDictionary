from tic_tac_toe import *
from copy import deepcopy

my_board = [
	["1", "2", "X"],
	["4", "5", "6"],
	["7", "8", "9"]
]

#Incorrect because new_board is now a pointer and will change the value in my_board
# new_board = my_board 

#Correct method of copying objects using deepcopy function
new_board = deepcopy(my_board)

select_space(new_board, 5, "O")
print_board(new_board) #these two will be the same
print_board(my_board)