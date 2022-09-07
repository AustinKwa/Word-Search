#  File: WordSearch.py

#  Description: Finds listed key words in a 2-D array of letters.

#  Student Name: Austin Kwa

#  Student UT EID: ak38754

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E 

#  Unique Number: 51125

#  Date Created: 1/27/2022

#  Date Last Modified: 1/27/2022

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    dimension = sys.stdin.readline()
    dimension = dimension.strip()
    dimension = int(dimension)
    sys.stdin.readline()

    grid = []
    for i in range(dimension):
        row = sys.stdin.readline()
        row = row.strip()
        grid_row = row.split(' ')
        grid.append(grid_row)
    sys.stdin.readline()

    num_words = sys.stdin.readline()
    num_words = num_words.strip()
    num_words = int(num_words)

    key = []
    for i in range(num_words):
        word = sys.stdin.readline()
        word = word.strip()
        key.append(word)

    return grid, key

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid
def find_word (grid, word):                                #error with grid
    grid_len = len(grid)
    test_word = list(word)
    for i in range(grid_len):
        for j in range(grid_len):
            if grid[i][j] == test_word[0]:
                if i >= 0:   #up
                    l = 0
                    m = i
                    repeat = True
                    while m >= 0 and repeat == True:
                        if grid[m][j] == test_word[l]:
                            if l == len(test_word) - 1:
                                return (i + 1, j + 1)
                            else:
                                m -= 1
                                l += 1
                        else:
                            repeat = False
                
                if i >= 0 and j < grid_len: #up right
                    l = 0
                    m = i
                    n = j
                    repeat = True
                    while n < grid_len and m >= 0 and repeat == True:
                        if grid[m][n] == test_word[l]:
                            if l == len(test_word) - 1:
                                return (i + 1, j + 1)
                            else:
                                m -= 1
                                n += 1
                                l += 1
                        else:
                            repeat = False

                if j < grid_len:   #right
                    l = 0
                    n = j
                    repeat = True
                    while n < grid_len and repeat == True:
                        if grid[i][n] == test_word[l]:
                            if l == len(test_word) - 1:
                                return (i + 1, j + 1)
                            else:
                                n += 1
                                l += 1
                        else:
                            repeat = False
                    
                if i < grid_len and j < grid_len: #down right
                    l = 0
                    m = i
                    n = j
                    repeat = True
                    while m < grid_len and n < grid_len and repeat == True:
                        if grid[m][n] == test_word[l]:
                            if l == len(test_word) - 1:
                                return (i + 1, j + 1)
                            else:
                                m += 1
                                n += 1
                                l += 1
                        else:
                            repeat = False
                    
                if i < grid_len:   #down
                    l = 0
                    m = i
                    repeat = True
                    while m < grid_len and repeat == True:
                        if grid[m][j] == test_word[l]:
                            if l == len(test_word) - 1:
                                return (i + 1, j + 1)
                            else:
                                m += 1
                                l += 1
                        else:
                            repeat = False

                if i < grid_len and j >= 0: #down left
                    l = 0
                    m = i
                    n = j
                    repeat = True
                    while m < grid_len and n >= 0 and repeat == True:
                        if grid[m][n] == test_word[l]:
                            if l == len(test_word) - 1:
                                return (i + 1, j + 1)
                            else:
                                m += 1
                                n -= 1
                                l += 1
                        else:
                            repeat = False

                if j >= 0:   #left
                    l = 0
                    n = j
                    repeat = True
                    while n >= 0 and repeat == True:
                        if grid[i][n] == test_word[l]:
                            if l == len(test_word) - 1:
                                return (i + 1, j + 1)
                            else:
                                n -= 1
                                l += 1
                        else:
                            repeat = False
                    
                if i >= 0 and j >= 0: #up left
                    l = 0
                    m = i
                    n = j
                    repeat = True
                    while m >= 0 and n >= 0 and repeat == True:
                        if grid[m][n] == test_word[l]:
                            if l == len(test_word) - 1:
                                return (i + 1, j + 1)
                            else:
                                m -= 1
                                n -= 1
                                l += 1
                        else:
                            repeat = False
    return (0, 0)

def main():
    # read the input file from stdin
    word_grid, word_list = read_input()

    # find each word and print its location
    for word in word_list:
        location = find_word (word_grid, word)
        print (word + ": " + str(location))

if __name__ == "__main__":
  main()