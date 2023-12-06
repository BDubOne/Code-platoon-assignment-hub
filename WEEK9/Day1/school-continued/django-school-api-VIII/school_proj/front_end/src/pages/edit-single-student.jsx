import React, { useState, useEffect } from 'react';
import { useParams, useLocation } from 'react-router-dom';
import axios from 'axios';

export const EditSingleStudent = ({ initialData }) => {
    const { id } = useParams();
    const [formData, setFormData] = useState(initialData || {});
    // const location = useLocation();
    // const queryParams = new URLSearchParams(location.search)
    // const initialData = JSON.parse(queryParams.get('initialData'))
    

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;

        // Use the type of the input to determine how to update the formData
        setFormData((prevData) => ({
            ...prevData,
            [name]: type === 'checkbox' ? checked : value,
            
        }));
      
    };
    console.log(initialData)

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
                        value={formData.name || ''}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Student Email:</label>
                    <input
                        type="email"
                        name="student_email"
                        value={formData.student_email || ''}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Personal Email:</label>
                    <input
                        type="email"
                        name="personal_email"
                        value={formData.personal_email || ''}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Locker Number:</label>
                    <input
                        type="integer"
                        name="locker_number"
                        value={formData.locker_number || ''}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Locker Combination:</label>
                    <input
                        type="text"
                        name="locker_combination"
                        value={formData.locker_combination || ''}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Good Student:</label>
                    <input
                        type="checkbox"
                        name="good_student"
                        checked={formData.good_student || false}
                        onChange={handleChange}
                    />
                </div>
                <button type="submit">Update</button>
            </form>
        </div>
    );
};
