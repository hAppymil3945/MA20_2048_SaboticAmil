def pack5(a,b,c,d,e):
    if d == 0:
        d,e = e,0

    if c == 0:
        c,d,e = d,e,0

    if b==0:
        b,c,d,e=c,d,e,0

    if a==0:
        a,b,c,d,e = b,c,d,e,0

    if a==b:
        a,b,c,d,e=2*a,c,d,e,0

    if b==c:
        b,c,d,e=2*b,d,e,0

    if c==d:
        c,d,e=2*c,e,0

    if d==e:
        d,e=2*d,0
        e=0
    return a,b,c,d,e

print(pack5(2,2,4,4,4))
print(pack5(0,0,0,0,2))
print(pack5(0,4,4,2,2))