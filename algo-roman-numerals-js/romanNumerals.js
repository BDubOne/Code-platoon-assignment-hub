function toRoman(num) {
  let romanNumeral = ''
  while (num > 1000) {
    romanNumeral += "M";
    num -= 1000;  
  };

  if (num >= 900) {
    romanNumeral += "CM";
    num -= 900;
  } else {
    num = num;
  }

  while (num > 100) {
    romanNumeral += "C";
    num -= 100;
  };

  if (num >= 90) {
    romanNumeral += "XC";
    num -= 90;
  } else {
    num = num;
  };
  
  if (num >= 50) {
    romanNumeral += "L";
    num -= 50;
  } else {
    num = num;
  };

  if (num >= 40) {
    romanNumeral += "XL";
    num -= 40;
  } else {
    num = num;
  };

  while (num > 10) {
    romanNumeral += "X";
    num -= 10
  };

  if (num === 9) {
    romanNumeral += "IX";
    num -= 9;
  } else {
    num = num;
  };
  if (num >= 5) {
    romanNumeral += "V";
    num -= 5;
  } else {
    num = num;
  }
  
  if (num === 4) {
    romanNumeral += "IV";
    num -= 4;
  };

  while (num >= 1) {
    romanNumeral += "I";
    num -= 1;
  }

  return romanNumeral;

}


module.exports = { toRoman};
