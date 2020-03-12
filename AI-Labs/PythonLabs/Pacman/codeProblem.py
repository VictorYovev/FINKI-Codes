import random


class Game:
    first, first1 = -1, -1

    def __init__(self, rows, columns, matrix):
        self.rows = rows
        self.columns = columns
        self.matrix = matrix
        self.dots = 0
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '.':
                    if self.first == -1:
                        self.first = i
                        self.first1 = j
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

    def play_game(self):
        xx, yy = 0, 0
        self.player.x = self.game.first
        self.player.y = self.game.first1
        flag = False
        while self.game.dots != 0:

            if self.game.matrix[self.player.x][self.player.y] == '.':
                self.game.dots -= 1
                self.game.matrix[self.player.x][self.player.y] = '!'

            self.random_moves.append((list([self.player.x, self.player.y])))

            if flag:
                xx = random.randint(self.player.x - 1 if self.player.x - 1 >= 0 else self.player.x,
                                    self.player.x + 1 if self.player.x + 1 < self.game.rows else self.player.x)
            else:
                yy = random.randint(self.player.y - 1 if self.player.y - 1 >= 0 else self.player.y,
                                    self.player.y + 1 if self.player.y + 1 < self.game.columns else self.player.y)

            flag = not flag
            self.player.move(tuple((xx, yy)))
        return self.random_moves


r = int(input())
c = int(input())
pacman = []
for each in range(r):
    pacman.append(list(input()))

gm = Game(r, c, pacman)
pl = Player()
pacman = Pacman(pl, gm)
print(*(pacman.play_game()), sep='\n')
