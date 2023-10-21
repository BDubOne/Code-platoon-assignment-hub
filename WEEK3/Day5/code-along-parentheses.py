'''/**
* @param {string} s
*@return {number}
*/'''

def longestValidParentheses(s):

    '''
    String only has parenthesis
    return the length of thel ongest valud substring
    -valid open/closing parenthesis
    -count length in characters
    
    -Examples:
    -Multiple Valid Substrings
    ")())((()))"
    -Invaled Examples:
    --")("
    --"((((
        --edge cases
        
        
    '''

    '''
    Solution
    
    --Every time we get a "(", we have opened a possible valid parens. need a corresponding ")" to close it
    -Need to track when one is opened and when it is closed
    '''
    stack = []
    
    # open_square = "["
    # closed_square="]"
    open = "("
    closed= ")"
    longest_valid = 0
    current_longest_valid = 0
   
    for i in range(len(s)):
        cur = s[i]
        print(f"cur is {cur}")
        


        if len(stack) > 0 and cur == closed and stack[-1] == open:
            current_longest_valid += 2
            
            stack.pop()
            if longest_valid < current_longest_valid:
                longest_valid = current_longest_valid
        
        elif cur == open:
            stack.append(cur)
        
        else:
            if current_longest_valid > longest_valid:
                longest_valid = current_longest_valid
                current_longest_valid = 0

    return current_longest_valid
print(longestValidParentheses(")())()))"))

print(longestValidParentheses("(((((((()))))))))"))


