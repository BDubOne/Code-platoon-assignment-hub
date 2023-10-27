
//Reques EXAMPLE
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



