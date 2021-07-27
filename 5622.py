dial = {
    'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5, 
    'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9
}
    
def findval(x):
    for key in dial:
        if x in key:
            return dial[key]+1
        

print(sum(map(findval, input())))