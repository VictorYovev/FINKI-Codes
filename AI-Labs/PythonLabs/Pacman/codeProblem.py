import random


class Game:
    def __init__(self, rows, columns, matrix):
        self.rows = rows
        self.columns = columns
        self.matrix = matrix
        self.dots = 0
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '.':
                    self.dots += 1


class Player:
    def __init__(self):
        self.x, self.y = 0, 0

    def move(self, position):
        self.x = position[0]
        self.y = position[1]


class Pacman:
    random_moves = []

    def __init__(self, player, game):
        self.player = player
        self.game = game

    def findPosition(self):
        possible_positions = []
        whatever_positions = []
        if self.player.x + 1 < self.game.rows:
            if self.game.matrix[self.player.x + 1][self.player.y] == '.':
                possible_positions.append(list([self.player.x + 1, self.player.y]))
            else:
                whatever_positions.append(list([self.player.x + 1, self.player.y]))
        if self.player.x - 1 >= 0:
            if self.game.matrix[self.player.x - 1][self.player.y] == '.':
                possible_positions.append(list([self.player.x - 1, self.player.y]))
            else:
                whatever_positions.append(list([self.player.x - 1, self.player.y]))
        if self.player.y + 1 < self.game.columns:
            if self.game.matrix[self.player.x][self.player.y + 1] == '.':
                possible_positions.append(list([self.player.x, self.player.y + 1]))
            else:
                whatever_positions.append(list([self.player.x, self.player.y + 1]))
        if self.player.y - 1 >= 0:
            if self.game.matrix[self.player.x][self.player.y - 1] == '.':
                possible_positions.append(list([self.player.x, self.player.y - 1]))
            else:
                whatever_positions.append(list([self.player.x, self.player.y - 1]))

        if len(possible_positions) != 0:
            return possible_positions[random.randint(0, len(possible_positions) - 1)]
        else:
            return whatever_positions[random.randint(0, len(whatever_positions) - 1)]

    def play_game(self):
        if self.game.dots == 0:
            return 'Nothing to do here'
        while self.game.dots != 0:
            position = self.findPosition()
            if self.game.matrix[position[0]][position[1]] == '.':
                self.game.dots -= 1
            self.game.matrix[position[0]][position[1]] = '#'
            self.random_moves.append((list([position[0], position[1]])))
            self.player.move(tuple((position[0], position[1])))
        return self.random_moves


r = int(input())
c = int(input())
pacman = []
for each in range(r):
    pacman.append(list(input()))

gm = Game(r, c, pacman)
pl = Player()
pacman = Pacman(pl, gm)
result = pacman.play_game()
if result != 'Nothing to do here':
    print(*result, sep='\n')
else:
    print(result)
