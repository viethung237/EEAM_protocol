def MyPowerMod(b,c,q):
    a = 1
    str = bin(c)[2:]
    for i in range(len(str)-1):
        if str[i] == '1':
            a = a*b
        a = (a**2) % q
        
    if str[-1] == '1' :
        a = a*b

    a = a % q
    return a
def Chebyshev(p,x,n): #Tn(x)mod p;n = g ^alpha
    if(p%4 != 3):
        sys.exit
    if MyPowerMod(x**2 -1,(p-1)//2,p) != 1:
        sys.exit
    k = (p+1)//4
    a = (x  + MyPowerMod(x**2-1,k,p)) % p
    r0 = pow(2,-1,p) 
    r1 = MyPowerMod(a,n,p)
    r2 = pow(r1,-1,p)
    r = (r0*(r1+r2)) %p
    return r  
    
def caculate(x,n):
    if(p%4 != 3):
        sys.exit
    if MyPowerMod(x**2 -1,(p-1)//2,p) != 1:
        sys.exit
    k = (p+1)//4
    a = (x  + MyPowerMod(x**2-1,k,p)) % p
    r0 = pow(2,-1,p) 
    r1 = MyPowerMod(a,n,p)
    r2 = pow(r1,-1,p)
    r = (r0*(r1+r2))
    return r