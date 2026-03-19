def recursive_decrease(n):
    print(n)
    if n == 1:
        return
    recursive_decrease(n-1)
    

#recursive_decrease(5)

def recursive_increase(n):
    if n < 1:
        return
    recursive_increase(n-1)
    print(n)
    
recursive_increase(6)