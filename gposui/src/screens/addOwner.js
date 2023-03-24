import React from 'react'
import { useState } from 'react'
import './addOwner.css'
import { useNavigate } from 'react-router-dom'
import { useEffect } from 'react'
const AddOwnerUi = () => {
    const navigation = useNavigate()
    const [name ,setName] = useState('')
    const [email , setEmail] = useState('')
    const [contact , setContact] = useState('')
    const [whatsapp , setWhatsapp] = useState('')
    const [address , setAddress] = useState('')
    const [city , setCity] = useState('')
    const [pincode , setPincode] = useState(0)
    const [country , setCountry] = useState('')
    const [pan , setPan] = useState('')
    const [password , setPassword] = useState('')

    const [ownerID , setOwnerID] = useState('')

            
        
   
    const currentdate = new Date()
    const Date_data_in_proper_format = currentdate.toLocaleDateString('en-CA' , {year:'numeric', month:'2-digit', day:'2-digit'}).replace(/\//g , '-')
    const data =     {
        
        "name": name,
        "email": email,
        "password": password,
        "contact_number": contact,
        "whatsapp_number": whatsapp,
        "address": address,
        "city": city,
        "pin": parseInt(pincode),
        "country": country,
        "pan_card_number": pan,
        "date_of_entry": Date_data_in_proper_format }
    
    const api_post_data = JSON.stringify(data)
    const handleClick = () => {

        console.log( `${typeof name} ${typeof email} ${typeof contact} ${typeof whatsapp}
        ${typeof address} ${typeof city} ${typeof pincode} ${typeof country} ${typeof pan} ${typeof Date_data_in_proper_format} `) 
        
        fetch('http://127.0.0.1:8000/add-owner' , {
            method:'POST',
            body:api_post_data,
            headers:{
                'Content-type':'application/json'
            }
        }).then(response => response.json()).then(data => {console.log(`${data.id} - ${typeof data.id}`)
                                                            setOwnerID(data)    
                                                        }).catch(error => {
            console.error(error);
        })
        
        navigation('/register-business')
        }
    
    return (
        <>
        
        <div className = 'main-container'>
        <h2 styles = {{alignSelf : 'center'}}>Lets Proceed With Your Personal Details</h2>
            <input className='Owners-Input' placeholder='Your Name' onChange={(event)=>{setName(event.target.value)}} />
            <input className='Owners-Input' placeholder='Your Email'  onChange={(event)=> {setEmail(event.target.value)}} />
            <input className='Owners-Input' placeholder='your contact number' onChange={(event) => {setContact(event.target.value)}} />
            <input className='Owners-Input' placeholder='your whatsapp number' onChange={(event) => {setWhatsapp(event.target.value)}} />
            <input className='Owners-Input' placeholder=' your full Address' onChange={(event) => {setAddress(event.target.value)}} />
            <input className='Owners-Input' placeholder='City' onChange={(event) => {setCity(event.target.value)}} />
            <input className='Owners-Input' placeholder='PIN Code' onChange={(event) => {setPincode(event.target.value)}} />
            <input className='Owners-Input' placeholder='Country' onChange={(event) => {setCountry(event.target.value)}} />
            <input className='Owners-Input' placeholder='Your Pan Card Number' onChange={(event) => {setPan(event.target.value)}} />
            <input className='Owners-Input' placeholder='Password' type='password' onChange={(event) => {setPassword(event.target.value)}} />
            <button onClick={() => {handleClick()}} className='AddOwnerButton' >REGISTER</button>
        </div>
        </>
    )
}



export default AddOwnerUi