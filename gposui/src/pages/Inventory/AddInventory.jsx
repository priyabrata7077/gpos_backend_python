import React from 'react'
import styles from './inventory.module.css'
import { Link } from 'react-router-dom'
import Button from "@mui/material/Button";
function AddInventory() {
  return (
    <div className={styles.main}>
    <div className={styles.Pagetitle}>
      <h1>Add Inventory</h1>
    </div>

    <div className={styles.cardContainer}>
      <h6>Inventory Details</h6>
      <form className="row pt-3" >
        <div className="col-6 mb-3">
          <label htmlFor="name">Name</label>
          <input type="text" className="form-control"  name="name"/>
        </div>
        <div className="col-6 mb-3">
          <label htmlFor="email">Email</label>
          <input type="email" className="form-control"  name="email" />
        </div>
        <div className="col-4 mb-3">
          <label htmlFor="phone">Phone</label>
          <input type="text" className="form-control"  name="phone" />
        </div>
        <div className="col-4 mb-3">
          <label htmlFor="address">Address</label>
          <input type="text" className="form-control"  name="address" />
        </div>
        <div className="col-4 mb-3">
          <label htmlFor="city">City</label>
          <input type="text" className="form-control"  name="city" />
        </div>
        <div className="col-4 mb-3">
          <label htmlFor="state">State</label>
          <input type="text" className="form-control"  name="state" />
        </div>

        <div className="col-4 mb-3">
          <label htmlFor="country">Country</label>
          <input type="text" className="form-control"  name="country" />
        </div>

        <div className="col-4 mb-3">
          <label htmlFor="pincode">Pincode</label>
          <input type="text" className="form-control"  name="pin" />
        </div>

        <div className="col-4 mb-3">
          <label htmlFor="pancard">Pan Card</label>
          <input type="text" className="form-control" name="pan"/>
        </div>
        <div className="col-4 mb-3">
          <label htmlFor="gst">Gst Number</label>
          <input type="text" className="form-control" name="gst_number" />
        </div>
      

        <div className={styles.btn}>
          <Link to="../summary">
            <Button variant="contained" className={styles.btn} type="submit" >
              Save
            </Button>
          </Link>
        </div>
      </form>
    </div>
  </div>
  )
}

export default AddInventory
