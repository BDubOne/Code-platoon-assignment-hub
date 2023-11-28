import Row from 'react-bootstrap/Row'
import { useEffect, useState } from 'react';
import axios from 'axios';

export const Students = () => {

    const [students, setStudents] = useState([]);

    const getAllStudents = async() => {
        let response = await axios
        .get("http://127.0.0.1:8000/api/v1/students/")
        .catch((err) =>{
            console.log(err);
            alert('something went wrong');
        });
        console.log(response.data)
        setStudents(response.data)
    };
    useEffect(() =>{
        getAllStudents();
    }, []);

    return (
        <Row style={{padding: "0 10vmin"}}>
            <h1 style = {{ textAlign: "center"}}> Students</h1>
            <ul>
                {students.map((student)=> (
                    <li key={student.id}
                    style={{
                        margin: "3vmin",
                        display: "flex",
                        flexDirection: "column",
                    }}
                    >
                        Id: {student.id} <br /> Name:{student.name} <br /> Student Email: {student.student_email}
                        <ul>
                        
                            {student.subjects.map((subject, idx) => (
                                <li key= {`${student.id}${idx}`}
                                style={{
                                    margin: "3vmin",
                                    display: "flex",
                                    flexDirection: "column",
                                }}
                                >{subject.subject_name}</li>
                            ))}
                        </ul>
                    </li>
                    ))}
            </ul>
        </Row>
    )


}