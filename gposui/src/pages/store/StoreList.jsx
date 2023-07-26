import styles from "./store.module.css";
import axios from "axios"
import { Link } from "react-router-dom";
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import Button from "@mui/material/Button";
import React, { useState, useEffect } from 'react';
import storedata from "../../data/storedata";
import AddBusinessOutlinedIcon from "@mui/icons-material/AddBusinessOutlined";
import DriveFileRenameOutlineOutlinedIcon from "@mui/icons-material/DriveFileRenameOutlineOutlined";

function StoreList() {
  const [business, setBusiness] = useState([]);

  useEffect(() => {
    // Fetch data from the API
    axios.get('http://127.0.0.1:8000/business/store/add')
      .then(response => {
        setBusiness(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return !business ? (
    <>
      <h1>ohooo no store added </h1>
      <button>
        <Link to="../store">add Store</Link>
      </button>
    </>
  ) : (
    <>
      <div className={styles.main}>
        <div className={styles.Pagetitle}>
          <h1>Stores </h1>
          <Link to="../store">
            <Button variant="contained">Add Store</Button>
          </Link>
        </div>
        <div>
          <div className="row">
            {business.map((item) => {
              // console.log(item);
              return (
                <div className="col-lg-3 col-md-6 col-12  my-3">
                  <div className={`card ${styles.card_business}`}>
                    <div className={styles.businessHeader}>
                      <small className="me-4">22 Jan 22</small>
                      <Tooltip title="Edit" data-bs-toggle="modal" data-bs-target="#exampleModal">
                        <IconButton>
                          <DriveFileRenameOutlineOutlinedIcon />
                        </IconButton>
                      </Tooltip>
                    </div>
                    <div className={styles.businessDetails}>
                      <h5>{item.store_name}</h5>
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
                                Store Name :
                              </small>
                              <small className={styles.smallData}>
                                {item.store_name}
                              </small>
                            </span>
                            <span>
                              <small className={styles.smallPara}>
                                Location :
                              </small>
                              <small className={styles.smallData}>
                                {item.store_location}
                              </small>
                            </span>
                            <span>
                              <small className={styles.smallPara}>
                                Business :
                              </small>
                              <small className={styles.smallData}>
                                {item.store_business}
                              </small>
                            </span>
                            {/* More Details */}
                          </li>

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


      <div className="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div className="modal-dialog modal-dialog-centered modal-lg">
          <div className="modal-content">
            <div className="modal-header">
              <h1 className="modal-title fs-5" id="exampleModalLabel">Abc Store
                <span className={`badge  ${styles.busId}`}>Id : <small>bus001</small></span>
              </h1>
              <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div className="modal-body">
              <form className={`row g-3 needs-validation ${styles.modalForm}`}>
                <div className="col-md-6">
                  <label for="validationCustom01" className="form-label">Store Name</label>
                  <input type="text" className="form-control" id="validationCustom01" value="Mark" required />
                </div>
                <div className="col-md-6">
                  <label for="validationCustom02" className="form-label">Location</label>
                  <input type="text" className="form-control" id="validationCustom02" value="Otto" required />
                </div>
                <div className="col-12 ">
                  <label for="validationCustom02" className="form-label">Business</label>
                  <select
                    class="form-select"
                    aria-label=" example"
                  >
                    <option selected>Open this select menu</option>
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                  </select>
                </div>
                <div className="col-12 py-3">
                  <div className={styles.modalBtn}>
                    <button type="button" className="me-2" data-bs-dismiss="modal">Close</button>
                    <button >Save</button>
                  </div>

                </div>
              </form>
            </div>

          </div>
        </div>
      </div>

    </>
  );
}

export default StoreList
