def f(A,B):
    return int( A and B)
print('A,B,f(A,B)-конъюнкция')
for A in 0,1:
    for B in 0,1:
        print(A,B,'|',f(A,B))

def f(A,B):
    return int( A or B)
print('A,B,f(A,B)-дизъюнкция')
for A in 0,1:
    for B in 0,1:
        print(A,B,'|',f(A,B))

def f(A,B):
    return int( A <= B)
print('A,B,f(A,B)-импликация')
for A in 0,1:
    for B in 0,1:
        print(A,B,'|',f(A,B))

def f(A,B):
    return int( A == B)
print('A,B,f(A,B)-эквиваленция')
for A in 0,1:
    for B in 0,1:
        print(A,B,'|',f(A,B))

def f(A):
    return int( not(not A))
print('A,not(not A)')
for A in 0,1:
    print(A,'|',f(A))

def f(A,B):
    return int(not(A and B))
def g(A,B):
    return int((not A) or (not B))
print('A|B|f(A,B)|g(A,B)')
for A in 0,1:
    for B in 0,1:
        print(A,B,'|',f(A,B),'|',g(A,B))

def f(A,B,C):
    return int(A and(B or C))
def g(A,B,C):
    return int((A and B) or (A and C))
print('A|B|C|f(A,B,C)|g(A,B,C)')
for A in 0,1:
    for B in 0,1:
        for C in 0,1:
            print(A,B,C,'|',f(A,B,C),'|',g(A,B,C))












