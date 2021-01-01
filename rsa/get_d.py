def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m,n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def totient(p, q):
    return (p - 1) * (q - 1)
# Calculate d in d = (1 + x * totient_n) / e

if __name__ == '__main__':
    print('GetD.py')
    e = int(input('please enter e:'))
    p = int(input('please enter p:'))
    q = int(input('please enter q:'))
    print(egcd(e, totient(p, q)))
