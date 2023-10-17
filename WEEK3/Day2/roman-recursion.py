# def roman_recursion(num):
    # if num == 1:
    #     return "I"

        
    
    # for idx in ordered_numerals:
    #     numeral = idx['r']
    #     val = idx['a']
         
    #     if  num >= val:
    #         times = num//val
    #         result += numeral* times
    #         num -= (val*times)
    # return result
   
def roman_recursion(num, ordered_numerals):   
 

    if num == 0:
        return ""
    for idx in range(len(ordered_numerals)):

        numeral = ordered_numerals[idx]['r']
        val = ordered_numerals[idx]['a']
        if num >= val:
            times = num//val
            return numeral * times + roman_recursion(num - val*times, ordered_numerals)

    return roman_recursion(num, ordered_numerals[1:])
    
    
    
ordered_numerals = [
    {"a" : 1000, "r": "M"},
    {"a" : 900, "r": "CM"},
    {"a" : 500, "r": "D"},
    {"a" : 400, "r": "CD"},
    {"a" : 100, "r": "C"},
    {"a" : 90, "r": "XC"},
    {"a" : 50, "r": "L"},
    {"a" : 40, "r": "XL"},
    {"a" : 10, "r": "X"},
    {"a" : 9, "r": "IX"},
    {"a" : 5, "r": "V"},
    {"a" : 4, "r": "IV"},
    {"a" : 1, "r": "I"},
]   


print(roman_recursion(494, ordered_numerals))
