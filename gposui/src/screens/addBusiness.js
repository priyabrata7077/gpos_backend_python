import React from "react";
import { useState } from "react";
import {useNavigate} from 'react-router-dom'

import './addOwner.css'


const AddBusinessUi = () => {
   
    const [Businessname ,setBusinessName] = useState('')
    const [Businessemail , setBusinessEmail] = useState('')
    const [Businesscontact , setBusinessContact] = useState('')
    const [Businesswhatsapp , setBusinessWhatsapp] = useState('')
    const [Businessaddress , setBusinessAddress] = useState('')
    const [Businesscity , setBusinessCity] = useState('')
    const [Businesspincode , setBusinessPincode] = useState(0)
    const [Businesscountry , setBusinessCountry] = useState('')
    const [Businesspan , setBusinessPan] = useState('')
    
    const Businesscurrentdate = new Date()
    const handleClick = () => {
        
        console.log('Hey Yo ')
        
    }

    return (
        <>
        
        <div className = 'main-container'>
        <h2 styles = {{alignSelf : 'center'}}>Register Your Business</h2>
            <input className='Owners-Input' placeholder='Your Name Again' onChange={(event)=>{setBusinessName(event.target.value)}} />
            <input className='Owners-Input' placeholder='Your Business Email'  onChange={(event)=> {setBusinessEmail(event.target.value)}} />
            <input className='Owners-Input' placeholder='your Business contact' onChange={(event) => {setBusinessContact(event.target.value)}} />
            
            <input className='Owners-Input' placeholder=' your Business Address' onChange={(event) => {setBusinessAddress(event.target.value)}} />
            <input className='Owners-Input' placeholder='City' onChange={(event) => {setBusinessCity(event.target.value)}} />
            <input className='Owners-Input' placeholder='PIN Code' onChange={(event) => {setBusinessPincode(event.target.value)}} />
            <input className='Owners-Input' placeholder='Country' onChange={(event) => {setBusinessCountry(event.target.value)}} />
            <input className='Owners-Input' placeholder='Your Business PAN no.' onChange={(event) => {setBusinessPan(event.target.value)}} />
            <input className='Owners-Input' placeholder='Your Business GST no.' onChange={(event) => {setBusinessPan(event.target.value)}} />

            <button onClick={() => {handleClick()}} className='AddBusinessButton' >
                REGISTER BUSINESS
            </button>
        </div>
        </>
    )
}

export default AddBusinessUi;