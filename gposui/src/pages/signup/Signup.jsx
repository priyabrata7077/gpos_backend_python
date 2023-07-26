import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./signup.module.css";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Checkbox from "@mui/material/Checkbox";
import FormControlLabel from "@mui/material/FormControlLabel";
import { NavLink } from "react-router-dom";
import axios from "axios";

function Signup() {
  const navigate = useNavigate();
  const [signupData, setSignupData] = useState({
    username: "",
    email: "",
    password: "", 
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setSignupData((prevProps) => ({
      ...prevProps,
      [name]: value,
    }));
  };

  const handleLogin = (event) => {
    navigate("/onboarding");
    event.preventDefault();
     
    const config = {
      method: 'post',
      url: 'http://127.0.0.1:8000/register',
      data : signupData
    };
    
    axios(config)
    .then(function (response) {
      console.log(JSON.stringify(response.data));
    })
    .catch(function (error) {
      console.log(error);
    });
    
   
  };

  return (
    <div className="container">
      <div className={`row ${styles.login}`}>
        <div className="col-lg-7 col-12 col-md-8">
          <div className={`card  ${styles.card}`}>
            <div className="card-body">
              <h5 className="card-title">Sign Up</h5>
              <p className="card-text mb-4"> Sign to stay connected. </p>
              <div className="mt-4">
                <form className="row gx-3" onSubmit={handleLogin} >
                  <div className=" col-12">
                    <TextField
                      id="standard-basic"
                      label="username "
                      variant="standard"
                      className={`mb-3 ${styles.textfiled}`}
                      name="username"
                      value={signupData.username}
                      onChange={handleChange}
                    />
                  </div>
                  <div className="col-12">
                    <TextField
                      id="standard-basic"
                      label="Email "
                      variant="standard"
                      className={`mb-3 ${styles.textfiled}`}
                      name="email"
                      onChange={handleChange}
                      value={signupData.email}
                    />
                  </div>
                  
                  <div className="col-12">
                    <TextField
                      id="standard-basic"
                      label="Password "
                      variant="standard"
                      className={`mb-3 ${styles.textfiled}`}
                      name="password"
                      onChange={handleChange}
                      value={signupData.password}
                    />
                  </div>
                  
                  <div className={styles.signupcheck}>
                <FormControlLabel
                  control={<Checkbox />}
                  label="I agree with the terms of use"
                />
              </div>
              <div className={styles.btndiv}>
                <NavLink to="/">Sign In</NavLink>
                <Button
                  variant="contained"
                  size="large"
                  className={styles.loginBtn}
                  onClick={handleLogin}
                >
                  Next
                </Button>
              </div>
                </form>
              </div>

              
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Signup;
