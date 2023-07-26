import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./login.module.css";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Checkbox from "@mui/material/Checkbox";
import FormControlLabel from "@mui/material/FormControlLabel";
import { NavLink } from "react-router-dom";
import axios from "axios";

function Login() {
  const navigate = useNavigate();
  const [logindata, setlogindata] = useState({
    username: "",
    password: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setlogindata((prevProps) => ({
      ...prevProps,
      [name]: value,
    }));
  };

  const handleLogin = (event) => {
    event.preventDefault();
    
    axios.post("http://127.0.0.1:8000/login", logindata)
      .then((response) => {
        // Handle successful login response here
        console.log(response.data);
        
        // Redirect the user to the onboarding page after successful login
        navigate("/onboarding");
      })
      .catch((error) => {
        // Handle login error response here
        console.error("Error:", error);
      });
  };
  return (
    <div className="container">
      <div className={`row ${styles.login}`}>
        <div className="col-lg-7 col-12 col-md-8">
          <div className={`card  ${styles.card}`}>
            <div className="card-body">
              <h5 className="card-title">Sign In</h5>
            <form onSubmit={handleLogin} method="POST" >
              <p className="card-text mb-4"> Login to stay connected. </p>
              <div className={styles.textdiv}>
                <TextField
                  id="standard-basic"
                  label="Username "
                  variant="standard"
                  className={`mb-3 ${styles.textfiled}`}
                  name="username"
                  value={logindata.username}
                  onChange={handleChange}
                />
                <TextField
                  id="standard-basic"
                  label="Password"
                  variant="standard"
                  className={styles.textfiled}
                  name="password"
                  type="password" // Use "type" attribute to specify password input
                  value={logindata.password}
                  onChange={handleChange}
                />
              </div>

              <div className={styles.signupcheck}>
                <FormControlLabel
                  control={<Checkbox />}
                  label="Remember Me"
                />
                <NavLink to="">Forget Password?</NavLink>
              </div>
              <div className={styles.btndiv}>
                <NavLink to="signup">Create your account</NavLink>
                <Button
                  variant="contained"
                  className={styles.loginBtn}
                  onClick={handleLogin}
                >
                  Sign In
                </Button>
              </div>
            </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
