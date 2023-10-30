//Import statements vs. require
// const tasks = require('./tasks.json')
import tasks from './tasks.json' assert {type:"json"};
import axios from 'axios';

// axios.get("https://pokeapi.co/api/v2/pokemon/ditto")
//     .then((resp)=>{
//         console.log(resp.data.sprites.front_default)
//     })
//     .catch((err)=>{
//         if (err.message) 
//         console.log('something went wrong')
//         // console.log("something went wrong", err)
//     })
const getPokemon = async() => {
    try{
        let response = await axios.get("https://pokeapi.co/api/v2/pokemon/ditto")
        console.log(response.data.sprites)
    }
    catch (err){
        console.log(err.message)
    }
}
getPokemon()


// for (let task of tasks) {
//     console.log(task)
// }

// let taskTitles = tasks.map(({id, task, completed}) => {
//    return task
// })
// console.log(taskTitles)

// let nums = [1,2,3,4,5,6,7,8]

// let oddNumbers = nums.map((num) => {
//     if (num % 2 !== 0) {
//         return num
//     }
//     return;
// })
// console.log(oddNumbers)

// nums.map((num, idx) => {
// // console.log(idx + ":", num + 2)
// // })

// let completedTasks = tasks.filter(({task, id, completed}) => {
//     return completed;
// })
// console.log(completedTasks)

