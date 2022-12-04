from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
import random

N = 4

E = Encoding()

#============== Propositions ==================

@proposition(E)
class Attack:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates  # tuple of coordinates

    def __repr__(self):
        return f"Attack({self.coordinates[0]}, {self.coordinates[1]})"


@proposition(E)
class Empty:
    def __init__(self, empty, coordinates):
        self.empty = empty
        self.coordinates = coordinates

    def __repr__(self):
        return f"Empty({self.coordinates[0]}, {self.coordinates[1]})"


@proposition(E)
class King:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"King({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"King({self.coordinates[0]}, {self.coordinates[1]})"


@proposition(E)
class Bishop:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Bishop({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Bishop({self.coordinates[0]}, {self.coordinates[1]})"


@proposition(E)
class Rook:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Rook({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Rook({self.coordinates[0]}, {self.coordinates[1]})"


@proposition(E)
class Knight:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Knight({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Knight({self.coordinates[0]}, {self.coordinates[1]})"

@proposition(E)
class Queen:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Queen({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Queen({self.coordinates[0]}, {self.coordinates[1]})"

#===============================================






#============== Theory ====================
def theory(pieces):

    #================= Piece Constraints ==================

    for piece in pieces:

        x = piece.coordinates[0]
        y = piece.coordinates[1]

        #King constraints
        if piece.piece == "K":
            E.add_constraint(King("K", (x, y)) >> (
                Attack("A", (x, y + 1))
                & Attack("A", (x, y - 1))
                & Attack("A", (x + 1, y))
                & Attack("A", (x - 1, y))
                & Attack("A", (x + 1, y + 1))
                & Attack("A", (x + 1, y - 1))
                & Attack("A", (x - 1, y + 1))
                & Attack("A", (x - 1, y - 1))
            ))

        #Knight constraints
        if piece.piece == "H":
            E.add_constraint(Knight("H", (x, y)) >> (
                Attack("A", (x + 2, y + 1))
                & Attack("A", (x + 2, y - 1))
                & Attack("A", (x - 2, y + 1))
                & Attack("A", (x - 2, y - 1))
                & Attack("A", (x + 1, y + 2))
                & Attack("A", (x + 1, y - 2))
                & Attack("A", (x - 1, y + 2))
                & Attack("A", (x - 1, y - 2))
            ))

        #Rook constraints
        if piece.piece == "R":
            for i in range(1, N):
                E.add_constraint(Rook("R", (x, y)) >> (
                    Attack("A", (x + i, y)) #Right
                    & Attack("A", (x, y - 1)) #Up
                    & Attack("A", (x - i, y)) #Left
                    & Attack("A", (x, y + 1)) #Down
                ))

        #Bishop constraints
        if piece.piece == "B":
            for i in range(1, N):
                E.add_constraint(Bishop("B", (x, y)) >> (
                    Attack("A", (x + i, y - i)) #Up and right
                    & Attack("A", (x - i, y - i)) #Up and left
                    & Attack("A", (x + i, y + i)) #Down and right
                    & Attack("A", (x - i, y + i)) #Down and left
                ))

            #Queen constraints
        if piece.piece == "Q":
            for i in range(1, N):
                E.add_constraint(Queen("Q", (x, y)) >> (
                    Attack("A", (x + i, y)) #Right
                    & Attack("A", (x, y - i)) #Up
                    & Attack("A", (x - i, y)) #Left
                    & Attack("A", (x, y + i)))) #Down
                E.add_constraint(Queen("Q", (x, y)) >> (
                    Attack("A", (x + i, y - i)) #Up and right
                    & Attack("A", (x - i, y - i)) #Up and left
                    & Attack("A", (x + i, y + i)) #Down and right
                    & Attack("A", (x - i, y + i)) #Down and left
                ))
        
    #================= General Constraints ==================



    #😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂

    return E


def writeSolutionToFile(solution, fileName):
    with open(fileName, 'w') as f:
        f.write(str(len(solution.keys())) + "\n")
        for line in solution.keys():
            #if "A" not in str(line) and "E" not in str(line) and "P" not in str(line):
                #if solution[line] == True:
                    f.write(f"{line}  \t {solution[line]} \n")


def makeBoard():
    board = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            board[i][j] = Empty("E", (i, j))
    return board


def printBoard(board):
    for i in range(N):
        for j in range(N):
            if "Empty" in str(board[i][j]):
                print(" _", end="  ")
            elif "King" in str(board[i][j]):
                print(" K", end="  ")
            elif "Bishop" in str(board[i][j]):
                print(" B", end="  ")
            elif "Rook" in str(board[i][j]):
                print(" R", end="  ")
            elif "Knight" in str(board[i][j]):
                print(" H", end="  ")
            elif "Queen" in str(board[i][j]):
                print(" Q", end="  ")
            elif "Attack" in str(board[i][j]):
                print(" X", end="  ")
        print(" ")


def determineValidity(attacks, pieces):
    for attack in attacks:
        if attack in pieces:
            return False
    return True

def filterUsefull(solution):
    validCoords = []
    for line in solution.keys():
        if solution[line] == True:
            if line.coordinates[0] < N and line.coordinates[1] < N and line.coordinates[0] >= 0 and line.coordinates[1] >= 0:
                validCoords.append(line)
    return validCoords

def setBoard(listOfPropositions, board):
    for proposition in listOfPropositions:
        board[proposition.coordinates[1]][proposition.coordinates[0]] = proposition


if __name__ == "__main__":
    # pieces = random.choices(["K", "H", "Q", "B", "R"], k = N)
    pieces = ["Q"]
    for i, piece in enumerate(pieces):
        if piece == "K":
            pieces[i] = King(piece, (random.randint(0, 3), i))
        elif piece == "H":
            pieces[i] = Knight(piece, (random.randint(0, 3), i))
        elif piece == "Q":
            pieces[i] = Queen(piece, (random.randint(0, 3), i))
        elif piece == "B":
            pieces[i] = Bishop(piece, (random.randint(0, 3), i))
        elif piece == "R":
            pieces[i] = Rook(piece, (random.randint(0, 3), i))

    T = theory(pieces) # Instantiates the theory 
    print(u'\u2713' + " ---> Theory Created")
    
    T = T.compile() # Compiles the theory
    print(u'\u2713' + " ---> Theory Compiled")
    
    solution = T.solve() # Solves the theory
    print(u'\u2713' + " ---> Theory Solution Found")
    print(u'\u2713' + " ---> Theory Satisfiable: %s" % T.satisfiable())
    
    determineValidity(solution, pieces)

    writeSolutionToFile(solution, "Total_Solutions.txt") # Writes full list of bauhaus solutions to a file
    print(u'\u2713' + " ---> Solution Written to File")

    
    board = makeBoard()
    usefullCords = filterUsefull(solution)
    setBoard(usefullCords, board)
    printBoard(board)