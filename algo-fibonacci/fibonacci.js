function fibonacci(num) {
  let fibArr = [0, 1];
  for (let i = 1; i <= num; i++) {
    fibArr.push(fibArr[fibArr.length - 1] + fibArr[fibArr.length - 2])
  }
  console.log(fibArr)

 return fibArr[num - 1]
}
console.log(fibonacci(10))

module.exports = fibonacci;
