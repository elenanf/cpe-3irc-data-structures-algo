L = [10, 5, 2, 76, 51, 1, 18]

def sort_tab_recursif(L):
    n = len(L)
    print(L)

    #base case
    if (n == 0):
        return []
    if (n == 1):
        return L
    if (n == 2):
        if (L[0] < L[1]):
            return L
        else:
            return [L[1], L[0]]

    first_third = n//3
    last_third = 2*n//3

    if (n % 3 != 0):
        first_third += 1
        last_third += 1


    L[:last_third] = sort_tab_recursif(L[:last_third])
    L[first_third:] = sort_tab_recursif(L[first_third:])
    L[:last_third] = sort_tab_recursif(L[:last_third])

    return L

    
print(sort_tab_recursif(L))