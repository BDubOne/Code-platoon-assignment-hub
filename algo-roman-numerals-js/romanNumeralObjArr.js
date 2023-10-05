const romanNumerals = [
    {name: "I", value: 1},
    {name: "IV", value: 4, isSpecial:true},
    {name: "v", value: 5},
    {name: "IX", value: 9, isSpecial:true},
    {name: "X", value: 10},
    {name: "XL", value: 40, isSpecial:true},
    {name: "L", value: 50},
    {name: "XC", value: 90, isSpecial:true},
    {name: "C", value: 100},
    {name: "CD", value: 400, isSpecial:true},
    {name: "D", value: 500},
    {name: "CM", value: 900, isSpecial:true},
    {name: "M", value:1000},
];
function toRomanLazy(num) {}

function toRoman(num) {
    let roman = ''
    for (let x = romanNumerals.length - 1; x >=0; x--) {
        amountDivides = Math.floor(num / romanNumerals[x].value);
        
        if(amountDivides > 0) {
            roman += romanNumerals[x].name.repeat(amountDivides)
            num-= amountDivides * romanNumerals[x].value
        }

            if(num == 0) return roman;
        }
        return "err";
    }
   
        
    
console.log(toRoman(599))