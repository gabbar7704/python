def fun(a,b,c,n):
    if(n>2):
        if((a**n)+(b**n)==(c**n)):
            print("Holy Smokes,Fermal was wrong!")
        else:
            print("No,that doesn't work.")

    else:
        print("No,that doesn't work.")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
n=int(input("n:"))
fun(a,b,c,n)