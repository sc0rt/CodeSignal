def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            pleft = i
        if s[i] == ")":
            pright = i
            return reverseParentheses(s[:pleft] + s[pleft+1:pright][::-1] + s[pright+1:])
    return s
