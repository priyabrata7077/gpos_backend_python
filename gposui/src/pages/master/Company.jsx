import React, { useState } from "react";
import styles from "./category.module.css";
import Button from "@mui/material/Button";
import DeleteIcon from "@mui/icons-material/Delete";
import BorderColorIcon from "@mui/icons-material/BorderColor";
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import { Link, Outlet, useLocation } from "react-router-dom";

function Company() {
  const location = useLocation();

  const[companyData,setcompanyData]=useState({
    company_name:""
  })

  const handleChange =(event)=>{
    const{name,value}=event.target
    setcompanyData((prevProps)=>({
      ...prevProps,[name]:value
    }))
  }

  const handleSubmit =(event)=>{
    event.preventDefault()
    console.log(companyData)
  }

  return location.pathname === "/dashboard/company/configure_brand" ? (
    <Outlet />
  ) : (
    <>
      <div className={styles.main}>
        <div className={styles.Pagetitle}>
          <h1>Companies</h1>
        </div>

        <div className="row my-4">
          <div className="col-lg-4 ">
            <div className={`card  ${styles.heading}`}>
              <label htmlFor="brandname">Company Name</label>
              <input type="text" className="form-control my-3"  placeholder="Enter Company Name" onChange={handleChange} name="company_name" value={companyData.company_name}/>
              <Button variant="contained" className={`mt-1 ${styles.button}`} text="submit" onClick={handleSubmit}>
                Save
              </Button>
            </div>
          </div>
          <div className="col-lg-8 mt-3 m-lg-0">
            <div className={`card ${styles.heading}`}>
              <table className={`table ${styles.tablestyle}`}>
                <thead>
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">Name</th>
                    <th scope="col">Brand</th>
                    <th scope="col">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td scope="row">1</td>
                    <td>BigBasket</td>
                    <td>
                      <div>
                        <span>10</span>
                        <Link
                          to="configure_brand"
                          className={styles.brand_name}
                        >
                          Configure Brand
                        </Link>
                      </div>
                    </td>
                    <td>
                      <Tooltip title="Edit">
                        <IconButton
                          data-bs-toggle="offcanvas"
                          data-bs-target="#offcanvasRight"
                          aria-controls="offcanvasRight"
                          className={styles.actionBtn}
                        >
                          <BorderColorIcon />
                        </IconButton>
                      </Tooltip>

                      <Tooltip title="Delete">
                        <IconButton
                          data-bs-toggle="modal"
                          data-bs-target="#exampleModal"
                          className={`ms-2 ${styles.actionBtn}`}
                        >
                          <DeleteIcon />
                        </IconButton>
                      </Tooltip>
                    </td>
                  </tr>
                  <tr>
                    <td scope="row">2</td>
                    <td>StarQuick</td>
                    <td>
                      <div>
                        <span>10</span>
                        <Link
                          to="configure_brand"
                          className={styles.brand_name}
                        >
                          Configure Brand
                        </Link>
                      </div>
                    </td>
                    <td>
                      <Tooltip title="Edit">
                        <IconButton
                          data-bs-toggle="offcanvas"
                          data-bs-target="#offcanvasRight"
                          aria-controls="offcanvasRight"
                          className={styles.actionBtn}
                        >
                          <BorderColorIcon />
                        </IconButton>
                      </Tooltip>

                      <Tooltip title="Delete">
                        <IconButton
                          data-bs-toggle="modal"
                          data-bs-target="#exampleModal"
                          className={`ms-2 ${styles.actionBtn}`}
                        >
                          <DeleteIcon />
                        </IconButton>
                      </Tooltip>
                    </td>
                  </tr>
                  <tr>
                    <td scope="row">3</td>
                    <td>Amazon Pantry</td>
                    <td>
                      <div>
                        <span>10</span>
                        <Link
                          to="configure_brand"
                          className={styles.brand_name}
                        >
                          Configure Brand
                        </Link>
                      </div>
                    </td>
                    <td>
                      <Tooltip title="Edit">
                        <IconButton
                          data-bs-toggle="offcanvas"
                          data-bs-target="#offcanvasRight"
                          aria-controls="offcanvasRight"
                          className={styles.actionBtn}
                        >
                          <BorderColorIcon />
                        </IconButton>
                      </Tooltip>

                      <Tooltip title="Delete">
                        <IconButton
                          data-bs-toggle="modal"
                          data-bs-target="#exampleModal"
                          className={`ms-2 ${styles.actionBtn}`}
                        >
                          <DeleteIcon />
                        </IconButton>
                      </Tooltip>
                    </td>
                  </tr>
                  <tr>
                    <td scope="row">4</td>
                    <td>DMart Ready</td>
                    <td>
                      <div>
                        <span>10</span>
                        <Link
                          to="configure_brand"
                          className={styles.brand_name}
                        >
                          Configure Brand
                        </Link>
                      </div>
                    </td>
                    <td>
                      <Tooltip title="Edit">
                        <IconButton
                          data-bs-toggle="offcanvas"
                          data-bs-target="#offcanvasRight"
                          aria-controls="offcanvasRight"
                          className={styles.actionBtn}
                        >
                          <BorderColorIcon />
                        </IconButton>
                      </Tooltip>

                      <Tooltip title="Delete">
                        <IconButton
                          data-bs-toggle="modal"
                          data-bs-target="#exampleModal"
                          className={`ms-2 ${styles.actionBtn}`}
                        >
                          <DeleteIcon />
                        </IconButton>
                      </Tooltip>
                    </td>
                  </tr>
                  <tr>
                    <td scope="row">5</td>
                    <td>Patanjali Ayurved</td>
                    <td>
                      <div>
                        <span>10</span>
                        <Link
                          to="configure_brand"
                          className={styles.brand_name}
                        >
                          Configure Brand
                        </Link>
                      </div>
                    </td>
                    <td>
                      <Tooltip title="Edit">
                        <IconButton
                          data-bs-toggle="offcanvas"
                          data-bs-target="#offcanvasRight"
                          aria-controls="offcanvasRight"
                          className={styles.actionBtn}
                        >
                          <BorderColorIcon />
                        </IconButton>
                      </Tooltip>

                      <Tooltip title="Delete">
                        <IconButton
                          data-bs-toggle="modal"
                          data-bs-target="#exampleModal"
                          className={`ms-2 ${styles.actionBtn}`}
                        >
                          <DeleteIcon />
                        </IconButton>
                      </Tooltip>
                    </td>
                  </tr>
                  <tr>
                    <td scope="row">6</td>
                    <td>Reliance Smart</td>
                    <td>
                      <div>
                        <span>10</span>
                        <Link
                          to="configure_brand"
                          className={styles.brand_name}
                        >
                          Configure Brand
                        </Link>
                      </div>
                    </td>
                    <td>
                      <Tooltip title="Edit">
                        <IconButton
                          data-bs-toggle="offcanvas"
                          data-bs-target="#offcanvasRight"
                          aria-controls="offcanvasRight"
                          className={styles.actionBtn}
                        >
                          <BorderColorIcon />
                        </IconButton>
                      </Tooltip>

                      <Tooltip title="Delete">
                        <IconButton
                          data-bs-toggle="modal"
                          data-bs-target="#exampleModal"
                          className={`ms-2 ${styles.actionBtn}`}
                        >
                          <DeleteIcon />
                        </IconButton>
                      </Tooltip>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <div
        className="modal fade "
        id="exampleModal"
      
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div className="modal-dialog modal-dialog modal-dialog-centered">
          <div className={`modal-content ${styles.deleteModal}`}>
            <div className={styles.modalHeader}>
              <h1 className="modal-title fs-5" id="exampleModalLabel">
                Delete Company
              </h1>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div className={styles.modalBody}>
              Are you sure you want to delete your record?{" "}
            </div>
            <div className={styles.modalFooter}>
              <Button
                variant="contained"
                data-bs-dismiss="modal"
                className={styles.cancelBtn}
              >
                Cancel
              </Button>
              <Button
                variant="contained"
                color="success"
                className={styles.saveBtn}
              >
                Save
              </Button>
            </div>
          </div>
        </div>
      </div>

      <div className="offcanvas offcanvas-end" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
        <div className="offcanvas-header">
          <h5 className={styles.offcanvasHeading} id="offcanvasRightLabel">
            Update Company Name
          </h5>
          <button
            type="button"
            className="btn-close"
            data-bs-dismiss="offcanvas"
            aria-label="Close"
          ></button>
        </div>
        <div className={`offcanvas-body ${styles.offcanvasBody}`}>
          <label >Company Name</label>
          <input type="text" className="form-control my-3" />
          <Button variant="contained" className={`mt-1 ${styles.button}`}>
            Save
          </Button>
        </div>
      </div>
    </>
  );
}

export default Company;
