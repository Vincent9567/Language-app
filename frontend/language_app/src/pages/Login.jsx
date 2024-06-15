import { useEffect, useState } from "react";
import { FaUser, FaLock  } from "react-icons/fa";
import { Link, Route, Routes, useNavigate } from "react-router-dom";
import './login.css'

const userProfileUrlBase = 'http://localhost:8080/api/userprofiles/';

function Login() {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    
    const navigate = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault();
        const userProfileUrl = `${userProfileUrlBase}${username}`
        
        try {
            const response = await fetch(userProfileUrl, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (response.ok) {
                const data = await response.json();
                console.log('User profile data:', data);
              
                if (data.password === password) {
                    console.log('Login successful');
                    navigate('/home'); // Replace with your actual dashboard route
                } else {
                    console.error('Incorrect password');
                    alert('Incorrect password');
                }
            } else {
                console.error('User not found');
                alert('User not found');
            }
        } catch (error) {
            console.error('Error fetching user profile:', error);
        }
    }


    return (  
    <>
        <div className="login-background">
            <div className="login-container">
                <form onSubmit={handleSubmit}>
                    <h1>Login</h1>
                    <div className="input-box">
                        <input 
                            type="text" 
                            placeholder="Username"
                            value={username} 
                            onChange={(e) => setUsername(e.target.value)} 
                            required/>
                        <FaUser className="icon" />
                    </div>
                    <div className="input-box">
                        <input 
                            type="text" 
                            placeholder="Password" 
                            value={password} 
                            onChange={(e) => setPassword(e.target.value)}
                            required/>
                        <FaLock className="icon" />
                    </div>
                    <div className="remember-forgot">
                        <label><input type="checkbox"/>Remember me</label>
                        <a href="#">Forgot Password?</a>
                    </div>

                    <button className="login" type="submit">Login</button>

                    <div className="register-link">
                        <p>Don't have an account?<Link to='/register'> Register</Link></p>
                    </div>
                </form>
            </div>
        </div>
    </>
);
}

export default Login;