
def fullJustify(self, words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    if len(words) == 0:
        return
    result = []
    if result[-1] is not None and len(f'{result[-1]}  {words[0]}') <=maxWidth:
        result[-1] = f"{result[-1]} {words[0]}"
        words.pop[0]
        return fullJustify(words, maxWidth)
    
    if result[-1] is None or len(f'{result[-1]} {words[0]}') >maxWidth:
        result.append(words[0])
        for i in result(0,-2):
            word_count = len(result[i].split(' '))
            empty_space = maxWidth - len(result[i])
            if word_count - empty_space >= 0:
            pass