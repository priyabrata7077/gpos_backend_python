import React, { useState } from "react";
import styles from "./business.module.css";
import Button from "@mui/material/Button";
import { Link } from "react-router-dom";
import axios from "axios";


function AddBusiness() {
  const [data, setData] = useState({
    name: "",
    email: "",
    phone: "",
    city: "",
    address: "",
    pin: "",
    gst_number: "",
    state: "",
    country: "",
    pan: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
  
    const url = "http://127.0.0.1:8000/add-business";
    axios
      .post(url, data)
      .then((response) => {
        // Handle successful response
        console.log("Response data:", response.data); // Log the response data to the console
        // You can update the state or perform any other actions with the data here
      })
      .catch((error) => {
        // Handle error
        console.error("Error:", error);       
      });
  };


  return (
    <div className={styles.main}>
      <div className={styles.Pagetitle}>
        <h1>Add Business</h1>
      </div>

      <div className={styles.cardContainer}>
        <h6>Business Details</h6>
        <form className="row pt-3" onSubmit={handleSubmit} method="POST">
          <div className="col-6 mb-3">
            <label htmlFor="name">Name</label>
            <input type="text" className="form-control" id="name" name="name" onChange={handleChange} value={data.name}/>
          </div>
          <div className="col-6 mb-3">
            <label htmlFor="email">Email</label>
            <input type="email" className="form-control" id="email" name="email" onChange={handleChange} value={data.email}/>
          </div>
          <div className="col-4 mb-3">
            <label htmlFor="phone">Phone</label>
            <input type="text" className="form-control" id="phone" name="phone" onChange={handleChange} value={data.phone}/>
          </div>
          <div className="col-4 mb-3">
            <label htmlFor="address">Address</label>
            <input type="text" className="form-control" id="address" name="address" onChange={handleChange} value={data.address}/>
          </div>
          <div className="col-4 mb-3">
            <label htmlFor="city">City</label>
            <input type="text" className="form-control" id="city" name="city" onChange={handleChange} value={data.city}/>
          </div>
          <div className="col-4 mb-3">
            <label htmlFor="state">State</label>
            <input type="text" className="form-control" id="state" name="state" onChange={handleChange} value={data.state}/>
          </div>

          <div className="col-4 mb-3">
            <label htmlFor="country">Country</label>
            <input type="text" className="form-control" id="country" name="country" onChange={handleChange} value={data.country}/>
          </div>

          <div className="col-4 mb-3">
            <label htmlFor="pin">Pincode</label>
            <input type="text" className="form-control" id="pin" name="pin" onChange={handleChange} value={data.pin}/>
          </div>

          <div className="col-4 mb-3">
            <label htmlFor="pan">Pan Card</label>
            <input type="text" className="form-control" id="pan" name="pan" onChange={handleChange} value={data.pan}/>
          </div>
          <div className="col-4 mb-3">
            <label htmlFor="gst_number">Gst Number</label>
            <input type="text" className="form-control" id="gst_number" name="gst_number" onChange={handleChange} value={data.gst_number}/>
          </div>
        

          <div className={styles.btn}>
            
            <button type="submit" className={styles.btn}>
              Save
            </button>
            
          </div>
        </form>
      </div>
    </div>
  );
}

export default AddBusiness;
