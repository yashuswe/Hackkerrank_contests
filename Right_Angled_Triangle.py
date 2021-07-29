#Program to print the right angle triangle with integer range given by user
def num(n):
    num=1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=" ")
            num=num+1
        print("\r")
n=int(input())
num(n)
