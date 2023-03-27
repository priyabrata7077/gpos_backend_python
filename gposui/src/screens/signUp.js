import React from 'react';
import {useState} from 'react';
import { useQuery } from 'react-query';
import { useNavigate } from 'react-router-dom';
import axios from 'axios'
import './signUp.css'
const SignInUi = () => {
    const [email , setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [apiResponse , setAPiResponse] = useState('')
    const navigate = useNavigate()
    
    const HandleAuth = async () => {
      const result = await axios.get(`http://127.0.0.1:8000/get-owner?userEmail=${email}&pass=${password}` , {} ).then((res) => {
            if (res['data'][0]){
                        if (res['data'][0] === 'auth failed'){
                            console.log('Wrong Credentials Bro')
                            console.log(`${email} -------- ${password}`)}
                        if (res['data'] === 'invalid input'){
                            console.log('Dont leave the boxes blank')
                            console.log(`${email} -------- ${password}`)}
                        if (res['data'] === 'no user'){
                            console.log('Gmail not in database -> ')
                            console.log(`${email} -------- ${password}`)}}
            if (res['data']['name']){
                    console.log('Got a hit bro')}

                }).catch((err) => console.log(err))}
    
    return (
        <>
            <div className='signup-container'>
                <span>SIGN IN</span>
                <input className='email-input' placeholder='Enter Your Registered Email' type="email" onChange={(event) => setEmail(event.target.value)} />
                <input className='pass-input' placeholder='Enter Your Password' type='password' onChange={(event) => setPassword(event.target.value)} />
                <button onClick={ () => HandleAuth()} >Sign In</button>
                <h2>Dont Have an account ? </h2>
                <button onClick={() => navigate('/register-owner')} >Sign Up</button>
            </div>
        </>
    )

    

}


export default SignInUi