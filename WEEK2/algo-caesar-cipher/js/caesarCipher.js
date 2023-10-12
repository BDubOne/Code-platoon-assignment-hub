exports.caesarCipher = function(str, numAsc) {
    strArr = str.split('');

    for (i = 0; i < strArr.length; i++) {
        let testEl = strArr[i].toUpperCase().charCodeAt();
        let changeEl = strArr[i].charCodeAt();
        if ((numAsc >= 0 && testEl >= 65 && (testEl + numAsc) <= 90) ||
        (numAsc < 0 && testEl >= 65 && (testEl + numAsc) >= 65 && testEl <= 90)) { 
            strArr[i] = String.fromCharCode((changeEl + numAsc));
        } else if (numAsc >= 0 && testEl >= 65 && (testEl + numAsc) > 90) {
            strArr[i] = String.fromCharCode(changeEl - (26 - numAsc));
        } else if ((numAsc < 0 && testEl >= 65 && (testEl + numAsc) < 65 && testEl <= 90)) {

            strArr[i] = String.fromCharCode(changeEl + (26 + numAsc));
        } else {
            strArr[i] = strArr[i];
        }
    }
    caesarString = strArr.join('')
    console.log(caesarString)
    return caesarString

    


};
