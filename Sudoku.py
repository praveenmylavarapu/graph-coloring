# ADS Package - Graph coloring applications - Solving Sudoku

class Sudoku:
    def __init__(self, q):
        self.Adj = [[] for i in range(81)]
        self.color = [int(q[i]) for i in range(81)]
        self.degree = [20 for i in range(81)]
        for i in range(81):
            r,c = divmod(i,9)
            for j in range(9):  self.Adj[i].append(9*j+c)
            for j in range(9):  self.Adj[i].append(9*r+j)
            b1,b2 = r//3*3, c//3*3
            for j in range(3):
                for k in range(3):
                    p = 9*(b1+k)+b2+j
                    if p not in self.Adj[i]:    self.Adj[i].append(p)
            self.Adj[i].remove(i)
            self.Adj[i].remove(i)

    def print(self):
        for i in range(81):
            print(self.color[i], end = ' ')
            if not (i+1)%9: print()

    def color_me(self):
        colors = [i for i in range(1,10)]
        for vi in range(81):
            v = self.degree[vi]
            if self.color[vi] != 0: continue
            ucd = [self.color[i] for i in self.Adj[vi]]
            for i in colors:
                if i not in ucd:
                    self.color[vi] = i
                    break

G = Sudoku(list('500003040618405370000000000405310726076058010231640908003106284049802605062530190'))
G.print()
print()
G.color_me()
G.print()
