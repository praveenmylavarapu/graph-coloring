# ADS Package - Graph coloring applications - Radio frequency distribution

from math import pi, sin, cos, acos

class graph:
    def __init__(self, n):
        self.Adj = [[] for i in range(n)]
        self.color = [0 for i in range(n)]
        self.degree = [0 for i in range(n)]
        self.n = n
    def add_edge(self,a,b):
        self.Adj[a].append(b)
        self.Adj[b].append(a)
        self.degree[a] += 1
        self.degree[b] += 1
    def color_me(self):
        p = self.degree[:]
        colors = [i for i in range(1,self.n+1)]
        while(True):
            ucd = []
            v = max(p)
            if v<0:
                break
            vi = p.index(v)
            if self.color[vi] != 0:
                p[vi] = -1
                continue
            for i in self.Adj[vi]:
                ucd.append(self.color[i])
            for i in colors:
                if i not in ucd:
                    self.color[vi] = i
                    break
            p[vi] = -1
        return max(self.color)

def greatCircleDistance(la1,la2,lo1,lo2):
    if la1 == la2 and lo1 == lo2:   return 0
    return ( acos(sin(la1*pi/180)*sin(la2*pi/180)+cos(la1*pi/180)*cos(la2*pi/180)*cos((lo2-lo1)*pi/180)) * 3956 )

f = open('TNcities.csv', 'r')
G = graph(2839)
i = 0
for line in f.readlines():
    s = line.split(',')
    s[1] = float(s[1])
    s[2] = float(s[2])
    g = open('TNcities.csv', 'r')
    j = 0
    for line1 in g.readlines():
        if j <= i:
            j += 1
            continue
        s1 = line1.split(',')
        s1[1] = float(s1[1])
        s1[2] = float(s1[2])
        if greatCircleDistance(s[1],s1[1], s[2], s1[2]) < 25:
            G.add_edge(i,j)
            
        j += 1
    g.close()
    i += 1
            
f.close()

cn = G.color_me()
print('\nNumber of frequencies needed: ',cn)

for i in range(1,cn+1):
    h = open('TNcities.csv', 'r')
    print('Frequency', i, ':')
    n=0
    for line in h.readlines():
        if i == G.color[n]:
            print('\t', line.split(',')[0])
        n+=1
    h.close()
