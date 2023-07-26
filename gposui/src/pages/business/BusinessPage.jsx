import React, { useState, useEffect } from "react";
import styles from "./business.module.css";
import { Link, useParams } from "react-router-dom";
import Button from "@mui/material/Button";
import axios from "axios";
import DonutChart from "../../components/chart/DonutChart";
import SmallCard from "../../components/card/smallCard/SmallCard";
import PeopleAltOutlinedIcon from "@mui/icons-material/PeopleAltOutlined";
import ForumOutlinedIcon from "@mui/icons-material/ForumOutlined";
import PersonAddAltOutlinedIcon from "@mui/icons-material/PersonAddAltOutlined";
import SsidChartOutlinedIcon from "@mui/icons-material/SsidChartOutlined";

function BusinessPage() {
  const { id } = useParams();
  console.log("ID:", id);
  const [businessData, setBusinessData] = useState({
    name: "",
    email: "",
    phone: "",
    address: "",
    city: "",
    pin: "",
    state: "",
    country: "",
    pan: "",
    gst_number: "",
    date_of_entry: "",
    owner_id: "",
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBusinessData = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/add-business/update/${id}`);
        setBusinessData(response.data);
        setLoading(false);
      } catch (error) {
        setError(error.message);
        setLoading(false);
      }
    };
    fetchBusinessData();
  }, [id]);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setBusinessData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const employeeData = {
      name: formData.get("name"),
      email: formData.get("email"),
      phone: formData.get("phone"),
      address: formData.get("address"),
      city: formData.get("city"),
      pin: formData.get("pin"),
      state: formData.get("state"),
      country: formData.get("country"),
      pan: formData.get("pan"),
      gst_number: formData.get("gst_number"),
      date_of_entry: formData.get("date_of_entry"),
      owner_id: formData.get("owner_id"),
    };

    const url = `http://127.0.0.1:8000/add-business/update/${id}`;

    axios
      .put(url, employeeData) // Use axios.put for updating data
      .then((response) => {
        console.log(response.data);
        // Handle successful response or perform any actions after successful update
      })
      .catch((error) => {
        console.error(error);
        // Handle error or display an error message to the user
      });
  };

  return (
    <>
      <div className={styles.main}>
        <div className={styles.Pagetitle}>
          <h1>{businessData.name}</h1>
          <Link to="../add_business">
            <Button variant="contained">Add Business</Button>
          </Link>
        </div>
        <div>
          <div className="row my-4">
            <div className="col-12">
              <div className={`card ${styles.cardPage}`}>
                <ul>
                  <li>
                    <span>Id</span>
                    {businessData.id}
                  </li>
                  <li>
                    <span>Email</span>
                    {businessData.email}
                  </li>
                  <li>
                    <span>Phone</span>
                    {businessData.phone}
                  </li>
                  <li>
                    <span>Pincode</span>
                    {businessData.pin}
                  </li>
                  <li>
                    <span>Address</span>
                    {businessData.address}
                  </li>
                  <li>
                    <span>City</span>
                    {businessData.city}
                  </li>
                  <li>
                    <span>State</span>
                    {businessData.state}
                  </li>
                  <li>
                    <span>Country</span>
                    {businessData.country}
                  </li>
                  <li>
                    <span>Pan Card</span>
                    {businessData.pan}
                  </li>
                  <li>
                    <span>Gst Number</span>
                    {businessData.gst_number}
                  </li>
                  <li>
                    <span>Store</span>
                    {/* Render the store names here */}
                    {businessData.stores?.map((store, index) => (
                      <small key={index}>{store.name}</small>
                    ))}
                  </li>
                </ul>
              </div>
            </div>
            <div className="col-lg-6 col-md-6 col-12  my-4">
              <DonutChart />
            </div>
            <div className="col-lg-6 my-4">
              <div className="row">
                <div className="col-lg-6">
                  <SmallCard number="168" title="Income" icons={<PeopleAltOutlinedIcon />} />
                </div>
                <div className="col-lg-6">
                  <SmallCard number="144" title="Customers" icons={<PersonAddAltOutlinedIcon />} />
                </div>
                <div className="col-lg-6">
                  <SmallCard number="198" title="Products" icons={<SsidChartOutlinedIcon />} />
                </div>
                <div className="col-lg-6">
                  <SmallCard number="236" title="Stores" icons={<ForumOutlinedIcon />} />
                </div>
                <div className="col-lg-6">
                  <SmallCard number="198" title="Products" icons={<SsidChartOutlinedIcon />} />
                </div>
                <div className="col-lg-6">
                  <SmallCard number="236" title="Chats" icons={<ForumOutlinedIcon />} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default BusinessPage;
