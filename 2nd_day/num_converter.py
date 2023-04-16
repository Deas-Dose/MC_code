f,s="1100 V/III/MCMLXXXV".split()
r={1000:'M',100:'C',50:'L',10:'X',5:'V',1:'I'}
z={v:k for k,v in r.items()}
e=s.split('/')
f=int(f)
g=["",0]
for x in r:
    while f>=x:
        g[0]+=r[x]
        f-=x
def a(b):
    c=0
    for i in range(len(b)):
        if i+1!=len(b) and z[b[i]]<z[b[i+1]]:
            c-=z[b[i]]
        else:
            c+=z[b[i]]
    return str(c)
g[1]="/".join(a(d) for d in e)
print(" ".join(g))
