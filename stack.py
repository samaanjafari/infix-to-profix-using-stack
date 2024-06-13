from prec import HigherPrecedence


class Stack:
    def __init__(self):
        self._data = []
        
    def push(self, data):
        self._data.append(data)
        
    def pop(self):
        return self._data.pop()
        
    def top(self):
        if self._data!=[]:
            return self._data[-1]
        else:
            return None
        
    def empty(self):
        if self._data==[]:
            return True
        else:
            return False
            
    def length(self):
        return len(self._data)
         
    def _print(self):
        print(self._data)
      
stack = Stack()


exp = input("write your experession: ")

operators = '(*/+-)^'

profix = []
'''-----------------------------------------------------------------------------------------'''

for i in range(len(exp)):
    
    if exp[i] not in operators:
        profix.append(exp[i])
        print(profix)
    

    else:
        while (not stack.empty()  and stack.top()!='(' and HigherPrecedence(stack.top(), exp[i])):
            if exp[i]!=')':
                element = stack.pop()
                profix.append(element)
            else:
                break
            
                    
        if exp[i]==')':
            while(stack.top()!='('):
                element = stack.pop()
                profix.append(element)
            stack.pop()                
        
        elif stack.empty():
            stack.push(exp[i])
            stack._print()
        
        if stack.top()=='(' or not HigherPrecedence(stack.top(), exp[i]):
            if exp[i]!=')':
                stack.push(exp[i])
                stack._print()

        
                                  
while ( not stack.empty()):
    element = stack.pop()
    print(element)
    if element!='(':
        profix.append(element)
        
profix = ''.join(profix)

print(profix)                       
            