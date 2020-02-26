
def triangle(n1, n2, n3):
    ''' a program in Python to classify triangles'''
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    res = " "
    if n1 == 0 or n2 == 0 or n3 == 0:
        res = "Invalid Input"
    elif n1 == n2 == n3:
        res = "equilateral"
    elif n1 == n2 or n1 == n3 or n2 == n3:
        res = "isosceles"
    elif n1 != n2 and n1 != n3 and n2 != n3:
        res = "scalene"
    elif n1**2 + n2**2 == n3**2 or n1**2 + n3**2 == n2**2 or n2**2 + n3**2 == n1**2:
        res = "right angle triangle"
    else:
        res = "please enter all the three sides "
    return res

def triangle(n1, n2, n3):
    ''' a program in Python to classify triangles'''
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    res = " "
    if n1 == 0 or n2 == 0 or n3 == 0:
        res = "Invalid Input"
    elif n1 == n2 == n3:
        res = "equilateral"
    elif n1 == n2 or n1 == n3 or n2 == n3:
        res = "isosceles"
    elif n1 != n2 and n1 != n3 and n2 != n3:
        res = "scalene"
    elif n1**2 + n2**2 == n3**2 or n1**2 + n3**2 == n2**2 or n2**2 + n3**2 == n1**2:
        res = "right angle triangle"
    else:
        res = "please enter all the three sides "
    return res
