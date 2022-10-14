n=int(input("enter no.of students in a class : "))
persentage=[]

def entry():
    for i in range(n):
        p=float(input("enter persentage of students : "))
        if p>100 or p<0:
            print("enter valid persentage : ")
            p = float(input("enter persentage of students : "))
        persentage.append(p)
    print("unsorted array : ",persentage)

def selection_sort():
    for i in range(n-1):
        for j in range(n):
            if i<j:
                if persentage[i]>persentage[j]:
                    temp=persentage[i]
                    persentage[i]=persentage[j]
                    persentage[j]=temp
    print("sorted array : ",persentage)
    top_five=persentage[n:n-6:-1]
    print("top five scores are : ",top_five)

def bubble_sort():
    for i in range(n-1):
        for j in range(n-1):
            if persentage[j]>persentage[j+1]:
                temp = persentage[j]
                persentage[j] = persentage[j+1]
                persentage[j+1] = temp
    print("sorted array : ", persentage)
    top_five = persentage[n:n - 6:-1]
    print("top five scores are : ", top_five)

print(" 1) entry of persentage\n 2) selection sort\n 3) bubble sort")
print("\t")

while (True):
    ch=int(input("enter choice : "))
    if ch==1:
        entry()
        print("\t")
    elif ch==2:
        selection_sort()
        print("\t")
    elif ch==3:
        bubble_sort()
        print("\t")
    else:
        print("please enter valid choice ")
        print("\t")