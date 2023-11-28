import Row from 'react-bootstrap/Row'
import Card from 'react-bootstrap/Card'
import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

export const SingleSubject = () => {
    const [singleSubject, setSingleSubject] = useState([]);
    const { id } = useParams();

    const getSingleSubject = async() => {
        let response = await axios
        .get(`http://127.0.0.1:8000/api/v1/Subjects/${name}/`)
        .catch((err) =>{
            alert('something went wrong');
        });
        console.log(response.data)
        setSingleSubject(response.data)
    };
    useEffect(() => {
        getSingleSubject();
    }, [])

    return (
        <Card style = {{ width: '18rem' }}>
            <Card.Body>
                <Card.Title>
            {singleSubject.subject_name}
                </Card.Title>
                <Card.Text>
                   Professor: {singleSubject.professor}
                    <br />
                </Card.Text>
            </Card.Body>
        </Card>
    )


}