import { useEffect, useState } from 'react';
import { Link, Navigate, Route, Routes, useNavigate } from "react-router-dom";


import './register.css'

const userProfileUrl = 'http://localhost:8080/api/userprofiles/'

function Register() {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')
    const [newProfile, setNewProfile] = useState([]);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const profile = { 
            user_name: username, 
            password, 
            user_email: email,
            target_language_id: {
                id: 1,
                language_name: "Spanish"
            },
            target_language: "Spanish",
            native_language: "English",
            active_cards: 0,
            words_learned: 0
        };
        setNewProfile([...newProfile, profile]);
        try {
            const response = await fetch(userProfileUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(profile)
            });
            
            if (response.ok) {
                const data = await response.json();
                console.log('Profile created successfully:', data);
                navigate('/login')
            } else {
                console.error('Failed to create profile:', response.statusText);
            }
        } catch (error) {
            console.error('Error creating profile:', error);
        }
    };


    return (  
        <>
            <div className="register-background">
                <div className="register-container">
                    <form onSubmit={handleSubmit}>
                        <h1>Create Profile</h1>
                        <div className="input-box">
                            <input 
                                type="text" 
                                placeholder='Create username'
                                value={username} 
                                onChange={(e) => setUsername(e.target.value)}
                                required/>
                        </div>
                        <div className="input-box">
                            <input 
                                type="text" 
                                placeholder='Create password' 
                                value={password} 
                                onChange={(e) => setPassword(e.target.value)}
                                required/>
                        </div>
                        <div className="input-box">
                            <input 
                                type="text" 
                                placeholder='Enter email'
                                value={email} 
                                onChange={(e) => setEmail(e.target.value)} 
                                required/>
                        </div>
                        <button className="login" type="submit">Create</button>
                    </form>
                </div>
            </div>
        </>
    );
}

export default Register;