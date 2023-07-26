import React, { useState, useEffect } from 'react';
import styles from "./people.module.css";
import Button from "@mui/material/Button";
import DeleteIcon from "@mui/icons-material/Delete";
import BorderColorIcon from "@mui/icons-material/BorderColor";
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import axios from "axios";

function createData(id, name, contact, store, address) {
  return { id, name, contact, store, address };
}

function Customer() {
  const [editCustomer, setEditCustomer] = useState(null);
  const [rows, setRows] = useState([]);
  const [formData, setFormData] = useState({
    name: "",
    contact: "",
    store: "",
    address: "",
  });
  const [stores, setStores] = useState([]); // Declare the stores state variable
  const fetchCustomer = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/handle-customer");
      // Rest of the code to handle the response
    } catch (error) {
      console.error(error);
    }
  };
  // Fetch stores data from the backend API
  useEffect(() => {
    const fetchStores = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/add-store"); // Replace with the correct API endpoint for fetching stores
        setStores(response.data);
      } catch (error) {
        console.error("Error fetching stores:", error);
      }
    };
    fetchStores();
  }, []);
  // Initialize customers as an empty array
  useEffect(() => {
    const fetchCustomer = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/handle-customer");
        if (Array.isArray(response.data)) {
          const customers = response.data.map((customer) =>
            createData(
              customer.id,
              customer.name,
              customer.contact,
              customer.store,
              customer.address
            )
          );
          setRows(customers);
        } else {
          console.error("Response data is not an array:", response.data);
          setRows([]);
        }
      } catch (error) {
        console.error(error);
      }
    };
    fetchCustomer();
  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      // Send a POST request to the server with the form data
      const response = await axios.post("http://127.0.0.1:8000/handle-customer",{
      id:formData.id,
      name: formData.name,
      contact: formData.contact,
      store: formData.store,
      address: formData.address,
    });
      console.log(response.data); // Handle successful response

      // Reset the form fields after successful submission
      setFormData({
        name: "",
        contact: "",
        store: "",
        address: "",
      });

      // Refetch the customer data to update the table with the latest data
      fetchCustomer();
    } catch (error) {
      console.error(error); // Handle error
    }
  };
  

  const handleEdit = (customer) => {
    setEditCustomer(customer);
    setFormData({
      name: customer.name,
      contact: customer.contact,
      store: customer.store,
      address: customer.address,
    });
  };
  const handleSubmitEdit = async (event) => {
    event.preventDefault();
    try {
      // Send a PUT request to the server with the form data
      const response = await axios.put(`http://127.0.0.1:8000/handle-customer/update/${editCustomer.id}`, {
        name: formData.name,
        contact: formData.contact,
        store: formData.store,
        address: formData.address,
      });
      console.log(response.data); // Handle successful response
  
      // Reset the form fields after successful submission
      setFormData({
        name: "",
        contact: "",
        store: "",
        address: "",
      });
  
      // Refetch the customer data to update the table with the latest data
      fetchCustomer();
    } catch (error) {
      console.error(error); // Handle error
    }
  };
  const handleDelete = async (customerId) => {
    try {
      // Send a DELETE request to the server with the customer ID
      const response = await axios.delete(`http://127.0.0.1:8000/handle-customer/update/${customerId}`);
      console.log(response.data); // Handle successful response
  
      // Refetch the customer data to update the table with the latest data
      fetchCustomer();
    } catch (error) {
      console.error(error); // Handle error
    }
  };
  return (
    <>
       <div className={styles.main}>
        <div className={styles.Pagetitle}>
          <h1>Customer Details</h1>
        </div>
        <div className="row my-4">
          <div className="col-lg-4 ">
            <div className={`card  ${styles.heading}`}>
              <form onSubmit={handleSubmit} action="../customer" method="POST">
                <label htmlFor="name">Name</label>
                <input
                  id="name"
                  name="name"
                  type="text"
                  className="form-control mb-3 mt-2"
                  placeholder="Enter Name"
                  value={formData.name}
                  onChange={handleChange}
                />
                <label htmlFor="contact">Contact</label>
                <input
                  id="contact"
                  name="contact"
                  type="text"
                  className="form-control mb-3 mt-2"
                  placeholder="Enter Contact"
                  value={formData.contact}
                  onChange={handleChange}
                />
                <label htmlFor="store">Store</label>
                <select
                  id="store"
                  name="store"
                  className="form-select mb-3 mt-2"
                  value={formData.store}
                  onChange={handleChange}
                >
                
                 <option value="">Select Store</option>
                  {stores.map((store) => (
                    <option key={store.id} value={store.id}>
                      {store.name}
                    </option>
                  ))}
                </select>
                <label htmlFor="address">Address</label>
                <input
                  id="address"
                  name="address"
                  className="form-control mb-3 mt-2"
                  placeholder="Enter Address"
                  value={formData.address}
                  onChange={handleChange}
                />
                <Button type="submit" variant="contained" className={`mt-1 ${styles.button}`}>
                  Save
                </Button>
              </form>
            </div>
          </div>
          <div className="col-lg-8 mt-3 m-lg-0">
            <div className={`card ${styles.heading}`}>
              <table className={`table ${styles.tablestyle}`}>
                <thead className={styles.theadRow}>
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">Name</th>
                    <th scope="col">Contact</th>
                    <th scope="col">Store</th>
                    <th scope="col">Address</th>
                    <th scope="col">Action</th>
                  </tr>
                </thead>
               
                <tbody>
                  {rows.map((row, index) => (
                    <tr key={index}>
                      <td scope="row">{index + 1}</td>
                      <td>{row.name}</td>
                      <td>{row.contact}</td>
                      <td>{row.store}</td>
                      <td>{row.address}</td>
                      <td>
                        <Tooltip title="Edit">
                          <IconButton
                            onClick={() => handleEdit(row)}
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
                            onClick={() => handleDelete(row.id)}
                            data-bs-toggle="modal"
                            data-bs-target="#exampleModal"
                            className={`ms-2 ${styles.actionBtn}`}
                          >
                            <DeleteIcon />
                          </IconButton>
                        </Tooltip>
                      </td>
                    </tr>
                  ))}
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
              <form onSubmit={handleDelete} action="../customer" method="POST"></form>
              <Button
          variant="contained"
          color="success"
          className={styles.saveBtn}
          onClick={() => {
            handleDelete(); // Clear the deleteCustomerId state variable
            performDelete(deleteCustomerId); // Perform the delete action with the stored customer ID
          }}
        >Yes
        </Button>
            </div>
          </div>
        </div>
      </div>

      <div className="offcanvas offcanvas-end" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
        <div className="offcanvas-header">
          <h5 className={styles.offcanvasHeading} id="offcanvasRightLabel">
            Edit Customer Details
          </h5>
          <button
            type="button"
            className="btn-close"
            data-bs-dismiss="offcanvas"
            aria-label="Close"
          ></button>
        </div>
        
        <div className={`card  ${styles.heading}`}>
    <form onSubmit={handleSubmitEdit} action="../customer" method="POST">
      <label htmlFor="name">Name</label>
      <input
        id="name"
        name="name"
        type="text"
        className="form-control mb-3 mt-2"
        placeholder="Enter Name"
        value={formData.name}
        onChange={handleChange}
        autoComplete="name" // Set autocomplete attribute for name field
      />
      <label htmlFor="contact">Contact</label>
      <input
        id="contact"
        name="contact"
        type="text"
        className="form-control mb-3 mt-2"
        placeholder="Enter Contact"
        value={formData.contact}
        onChange={handleChange}
        autoComplete="tel" // Set autocomplete attribute for contact (telephone number) field
      />
      <label htmlFor="store">Store</label>
      <select
        id="store"
        name="store"
        className="form-select mb-3 mt-2"
        value={formData.store}
        onChange={handleChange}
        autoComplete="store" // Set autocomplete attribute for store field
      >
        <option value="">Select Store</option>
        {stores.map((store) => (
          <option key={store.id} value={store.id}>
            {store.name}
          </option>
        ))}
      </select>
      <label htmlFor="address">Address</label>
      <input
        id="address"
        name="address"
        className="form-control mb-3 mt-2"
        placeholder="Enter Address"
        value={formData.address}
        onChange={handleChange}
        autoComplete="address" // Set autocomplete attribute for address field
      />
      <Button type="submit" variant="contained" className={`mt-1 ${styles.button}`}>
        Save
      </Button>
    </form>
  </div>

      </div>
    </>
  )
}
export default Customer
