data = []

with open("input.txt", "r") as f:
    for i in f:
        data.append(i.strip())

def conditions(data, word):
    count = 0
    coords = []
    rows = len(data)
    cols = len(data[0])
    for x in range(rows):
        for y in range(cols):
            if data[x][y] == word[0]:
                coords.append((x, y)) # saves the index location of every X

    def check(x, y, dx, dy):
        for i in range(1, len(word)):
            nx = x + i*dx
            ny = y + i*dy # calculate new x and new y in all 8 directions
            if not (0 <= nx < rows and 0 <= ny < cols): # exclude those that are out of bounds
                return False
            if data[nx][ny] != word[i]: # from index location of X, check the 8 adjacent squares for the next letter
                return False
        return True   
        
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, -1), (1, 1)] 
    for xcoord, ycoord in coords:
        for dx, dy in directions:
            if check(xcoord, ycoord, dx, dy):
                count += 1

    return count 
                
conditions(data, "XMAS") # part 1

def crosscheck(data, word):
    rows = len(data)
    cols = len(data[0])
    count = 0

    for x in range(1, rows-1):
        for y in range(1, cols-1):
            if data[x][y] == word[1]: # check middle letter
                word1 = data[x+1][y+1] + data[x][y] + data[x-1][y-1] # check what word is from top left to bot right
                word2 = data[x+1][y-1] + data[x][y] + data[x-1][y+1] # check what word is from bot left to top right
                if word1 in (word, word[::-1]) and word2 in (word, word[::-1]):
                    count += 1
                
    return count

crosscheck(data, "MAS") # part 2