function factorial(num) {
let factResult = 1;
  for (let i = num; i > 0; i--) {
    factResult *= i
  }
 
  return factResult;
}

module.exports = factorial;
