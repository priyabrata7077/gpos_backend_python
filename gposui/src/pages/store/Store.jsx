import React, { useState, useEffect } from "react";
import styles from "./store.module.css";
import Button from "@mui/material/Button";
import axios from "axios";

function Store() {
  const [rows, setRows] = useState([]);
  const [storedata, setStoreData] = useState({
    store_name: "",
    location: "",
    business: "",
  });

  const fetchStores = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/business/store/add");
      setRows(response.data);
    } catch (error) {
      console.error("Error fetching stores:", error);
    }
  };

  useEffect(() => {
    fetchStores();
  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setStoreData((prevProps) => ({
      ...prevProps,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const url = "http://127.0.0.1:8000/business/store/add"; // Correct URL for the POST request

      // Send a POST request to the server with the storedata
      const response = await axios.post(url, storedata);
      console.log(response.data); // Handle successful response

      // Reset the form fields after successful submission
      setStoreData({
        store_name: "",
        location: "",
        business: "",
      });

      // Refetch the store data to update the table with the latest data
      fetchStores();
    } catch (error) {
      console.error(error); // Handle error
    }
  };
  return (
    <div className={styles.main}>
      <div className={styles.Pagetitle}>
        <h1>Add Store</h1>
      </div>

      <div className={styles.cardContainer}>
        <h6>Store Details</h6>
        <form className="row pt-3">
          <div className="col-12 mb-3">
            <label htmlFor="store_name">Store Name</label>
            <input
              type="text"
              className="form-control"
              id="store_name" // Add an id attribute here
              name="store_name"
              onChange={handleChange}
              value={storedata.store_name}
            />
          </div>
          <div className="col-12 mb-3">
            <label htmlFor="location">Location</label>
            <input
              type="location"
              className="form-control"
              id="location" // Add an id attribute here
              name="location"
              onChange={handleChange}
              value={storedata.location}
            />
          </div>
          <div className="col-12 mb-3">
            <label htmlFor="business">Business</label>
            <select
              id="business" // Add an id attribute here
              name="business"
              className="form-select mb-3 mt-2"
              value={storedata.business}
              onChange={handleChange}
            >
              <option value="">Select Business</option>
              {rows.map((business) => (
                <option key={business.id} value={business.id}>
                  {business.name}
                </option>
              ))}
            </select>
          </div>
          <div className={styles.btn}>
            <Button
              variant="contained"
              className={styles.btn}
              type="submit"
              onClick={handleSubmit}
            >
              Save
            </Button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Store;
