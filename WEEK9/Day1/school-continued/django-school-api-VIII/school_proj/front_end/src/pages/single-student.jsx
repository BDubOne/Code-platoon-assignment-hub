
import Card from 'react-bootstrap/Card'
import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
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

    const handleDelete = async ()=> {
        try {
            await axios.delete(`http://127.0.0.1:8000/api/v1/students/${id}/`);
            alert(`Student with ID ${id} has been deleted`);
        } catch (err) {
            console.log(err);
            alert('could not delete student')
        }
    };

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
                    Good Student: {singleStudent.good_student ? "Yes" : "No"}
                    <br />
                    <ul>
                        {Object.entries(singleStudent.subjects || {}).map(([subjectName, grade]) => (
                            <li key={subjectName}>
                                {subjectName}: {grade}
                            </li>
                        ))}
                    </ul>

                </Card.Text>
                <button onClick={handleDelete}>Delete</button>
                 <Link to="edit/">Edit</Link>
            </Card.Body>
        </Card>
    )


}