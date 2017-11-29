def multiplication_table(m, n):
    i= 1

    while i <= 9:
        for j in range(m,n+1):
            print (j,"*",i,"=",str(j*i).zfill(2),end="         ")
        print('')
        i += 1

def pyramid(n):

    for i in range(n):
        print (' '*(n-i) + '*' *(2*i+1)) 
