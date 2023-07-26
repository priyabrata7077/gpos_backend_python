import React, { useState, useEffect } from "react";
import Button from "@mui/material/Button";
import axios from "axios";
import { useParams } from 'react-router-dom';

function EditEmployee() {
  const { id } = useParams();
  console.log("ID:", id);
  const [employeeData, setEmployeeData] = useState({
    name: "",
    email: "",
    phone: "",
    address: "",
    adhaar: ""
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchEmployeeData = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/business/employee/update/${id}`);
        setEmployeeData(response.data);
        setLoading(false);
      } catch (error) {
        setError(error.message);
        setLoading(false);
      }
    };
    fetchEmployeeData();
  }, [id]);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setEmployeeData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const employeeData = {
      name: formData.get("name"),
      email: formData.get("email"),
      phone: formData.get("phone"),
      address: formData.get("address"),
      adhaar: formData.get("adhaar"),
    };

    const url = `http://127.0.0.1:8000/business/employee/update/${id}`;

    axios
      .put(url, employeeData) // Use axios.put for updating data
      .then((response) => {
        console.log(response.data);
        // Handle successful response or perform any actions after successful update
      })
      .catch((error) => {
        console.error(error);
        // Handle error or display an error message to the user
      });
  };

  return (
    <div>
      <h1>Edit Employee</h1>
      <form className="row pt-3" action="/employee_mas" onSubmit={handleSubmit} method="POST">
        
        <div className="col-6 mb-3">   
          <label htmlFor="name">Name</label>
          <input type="text" className="form-control" id="name" name="name" onChange={handleChange} value={employeeData.name} autoComplete="name" required/>
        </div>
        <div className="col-6 mb-3">
          <label htmlFor="email">Email</label>
          <input type="email" className="form-control" id="email"  name="email" onChange={handleChange} value={employeeData.email} autoComplete="email" required/>
        </div>
        <div className="col-6 mb-3">
          <label htmlFor="phone">Phone</label>
          <input type="numtexter" className="form-control" id="phone" name="phone" onChange={handleChange} value={employeeData.phone} autoComplete="phone" required/>
        </div>
        <div className="col-6 mb-3">
          <label htmlFor="address">Address</label>
          <input type="text" className="form-control" id="address" name="address" onChange={handleChange} value={employeeData.address} autoComplete="address" required/>
        </div>
      
        <div className="col-6 mb-3">
          <label htmlFor="adhaar">Aadhar Number</label>
          <input type="text" className="form-control" id="adhaar" name="adhaar" onChange={handleChange} value={employeeData.adhaar} autoComplete="adhaar" required/>
        </div>
        {/*<div className="col-6 mb-3">
          <label htmlFor="business">Business</label>
          <input type="text" className="form-control" id="business" name="business" onChange={handleChange} value={addemployee.business} required/>
        </div>*/}
  
        <button><a
          href="/dashboard/employee_master"
          to={`/employee/${id}`} // Replace with the appropriate route path to go back
          variant="contained"
          color="primary"
        >
          Back</a>
        </button>
        <Button type="submit" variant="contained" color="primary">
          Update
        </Button>
        </form>
    </div>
  ); 
}

export default EditEmployee;