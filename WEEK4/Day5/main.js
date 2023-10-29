
//Request  EXAMPLE
const sendARequest = () => {
    let request = (method = 'POST', endpoint ="app/students", data= {
        'first_name': 'Bryan',
        'last_name': 'Bartell',
        'age': 37,
        'subject': 3

    })

//Same thing, but less secure and messier
    let request2 =(
        method = 'POST',
        endpoint = 'app/students?first_name=Bryan&last_name=Bartell&age=99&subject=3',
        data= {

        } 
        )
}


const getStudents = async() => {
    let response = await fetch('http://127.0.0.1:5000/students')
    let data = await response.json()

    let ul = document.getElementById("student-list")

    for (student of data) {     
        let li = document.createElement('li')
        li.innerText = `Student Name: ${student.first_name} ${student.last_name}`
        ul.appendChild(li)
  
    }
    
}
    // .then((response) => {
    //     return response.json()
        // console.log(response.data)
    // })
    // .then((data) => {
    //     console.log(data)
    // })

getStudents()
console.log("connection made")