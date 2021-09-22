# def change(string):
#     s = ''
#     for c in string:
#         s += '#' if c =='1' else ' '

#     return s
    
# def solution(n, arr1, arr2):
#     print([change(bin(x|y).zfill(n)[2:]) for x, y in zip(arr1, arr2)])
#     return [change(bin(x|y).zfill(n)[2:]) for x, y in zip(arr1, arr2)]

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])  == 
   ["#####",
    "# # #", 
    "### #", 
    "#  ##", 
    "#####"]
)

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]) == 
   ["######", 
    "### #", 
    "## ##", 
    " #### ", 
    " #####", 
    "### # "]
)