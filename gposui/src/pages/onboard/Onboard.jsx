import React, { useState } from "react";
import styles from "./onboard.module.css";
import Button from "@mui/material/Button";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";

function Onboard() {
  const navigate = useNavigate()
  
  const [ownerDetails, setOwnerDetails] = useState({
    name: "", email: "", password: "", contact_number: "", whatsapp_number: "",
    city: "", address: "", country: "", pin: "", pan_card_number: ""
  })

  const handleChange = (event) => {
    const { name, value } = event.target;
    setOwnerDetails((prevProps) => ({
      ...prevProps, [name]: value
    }))
  }

  const handleSubmit = (event) => {
    event.preventDefault()

    const token = localStorage.getItem("token")

    const config = {
      url: "http://192.168.1.19:8000/add-owner-details",
      method: 'post',
      headers: {
        Authorization: token
      },
      data: ownerDetails
    }

    axios(config)
      .then((response) => {
        console.log(response)
      })
      navigate('/dashboard')
      .catch((error) => {
        console.log(error)
      })

  }


  return (
   

    <>
      <div className="container">
        <div className={`row ${styles.onboard}`}>
          <div className="col-md-10 col-12">
            <div className={`card  ${styles.card}`}>
              <h5>Onboarding</h5>
              <form class={`row g-3 ${styles.formArea}`}>
                <div className="col-12">
                  <h6>Personal Details</h6>
                </div>
                <div class="col-md-6 col-12">
                  <label for="validationCustom01" class="form-label">
                    Name
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    id="validationCustom01"
                    name="name" onChange={handleChange} value={ownerDetails.name}
                  />
                </div>
                <div class="col-md-6 col-12">
                  <label for="validationCustom01" class="form-label">
                    Email
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    id="validationCustom01"
                    name="email" onChange={handleChange} value={ownerDetails.email}
                  />
                </div>
                <div class="col-md-4 col-12">
                  <label for="validationCustom01" class="form-label">
                    Contact Number
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    id="validationCustom01"
                    name="contact_number" onChange={handleChange} value={ownerDetails.contact_number}
                  />
                </div>
                <div class="col-md-4 col-12">
                  <label for="validationCustom01" class="form-label">
                    Whatsapp Number
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    id="validationCustom01"
                    name="whatsapp_number" onChange={handleChange} value={ownerDetails.whatsapp_number}
                  />
                </div>
                <div class="col-md-4 col-12">
                  <label for="validationCustom01" class="form-label">
                    Password
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    id="validationCustom01"
                    name="password" onChange={handleChange} value={ownerDetails.password}
                  />
                </div>
                <div className="col-12 mt-5">
                  <h6>Advance Details</h6>
                </div>
                <div class="col-md-6 col-12">
                  <label for="validationCustom01" class="form-label">
                    Pan Card
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    id="validationCustom01"
                    name="pan_card_number" onChange={handleChange} value={ownerDetails.pan_card_number}
                  />
                </div>
                <div class="col-md-6 col-12">
                  <label for="validationCustom01" class="form-label">
                    Address
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    id="validationCustom01"
                    name="address" onChange={handleChange} value={ownerDetails.address}
                  />
                </div>
                <div class="col-md-4 col-12">
                  <label for="validationCustom01" class="form-label">
                    City
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    id="validationCustom01"
                    name="city" onChange={handleChange} value={ownerDetails.city}
                  />
                </div>

                <div class="col-md-4 col-12">
                  <label for="validationCustom01" class="form-label">
                    Country
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    id="validationCustom01"
                    name="country" onChange={handleChange} value={ownerDetails.country}
                  />
                </div>
                <div class="col-md-4 col-12">
                  <label for="validationCustom01" class="form-label">
                    Pincode
                  </label>
                  <input
                    type="text"
                    class="form-control"
                    id="validationCustom01"
                    name="pin" onChange={handleChange} value={ownerDetails.pin}
                  />
                </div>


                <div class="col-12 text-end mt-5">
                  <button class={`btn me-3 ${styles.onboardBtn}`} type="reset">
                    Cancel
                  </button>
                  
                    <Button variant="contained" className={styles.onboardBtn} onClick={handleSubmit}>
                      Save
                    </Button>
                  

                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Onboard;
