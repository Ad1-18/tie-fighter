#===========Setup===========
n = int(input())
k = int(n/2)
x = " "
#===========Main Function===========
def tie_fighter(n):
    if (n%2==0 or n<5):
	    return(print("Error. Enter an odd number greater than 5."))

    else:
        line0(k)
        line1toK(k,1)
        lineK(k)
        lineKtoN(k,k-1)
        lineN(k)

#===========Child Functions===========
def line0(k):
    print("||" + k*x + (k-1)*"_" + k*x + "||")

def line1toK(k,i):
    print("||" + (k-i)*x + "/" + (i-1)*x + (k-1)*x + (i-1)*x + "\\" + (k-i)*x + "||")
    if (i<k-1):
        line1toK(k,i+1)

def lineK(k):
    print("||" + k*"=" + (k-1)*x + k*"=" + "||")

def lineKtoN(k,i):
    print("||" + (k-i)*x + "\\" + (i-1)*x + (k-1)*x + (i-1)*x + "/" + (k-i)*x +"||")
    if (i>1):
        lineKtoN(k,i-1)

def lineN(k):
    print("||" + k*x + (k-1)*"‾" + k*x + "||")

#===========Output===========
tie_fighter(n)