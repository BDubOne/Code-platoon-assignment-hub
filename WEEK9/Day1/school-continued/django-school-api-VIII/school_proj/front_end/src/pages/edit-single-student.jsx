import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';


export const EditSingleStudent = () => {
    const { id } = useParams();

    const [student, setStudent] = useState({});
    const [formData, setFormData] = useState({
        name: '',
        student_email: '',
        personal_email: '',
        locker_number: '',
        locker_combination: '',

    });

    const getSingleStudent = async () => {
        try {
            response = await axios
            .get(`http://127.0.0.1:8000/api/v1/students/${id}/`)
            setStudent(response.data);
            setFormData({
                name: response.data.name,
                student_email: response.data.student_email,
                personal_email: response.data.personal_email,
                locker_number: response.data.locker_number,
                locker_combination: response.data.locker_combination,
                good_student: response.data.good_student
            });
        } catch (err) {
            console.log(err);
            alert('oops');
        }
    };
    useEffect(() => {
        getSingleStudent();

    }, [id]);
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    } ;
   
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.put(`http://127.0.0.1:8000/api/v1/students/${id}/`, formData);
            alert('Student updated successfully');
        } catch (err) {
            console.log(err);
            alert('Failed to update student');
        }
    };
    
    return (
        <div>
            <h1>Edit Student</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Name:</label>
                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Student Email:</label>
                    <input
                        type="email"
                        name="student_email"
                        value={formData.student_email}
                        onChange={handleChange}
                    />
                </div>
                {/* Add more form fields for other attributes */}
                <button type="submit">Update</button>
            </form>
        </div>
    );
};
