def HigherPrecedence(top, operator):
    prec1 = ['(', ')']
    prec2 = ['^']
    prec3 = ['*', '/']
    prec4 = ['+', '-']
    precs = [prec1, prec2, prec3, prec4]
    
    for i in range(len(precs)):
        for j in range(len(precs)):
            if top in precs[i] and operator in precs[j]:
                if i < j:
                    return True
                elif i > j:
                    return False
                else:
                    return True  # If they have the same precedence, return True


#easier way

# def HigherPrecedence(a, b):
#     precedence = {
#         '(': 0, ')': 0,
#         '*': 1, '/': 1,
#         '+': 2, '-': 2
#     }
    
    # if precedence[a] < precedence[b]:
    #     return a
    # elif precedence[a] > precedence[b]:
    #     return b
    # else:
    #     return a  # If both have the same precedence, return the first one 

# print(HigherPrecedence('+', '*'))



