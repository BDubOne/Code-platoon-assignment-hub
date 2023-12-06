import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom'
import Row from 'react-bootstrap/esm/Row';
import axios from 'axios'


export const RegisterPage = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const navigate = useNavigate();

    const SignUp = async (e) => {
        e.preventDefault();
        const data = { email, password };
        const response = await axios.post('http://127.0.0.1:8000/api/v1/users/signup/', data)
        .catch(err =>console.log(`signup err ${err}`));
        const trainerEmail = response.data.trainer;
        const token = response.data.token;

        console.log(`signup success, email; ${trainerEmail}, token: ${token}`);

        
        localStorage.setItem("token", token);
        localStorage.setItem("email", trainerEmail)
        navigate('/');


    }

    useEffect(() => {
        SignUp()
    },[])

    return (

        <>
        <form onSubmit = {(e)=>SignUp(e)}>
            <h2>create a user</h2>
            <input type="text" placeholder="email" />
            <input type="text" placeholder="password" />
            <button type="submit">Submit</button>
        </form>
        
        </>
    )
}