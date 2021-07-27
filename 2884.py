H, M = (int(x) for x in input().split())

if M >= 45:
    print(H, M-45, sep=' ')
else:
    if H:
        print(H-1, M+15, sep=' ')
    else:
        print(23, M+15, sep=' ')