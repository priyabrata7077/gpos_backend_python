import React, { useState } from "react";
import styles from "./people.module.css";
import Button from "@mui/material/Button";
import { Link } from "react-router-dom";
import axios from "axios";

function AddEmployee() {
  
  const [addemployee, setAddEmployee] = useState({
    name: '',
    email: '',
    phone: '',
    address: '',
    adhaar: '',
  
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setAddEmployee((prevaddemployee) => ({
      ...prevaddemployee,
      [name]: value,
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const url = 'http://127.0.0.1:8000/business/employee/add'; // Replace with your API endpoint URL

    axios
      .post(url, addemployee)
      .then((response) => {
        console.log(response.data);
        // Handle successful response
      })
      .catch((error) => {
        console.error(error);
        // Handle error
      });
  };



  return (
    <div className={styles.main}>
    <div className={styles.Pagetitle}>
      <h1>Add Employee</h1>
    </div>
   
    

    <div className={styles.cardContainer}>
    <div>
    <button><a
          href="/dashboard/employee_master"
          // Replace with the appropriate route path to go back
          variant="contained"
          color="primary"
        >
          Back</a>
        </button>
    </div>
      <h6>Employee Details</h6>
      <form className="row pt-3" action="/employee_mas" onSubmit={handleSubmit} method="POST">
        
        <div className="col-6 mb-3">   
          <label htmlFor="name">Name</label>
          <input type="text" className="form-control" id="name" name="name" onChange={handleChange} value={addemployee.name} autoComplete="name" required/>
        </div>
        <div className="col-6 mb-3">
          <label htmlFor="email">Email</label>
          <input type="email" className="form-control" id="email"  name="email" onChange={handleChange} value={addemployee.email} autoComplete="email" required/>
        </div>
        <div className="col-6 mb-3">
          <label htmlFor="phone">Phone</label>
          <input type="numtexter" className="form-control" id="phone" name="phone" onChange={handleChange} value={addemployee.phone} autoComplete="phone" required/>
        </div>
        <div className="col-6 mb-3">
          <label htmlFor="address">Address</label>
          <input type="text" className="form-control" id="address" name="address" onChange={handleChange} value={addemployee.address} autoComplete="address" required/>
        </div>
      
        <div className="col-6 mb-3">
          <label htmlFor="adhaar">Aadhar Number</label>
          <input type="text" className="form-control" id="adhaar" name="adhaar" onChange={handleChange} value={addemployee.adhaar} autoComplete="adhaar" required/>
        </div>
        {/*<div className="col-6 mb-3">
          <label htmlFor="business">Business</label>
          <input type="text" className="form-control" id="business" name="business" onChange={handleChange} value={addemployee.business} required/>
        </div>*/}
    
 
      

        <div className={styles.btn}>
        <button type="submit">
              Save
            </button>
          {/* <Link to="../summary">
          
          </Link> */}
        </div>
      </form>
    </div>
  </div>
  )
}

export default AddEmployee
