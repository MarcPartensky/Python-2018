def name(var):
    for n,v in globals().items() :
        if v is var :
            return n
    return '?????' 
 
def printv(var):
    print(name(var))
 
nom1 = 132
printv( nom1 )
