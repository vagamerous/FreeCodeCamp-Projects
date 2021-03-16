def arranged_problems(up, down, op):
    a = 0
    while a <= (len(up)-1):
        if up[a] >= down[a]:
            x = len(str(up[a])) + 2        
        else:
            x = len(str(down[a])) + 2
        print(str(up[a]).rjust(x), end='    ')
        a += 1
    print('')
    data = list(zip(op, down))
    a = 0
    while a <= (len(up)-1):
        if up[a] >= down[a]:
            x = len(str(down[a])) + 1        
        else:
            x = len(str(up[a])) + 1
        print(str(data[a][0]).ljust(1), str(data[a][1]).rjust(x), end='    ')
        a += 1
    a = 0
    print('')
    while a <= (len(up)-1):
        if up[a] >= down[a]:
            x = len(str(up[a])) + 2        
        else:
            x = len(str(down[a])) + 2
        print('-'*x, end='    ')
        a += 1
        

        
