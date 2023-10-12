const factorial = require("./factorial.js");
describe("test factorial", () => {
    test("factorial(1) === 1", () => {
      expect(factorial(1)).toBe(1);
    });
  
    test("factorial(2) === 2", () => {
      expect(factorial(2)).toBe(2);
    });
  
    test("factorial(3) === 6", () => {
      expect(fibonacci(3)).toBe(6);
    });
  });
  
console.log(factorial(0) === 1);
console.log(factorial(1) === 1);
console.log(factorial(2) === 2);
console.log(factorial(4) === 24);
console.log(factorial(8) === 40320);
console.log(factorial(18) === 6402373705728000);
// Test how high of a number your program can calculate. Can you push it further?
