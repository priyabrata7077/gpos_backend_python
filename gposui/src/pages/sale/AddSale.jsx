import React,{useState} from 'react'
import styles from './sale.module.css'
import { Link } from 'react-router-dom'
import Button from "@mui/material/Button";
import axios from 'axios';


function AddSale() {
  const [saleData, setSaledata] = useState({
    id:"",
    qty: "",
    purchase_rate: "",
    mrp: "",
    sale_rate:"",
    sub_total:"",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setSaledata((prevProps) => ({
      ...prevProps,
      [name]: value
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Send the sale data to the API
    axios.post('http://127.0.0.1:8000/sales', saleData)
      .then((response) => {
        console.log('Sale data sent successfully:', response.data);
        // Add any further actions you want to perform after successful data submission.
      })
      .catch((error) => {
        console.error('Error submitting sale data:', error);
        // Handle any error responses from the API here.
      });
  };
  return (
    <div className={styles.main}>
    <div className={styles.Pagetitle}>
      <h1>Add Sale</h1>
    </div>

    <div className={styles.cardContainer}>
      <h6>Sale Details</h6>
      <form className="row pt-3" >
        <div className="col-4 mb-3">
          <label htmlFor="id">Bill ID</label>
          <input type="number" className="form-control"  name="id" onChange={handleChange} value={saleData.id}/>
        </div>
        <div className="col-4 mb-3">
          <label htmlFor="qty">Quantity</label>
          <input type="number" className="form-control"  name="qty" onChange={handleChange} value={saleData.qty}/>
        </div>
        <div className="col-4 mb-3">
          <label htmlFor="purchase_rate">Purchase Rate</label>
          <input type="number" className="form-control"  name="purchase_rate" onChange={handleChange} value={saleData.purchase_rate}/>
        </div>
         
        <div className="col-4 mb-3">
          <label htmlFor="mrp">MRP</label>
          <input type="number" className="form-control"  name="mrp" onChange={handleChange} value={saleData.mrp}/>
        </div>
        <div className="col-4 mb-3">
          <label htmlFor="sale_rate">Sale Rate</label>
          <input type="number" className="form-control"  name="sale_rate" onChange={handleChange} value={saleData.sale_rate}/>
        </div>
        <div className="col-4 mb-3">
          <label htmlFor="sub_total">Total</label>
          <input type="number" className="form-control"  name="sub_total" onChange={handleChange} value={saleData.sub_total}/>
        </div>
        
      

 
      

        <div className={styles.btn}>
          
            <Button variant="contained" className={styles.btn} type="submit" onClick={handleSubmit}>
              Save
            </Button>
          
        </div>
      </form>
    </div>
  </div>
  )
}

export default AddSale
