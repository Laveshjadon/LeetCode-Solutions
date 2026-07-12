class Solution(object):
    def simplifyPath(self, path):
       comp = path.split('/')
       stack = []
       for c in comp:
        if c == '' or c == '.':
            continue
        elif c == '..':
            if stack:
                stack.pop()
        else:
            stack.append(c)
       return '/' + '/'.join(stack)

        