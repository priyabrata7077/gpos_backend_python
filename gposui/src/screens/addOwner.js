import React from 'react'
import { useState } from 'react'
import './addOwner.css'


const AddOwnerUi = () => {
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
    const currentdate = new Date()

    const data =     {
        "id": 1,
        
        "name": name,
        "email": email,
        "password": password,
        "contact_number": contact,
        "whatsapp_number": whatsapp,
        "address": address,
        "city": city,
        "pin": pincode,
        "country": country,
        "pan_card_number": pan,
        "date_of_entry": currentdate.toDateString() }
    

    const handleClick = () => {
        console.log( `${name} ${email}${contact})${whatsapp}
        ${address} ${city} ${pincode} ${country} ${pan} ${currentdate.toDateString()} `) }

    return (
        <>
        
        <div className = 'main-container'>
        <h2 styles = {{alignSelf : 'center'}}>Enter Your Personal Details Bro</h2>
            <input placeholder='Your Name' onChange={(event)=>{setName(event.target.value)}} />
            <input placeholder='Your Email'  onChange={(event)=> {setEmail(event.target.value)}} />
            <input placeholder='your contact number' onChange={(event) => {setContact(event.target.value)}} />
            <input placeholder='your whatsapp number' onChange={(event) => {setWhatsapp(event.target.value)}} />
            <input placeholder=' your full Address' onChange={(event) => {setAddress(event.target.value)}} />
            <input placeholder='City' onChange={(event) => {setCity(event.target.value)}} />
            <input placeholder='PIN Code' onChange={(event) => {setPincode(event.target.value)}} />
            <input placeholder='Country' onChange={(event) => {setCountry(event.target.value)}} />
            <input placeholder='Your Pan Card Number' onChange={(event) => {setPan(event.target.value)}} />
            <button onClick={() => handleClick()} className='AddOwnerButton' >REGISTER</button>
        </div>
        </>
    )
}



export default AddOwnerUi