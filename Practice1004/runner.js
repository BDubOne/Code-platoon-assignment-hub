const makeAName = require("./day3.js")

console.log(makeAName("Bryan", "Bartell"));

const addingTwos = require("./day3.js")
console.log(addingTwos(4));

const greetingWithName = (name) => {
    return `Hello ${name}`
}

module.exports = greetingWithName;
