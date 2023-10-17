// const addingTwos = require("./day3.js")

// describe("Writing  simple addition test", () => {
//     test ( "testing addingTwos to ensure it works properly", () =>{
//         expect(addingTwos(4)).toBe(6)
//     })
// })

// describe("Checking a name function", () => {
// test("makeAName function with two parameters", ()=>{
//     const makeAName = (first, last) => {
//         return `${first} ${last}`
//     }
//     expect(makeAName("Bryan", "Bartell")).toBe("Bryan Bartell")
// })
// })
const greetingWithName = require("./runner.js")

describe("greetingWithName being tested", () => {
    test("greetingWithName appearing correctly", () => {
        expect(greetingWithName("Bryan")).not.toBe("Hello Bryan")
    })
})