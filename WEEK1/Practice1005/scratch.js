
//while trailing commas is necessary in python, it is not in javascript. 
//does not work in JSON
const foods = {
    beans: 'gross',
    donuts: 'yummy',
    candy: 'yummy',
}

console.log(foods)
//using functions as first class objects


const sayHello = function(name) {
    console.log('extra special hello ' + name)
}

function sayHelloWithExtra(name, helloFunction) {
        console.log('hello ' + name)
        helloFunction(name)
    }
    sayHelloWithExtra("Bryan", sayHello)
