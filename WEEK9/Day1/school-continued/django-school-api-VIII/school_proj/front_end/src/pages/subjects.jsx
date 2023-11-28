import Row from 'react-bootstrap/Row'
import axios from 'axios'
import {useState, useEffect } from 'react' 

export const Subjects = () => {
    const [subjects, setSubjects] = useState([])

    const getAllSubjects = async() =>{
        let response = await axios
        .get("http://127.0.0.1:8000/api/v1/subjects/")
        .catch((err) => {
            console.log(err);
            alert("something went wrong");
        });
        console.log(response.data)
        setSubjects(response.data);
    };
    useEffect(() => {
        getAllSubjects();

    }, []);

    return (
        <Row style = {{padding: "0 10vmin" }}>
            <h1 style={{ textAlign: "center" }}>Subjects</h1>
            <ul>
                {subjects.map((subject) => (
                    <li key={subject.id}
                    style= {{
                        margin: "3vmin",
                        display: "flex",
                        flexDirection: "column",
                    }}
                    >
                        Subject Name:{subject.subject_name} <br />
                        Professor: {subject.professor} <br />
                        Students: {subject.students} <br />
                        Average Grade: {subject.grade_average}
                    </li>
                ))}
            </ul>
        </Row>
    )


}