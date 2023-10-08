// // Let vs const

// //let can be mutated

// //const cannot

// // //Let is mutable. Const is not

// // let greeting = "Hello Victor"

// // const goodbye = "Goodbye all!"

// // greeting += " 35"

// // //FUNCTIONS

// function makeAName(firstName, lastName) {
//     let fullName = firstName + " " + lastName;
//     return fullName
// }

// ARROW FUNCTIONS

const makeAName = (first, last) => {
    return `${first} ${last}`
}

// MODULES /////////////////////
module.exports = makeAName;

const addingTwos = (num) => {
    return num + 2;
}
module.exports = addingTwos;

// console.log(makeAName("James", "Kirk"))

// // //DRY === "Don't Repeat Yourself!"

// // console.log(greeting)

// // // DATA TYPES

// // // STRINGS

// // //Strings are immutable

// // greeting = "I am a string and this is how I work";

// // console.log(greeting.length);

// // let person = "Adam"

// // console.log(greeting + ", " + person)

// // console.log(`${greeting} ${person}`)

// // //methods --
// // //W3schools


// // //numbers
// // // Math!

// // console.log(Math.pow(3, 2))
// // console.log(Math.floor(3298473289478934.23948234982374982472/4))
// // console.log(Math.ceil(23947897/4))

// // //BOOLEAN

// // // console.log('' == false);
// // // console.log(0 == false);

// // // let x = 5;
// // // let o = 6;

// // // return x === o

// // console.log(undefined == true) //undefined is undefined
// // console.log(undefined == false)

// // console.log(null == true) //null is undefined
// // console.log(null == false) 

// // console.log(null == undefined)

// //undefined means you didn't make variable and it never got value. Null means you assigned a variable and it didn't receive a value.

// // == looks for whether values are equal, ignoring data type
// // === looks for whether values are strictly equal

// //COMPARISON OPERATORS

// let myArray = ["Names", `${35}`, 89, false, {
//     potatoes: "root",
//     leeks: "shoot",
//     spinach: "leaf"
// },
// 955, [122, 35, 255, 67], "Joshua",
// "anthony",
// "Aaron",
// "Adam",
// "Francisco"
// ];


// MAP FUNCTIONS /////////////////////////////////
// let myArray = [
//     1, 2, 3, 4, 5, 6
// ]; 

// myArray.map((placer, idx) => {
//     if (idx % 2 === 0) {
//         console.log(placer);
//     } else {
//         console.log(placer * 2)
//     }
// })

// // console.log(myArray[6][2])
// // console.log(myArray[4].potatoes)
// // myArray[6].push("this is new");

// //OBJECTS

// const database = {
//     457: {
//         name: "Tom",
//         age: 34,
//     },
//     57782: {
//         name: "Sally",
//         age: 42,
//     },
// };

// // console.log(database[57782].age) //Sally age

// // for (key in database) {  //iterate through database
// //     console.log(key)
// //     console.log(database[key]['name'])
// // }

// const myObject = { name: "Tom", age: 34}; //using objects and functions

// function increaseAge(obj) {
//     obj.age = obj.age + 1;
// }

// // increaseAge(myObject);
// // console.log(myObject)

// // IF ELSE STATEMENTS

// // if (3 > 5) {
// //     console.log("take a nap");
// // } else if (3 === 3) {
// //     console.log("groovy");
// // } else {
// //     console.log("Is this real life?");
// // };

// // TERNIARY STATEMENT  use if you can fit on one line and if only two possibilities.

// // let age = 18;
// // let drinkingAge = age >= 21 ? "Of drinking age" : "Designated driver"
// // console.log(drinkingAge);


// // LOOP THE LOOP

// // while, for of, for in, for i


// // WHILE LOOP
// // let number = 100;

// // while (number > 0) {
// //     console.log(number);
// //     number--;
// // }
// // console.log("end of while loop");

// //FOR i LOOP

// // for (let i = 10; i > 0; i--) {
// //     console.log(i)
// // }
// // console.log("blast off!")

// //FOR OF and FOR IN LOOP

// let myObj = {
//     "I": 1,
//     "II": 2,
//     "III": 3,
//     "IV": 4,
//     "V": 5
// }
// // FOR OF
// // for (item of Object.entries(myObj)) {
// //     console.log(item)
// // }


// let myString = 'slkfjjsdlkfjsdklfjsdfiofeklhfjkhklewhfweh';

// let letters = {};

// for (ltr of myString) {
//     if (letters[ltr]) {
//         letters[ltr] += 1;
//     }
//     else {
//         letters[ltr] = 1;
//     }
//     }
// console.log(letters)

// // FOR IN
// for (numeral in myObj) {
//     console.log(numeral)
// }


//DESTRUCTURING ////////////////////////////////////////
// let arrayOfLtrs = ['a', 'b', 'c', 'd', 'e']

// console.log(arrayOfLtrs[arrayOfLtrs.length-1])

// let {a, b, c} = {"a": 45, "b": 32, "c": 5}
// console.log(b)
// let [a, b, c] = [1, 2, 3]

// let {person1, person2} = {
//     person1: {
//         name: "Tom",
//         age: 34,
//     },
//     person2: {
//         name: "Sally",
//         age: 42,
//     },
// };
// console.log(person1)
// console.log(c)


