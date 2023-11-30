import Row from 'react-bootstrap/Row'
import { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom'

import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import ListGroupItem from 'react-bootstrap/ListGroupItem';

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
        <>
        {students.map((student) => (
            <Card key={student.id} style={{ margin: '1rem' }}>
                <Card.Body>
                    <Card.Title>
                    <Link to={`${student.id}/`}>{student.name}</Link>
                    </Card.Title>
                    <Card.Subtitle className="mb-2 text-muted">Student ID: {student.id}</Card.Subtitle>
                    <ListGroup className="list-group-flush">
                        <ListGroupItem>Student Email: {student.student_email}</ListGroupItem>
                        <ListGroupItem>Good Student: {student.good_student ? 'Yes' : 'No'}</ListGroupItem>
                        <ListGroupItem>
                            Subjects:
                            <ul>
                                {Object.entries(student.subjects).map(([subjectName, grade]) => (
                                    <li key={subjectName}>
                                        {subjectName}: {grade}
                                    </li>
                                ))}
                            </ul>
                        </ListGroupItem>
                    </ListGroup>
                </Card.Body>
            </Card>
        ))}
        </>
        
    )


}