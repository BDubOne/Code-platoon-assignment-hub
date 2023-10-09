exports.isCharacterMatch = function(string1, string2) {
   
 let sorted1 = string1.toLowerCase().split('').sort().join('').trim();
 let sorted2 = string2.toLowerCase().split('').sort().join('').trim();
console.log(sorted1);
console.log(sorted2);
if (sorted1 === sorted2) {
    return true;
} else {
    return false;
}
};


//exports.
exports.anagramsFor = function(word, listOfWords) {

    let sortedWord = word.toLowerCase().split('').sort().join('');
    let anaRay = []

    for (let i = 0; i < listOfWords.length; i++) {
        
        let sortedCurrent = listOfWords[i]
        .toLowerCase().split('').sort().join('');

        if (sortedWord === sortedCurrent) {
            anaRay.push(listOfWords[i])

        }
    }
    console.log(anaRay)
    return anaRay
};

// console.log(anagramsFor('threads',["threads", "trashed", "hardest", "hatreds", "hounds"]));
