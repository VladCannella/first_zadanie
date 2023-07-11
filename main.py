def reverse_check(string):
    first = string
    second = ''.join(reversed(string))
    if first == second:
        return True
    else:
        return False
    
print(reverse_check('goog'))
print(reverse_check('good'))