const sendARequest = () => {
    let request = (method = 'POST', endpoint ="app/students", data= {
        'first_name': 'Bryan',
        'last_name': 'Bartell',
        'age': 37,
        'subject': 3

    })
    let request2 =(
        method = 'POST',
        endpoint = 'app/students?first_name=Bryan&last_name=Bartell&age=37&subject=3',
        data= {

        } 
        )
}