// // headerValue = document.getElementById("headerTitle");
// // console.log(headerValue.innerHTML)
// // console.log("good morning")
// const dog = "https://dogtime.com/wp-content/uploads/sites/12/2011/01/GettyImages-653001154-e1691965000531.jpg?w=1024"

// const fire = "https://media.npr.org/assets/img/2023/01/14/this-is-fine_custom-dcb93e90c4e1548ffb16978a5a8d182270c872a9-s1100-c50.jpg"

// const showName = () =>{
//     let nameInput = document.getElementById("input-name").value
//     let parent = document.getElementById("output")
//     output.innerText = `Hello ${nameInput}`
//     let img = document.createElement("img")
//     if (nameInput === 'dog') {
//         img.src = dog
//     } else{
//         img.src = fire;
//         }

//     }
// console.log(showName())
const favoriteColor = (event) => {
    event.preventDefault()
    const formData = new FormData(event.target)
    const formatData = Object.fromEntries(formData)
    console.log(formatData)
    output.innerText = `${formatData.name}'s favorite color is ${formatData.color}`
}

const changeColor = (event) =>{
    event.target
}
let box = document.getElementById("box")
box.addEventListener("mouseover", (event) => {
    event.target.style.backgroundColor = 'cyan'
})
box.addEventListener("mouseout", (event) => {
    event.target.style.backgroundColor = 'white'
})

// document.getElementsByClassName('div')
// document.querySelector('div')
// document.querySelectorAll('a')
