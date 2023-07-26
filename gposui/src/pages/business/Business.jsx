import React, { useState, useEffect } from "react";
import styles from "./business.module.css";
import axios from "axios";
import { Link } from "react-router-dom";
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import Button from "@mui/material/Button";
import AddBusinessOutlinedIcon from "@mui/icons-material/AddBusinessOutlined";
import DriveFileRenameOutlineOutlinedIcon from "@mui/icons-material/DriveFileRenameOutlineOutlined";

function Business() {
  const [businessData, setBusinessData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBusiness = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/add-business");
        console.log(response.data);
        setBusinessData(response.data);
        setLoading(false);
      } catch (error) {
        console.log(error);
        setError("Error fetching data");
        setLoading(false);
      }
    };

    fetchBusiness();
  }, []);


  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return !businessData ? (
    <>
      <h1>ohooo no business added </h1>
      <button>
        <Link to="../add_business">add bussiness</Link>
      </button>
    </>
  ) : (
    <>
      <div className={styles.main}>
        <div className={styles.Pagetitle}>
          <h1>Businesses </h1>
          <Link to="../add_business">
            <Button variant="contained">Add Business</Button>
          </Link>
        </div>
        <div>
          <div className="row">

            {businessData.map((item) => {
              return (
                <div className="col-lg-3 col-md-6 col-12  my-3">
                  <div className={`card ${styles.card_business}`}>
                    <div className={styles.businessHeader}>
                      <small className="me-4">22 Jan 22</small>
                      <Link to='../store'>
                        <Tooltip title="Add Store">
                          <IconButton>
                            <AddBusinessOutlinedIcon />
                          </IconButton>
                        </Tooltip>
                      </Link>


                      <Tooltip title="Edit" data-bs-toggle="modal" data-bs-target="#exampleModal">
                        <IconButton>
                          <DriveFileRenameOutlineOutlinedIcon />
                        </IconButton>
                      </Tooltip>

                    </div>
                    <div className={styles.businessDetails}>
                      <h5>{item.name}</h5>
                      <div className={styles.innerData}>
                        <ul className={styles.businessCard} key={item.id}>
                          <li>
                            <span>
                              <small className={styles.smallPara}>Id : </small>
                              <small className={styles.smallData}>
                                {item.id}
                              </small>
                            </span>
                            <span>
                              <small className={styles.smallPara}>
                                Email :
                              </small>
                              <small className={styles.smallData}>
                                {item.email}
                              </small>
                            </span>
                            <span>
                              <small className={styles.smallPara}>
                                Phone :
                              </small>
                              <small className={styles.smallData}>
                                {item.phone}
                              </small>
                            </span>
                            <span>
                              <small className={styles.smallPara}>
                                Pincode :
                              </small>
                              <small className={styles.smallData}>
                                {item.pin}
                              </small>
                            </span>   
                          </li>
                         
                <Link to={`../business_page/${item.id}`}>
                  view
                </Link>
                
             
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
           
          </div>
        </div>
      </div>


    

    </>
  );
}

export default Business;
