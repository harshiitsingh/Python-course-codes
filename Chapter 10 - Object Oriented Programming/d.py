class gas:

    def __init__(self,n,p,k):
        self.n = n
        self.p = p
        self.k = k

    def ans(self):
        a = 0
        d = 1
        j = 0
        while d<=self.n:
            x = 0
            i = 0

            while x<self.p:
                if j == (i%self.k):
                    a = i
                
                x += 1
                d += 1
                i += 1
            
            if x == self.p:
                j += 1

        return a

t = int(input())
for i in range(t):
        n,p,k= map(int,input().split())
        answer = gas(n,p,k)

        print(answer.ans())
        