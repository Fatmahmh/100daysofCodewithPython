# 1st challenge
def Recursion(x,p):
    if p>0 :
        result = x*Recursion(x,p-1)
    else:
        result = 1
    return result
print(Recursion(5,3))



# 2nd challenge
numbers = [-4, -6, -5, -1, 2, 3, 7, 9, 88]

def positive_No(list) :
    y = lambda x : x>0
    for x in list:
        if (y(x)):
            print(x)
positive_No(numbers)



