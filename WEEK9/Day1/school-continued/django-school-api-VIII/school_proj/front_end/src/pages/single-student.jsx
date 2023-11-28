import Row from 'react-bootstrap/Row'
import Card from 'react-bootstrap/Card'
import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

export const SingleStudent = () => {
    const [singleStudent, setSingleStudent] = useState([]);
    const { id } = useParams();

    const getSingleStudent = async() => {
        let response = await axios
        .get(`http://127.0.0.1:8000/api/v1/students/${id}/`)
        .catch((err) =>{
            alert('something went wrong');
        });
        console.log(response.data)
        setSingleStudent(response.data)
    };
    useEffect(() => {
        getSingleStudent();
    }, [])

    return (
        <Card style = {{ width: '18rem' }}>
            <Card.Body>
                <Card.Title>
            {singleStudent.name}
                </Card.Title>
                <Card.Text>
                    Personal Email: {singleStudent.personal_email}
                    <br />
                    Student Email: {singleStudent.student_email}
                    <br />
                    Locker Number: {singleStudent.locker_number}
                    <br />              

                </Card.Text>
            </Card.Body>
        </Card>
    )


}