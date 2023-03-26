import React from 'react';
import {useState} from 'react';
import { useQuery } from 'react-query';
import { useNavigate } from 'react-router-dom';
import axios from 'axios'

const SignInUi = () => {
    const [email , setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [apiResponse , setAPiResponse] = useState('')
    const navigate = useNavigate()
    
    const HandleAuth = () => {
      const result = fetch(`http://127.0.0.1:8000/get-owner?userEmail=${email}&pass=${password}` ,  {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      }).then((res) => res.json()).then((data) => {
      setAPiResponse(data)  
      console.log(apiResponse)}).catch((err) => console.log(err))
    }
    
    return (
        <>
            <div>
                <span>SIGN IN</span>
                <input placeholder='Enter Your Registered Email' type="email" onChange={(event) => setEmail(event.target.value)} />
                <input placeholder='Enter Your Password' type='password' onChange={(event) => setPassword(event.target.value)} />
                <button onClick={ () => HandleAuth()} >Sign In</button>
                <h2>Dont Have an account ? </h2>
                <button onClick={() => navigate('/register-owner')} >Sign Up</button>
            </div>
        </>
    )

    

}


export default SignInUi