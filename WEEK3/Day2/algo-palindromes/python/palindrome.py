def palindrome(word):
    stripped_str = ''.join(i for i in str(word) if i.isalnum()).lower()

    def palinwhat(s):
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return palinwhat(s[1:-1])
        else: 
            return False
    return palinwhat(stripped_str)
print(palindrome(141))
