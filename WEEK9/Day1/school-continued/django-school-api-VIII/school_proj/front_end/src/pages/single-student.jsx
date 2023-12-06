
import Card from 'react-bootstrap/Card'
import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import axios from 'axios'
import { EditSingleStudent } from './edit-single-student'


export const SingleStudent = () => {
    const [singleStudent, setSingleStudent] = useState([]);
    const { id } = useParams();
    const [initialData, setInitialData] = useState({})

    const getSingleStudent = async() => {
        try {
            let response = await axios
            .get(`http://127.0.0.1:8000/api/v1/students/${id}/`)
            const studentData = response.data


    
            const editData = {
                name: studentData.name,
                student_email: studentData.student_email,
                personal_email: studentData.personal_email,
                locker_number: studentData.locker_number,
                locker_combination: studentData.locker_combination,
                good_student: studentData.good_student,
                subjects: studentData.subjects || {}, // Handle the subjects data, or provide an empty object as a default
           
        };
        setSingleStudent(studentData)
        setInitialData(editData)
        console.log(studentData)
        console.log(editData)

          

        // Set the initial data in the state
         
        }  catch(err) {
            alert('something went wrong');
        };

      
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
                 <Link to={`edit/?initialData=${encodeURIComponent(JSON.stringify(initialData))}`}>
                    <button>Edit</button></Link>
            </Card.Body>
            <EditSingleStudent initialData={initialData} />
        </Card>
    )


}