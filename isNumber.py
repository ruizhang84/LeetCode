# Validate if a given string is numeric.

# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true

# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

# int 1234
# +/-1234
# float 12.34
# +/-1e+/-12
# ".1" "1."
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if 'e' in s:
            temp = s.split('e')
            if len(temp) != 2:
                return False
            a, b = temp
            a = strip_sign(a)
            b = strip_sign(b)
            return isfloat(a) and isint(b)
        s = strip_sign(s)
        return isfloat(s)
         
def isint(s):
    if len(s) == 0:
        return False
    for i in s:
        if i not in '1234567890':
            return False
    return True

def isfloat(s):  
    if isint(s):
        return True
    
    temp = s.split('.')
    if len(temp) != 2:
        return False
    a,b = temp
    if len(a) == 0:
        return isint(b)
    elif len(b) == 0:
        return isint(a)
    return isint(a) and isint(b)


def strip_sign(s):
    if len(s) > 0 and (s[0] == '+' or s[0] == '-'):
        return s[1:]
    return s