class Invent:
    
    def __init__(self,n,p,k):
        self.n = n
        self.p = p
        self.k = k

    def days(self):
        ans = 0
        a=p%self.k - 1 
        b=((n-1)//self.k)*self.k
        b=n-1-b
        if (a>b):
            ans+=(b+1)*((self.n-1)//k + 1)+ (a-b)*((self.n-1)//self.k)
        else:
            ans+=((self.n-1)//self.k + 1)*(a+1)
        
        for i in range(a+1,self.n,self.k):
            ans+=1
            if(i==self.p):
                print(ans)
                break
        


num = int(input())
for i in range(num):
        n,p,k = map(int, input().split())
        ans = Invent(n,p,k)
        
        print(ans.days())