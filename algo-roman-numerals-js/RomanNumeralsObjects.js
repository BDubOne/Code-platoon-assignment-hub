function toRoman(num) {
    let output = '';
    const numeralCharacters = {
        M : 1000,
        CM : 900,
        D : 500,
        CD : 400,
        C : 100,
        XC : 90,
        L : 50,
        XL : 40,
        X : 10,
        IX : 9,
        V : 5,
        IV : 4,
        I : 1
    };

    const priorityOrder = [
        "M", 
        "CM", 
        "D", 
        "CD", 
        "C", 
        "XC", 
        "L", 
        "XL",
        "X",
        "IX",
        "V",
        "IV",
        "I"
    ];
    for (ltr of priorityOrder) {
        if (num / numeralCharacters[ltr] >= 1) {
        howMany = Math.floor(num/ numeralCharacters[ltr]);
        for (i = howMany; i > 0; i--) {
            output += ltr;
            num -= numeralCharacters[ltr];
        }
        }
    }
console.log(output);
return output;

    }
console.log(toRoman(344))