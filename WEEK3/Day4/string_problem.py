
def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    if len(words) == 0:
        return result
    result = []
    

    if len(result) > 0 and (len(result[-1]) + len(words[0])) <=maxWidth:
        result[-1] = f"{result[-1]} {words[0]}"
        words.pop(0)
        
    elif len(result) == 0:
        result.append
    return fullJustify(words, maxWidth)
    
    if len(f'{result[-1]} {words[0]}') >maxWidth:
        result.append(words[0])
        for i in range(result(-1)):
            word_count = len(result[i].split(' '))
            empty_space = maxWidth - len(result[i])
            if word_count - empty_space >= 0:
                added_padding = empty_space // len(result[i].split(' '))
                result[i] = result[i].split(' ').join(' '*added_padding)

print(fullJustify(['potato', 'organ', 'hotdog', 'climb', 'the', 'lonely', 'road'], 16))

    
            