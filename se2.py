groupA,groupB,groupC,a,b,c=[],[],[],[],[],[]
def cricket():
    p=int(input("enter no. of students playing cricket : "))
    for i in range(p):
        l=int(input("enter roll no. of student : "))
        groupA.append(l)
cricket()
print("list of student who plays cricket : ",groupA)

def badminttan():
    q=int(input("enter no. of students play badminttan"))
    for i in range(q):
        m=int(input("enter roll no. of students : "))
        groupB.append(m)
badminttan()
print("list of students who plays badminttan : ",groupB)

def football():
    r=int(input("enter no. of students playing football : "))
    for i in range(r):
        n=int(input("enter roll no. of students : "))
        groupC.append(n)
football()
print("list of students who plays football : ",groupC)

#case 1
def intersectionAB():
    for i in groupA:
        if i in groupB:
            a.append(i)
intersectionAB()
print("list of students who play both cricket and badminttan : ",a)

#case 2
def either():
    x=groupA+groupB
    for i in groupA:
        if i in groupB:
            x.remove(i)
    for i in groupB:
        if i in groupA:
            x.remove(i)
    print("list of students who play either cricket or badminttan but not both :",x)
either()

#case 3
def nither():
    u=groupA+groupB+groupC
    for i in u:
        if i not in groupA:
            if i not in groupB:
                b.append(i)
    print("list of students who play neither cricket nor badminttan : ", b)
nither()

#case 4
def abc():
    u = groupA + groupB + groupC
    for i in u:
        if i not in groupB:
            c.append(i)
    for i in groupA:
        if i in groupC:
            if i in c:
                c.remove(i)
    print("list of students who play cricket and football but not badminttan :",c)
abc()