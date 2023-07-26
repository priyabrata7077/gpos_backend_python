import React from "react";
import styles from "./dashboardHome.module.css";
//import SquareCard from "../../components/card/squareCard/SquareCard.jsx";
import SmallCard from "../../components/card/smallCard/SmallCard";
import PeopleAltOutlinedIcon from "@mui/icons-material/PeopleAltOutlined";
import ForumOutlinedIcon from "@mui/icons-material/ForumOutlined";
import PersonAddAltOutlinedIcon from "@mui/icons-material/PersonAddAltOutlined";
import SsidChartOutlinedIcon from "@mui/icons-material/SsidChartOutlined";
import Button from '@mui/material/Button';
import DonutChart from "../../components/chart/DonutChart";
import AreaChart from "../../components/chart/areaChart/AreaChart";
import LineChart from "../../components/chart/lineChart/LineChart";
import CompanyTable from "../../components/table/CompanyTable";
import { Link } from "react-router-dom";

function DashboardHome() {
  return (
    <div className={styles.main}>
      <div className={styles.Pagetitle}>
        <h1>Dashboard </h1>
        <div className={styles.addOwner}>
          <Link to="../add_business"><Button variant="contained">Add Business</Button></Link>
          <div className={styles.selectBar}>
            <select
              className="form-select form-select-sm"
              aria-label=".form-select-sm example"
            >
              <option value="1">Week</option>
              <option value="2">Month</option>
              <option value="3">Year</option>
            </select>
          </div>
        </div>
      </div>
      <div className="card-container row my-4">
        <div className="col-12 col-lg-7">
          <DonutChart />
        </div>
        <div className="col-12 col-lg-5">
          <div className="row">
            <div className="col-lg-6">
              <SmallCard
                number="168"
                title="Income"
                icons={<PeopleAltOutlinedIcon />}
                graph={<AreaChart />}
              />
            </div>
            <div className="col-lg-6">
              <SmallCard
                number="144"
                title="Customers"
                icons={<PersonAddAltOutlinedIcon />}
                // graph={<LineChart />}
              />
            </div>
            <div className="col-lg-6">
              <SmallCard
                number="198"
                title="Products"
                icons={<SsidChartOutlinedIcon />}
              />
            </div>
            <div className="col-lg-6">
              <SmallCard
                number="236"
                title="Chats"
                icons={<ForumOutlinedIcon />}
              />
            </div>
            <div className="col-lg-6">
              <SmallCard
                number="198"
                title="Products"
                icons={<SsidChartOutlinedIcon />}
              />
            </div>
            <div className="col-lg-6">
              <SmallCard
                number="236"
                title="Chats"
                icons={<ForumOutlinedIcon />}
              />
            </div>
          </div>
        </div>

        <div className="col-lg-12 col-12 mt-3">
          <CompanyTable />
        </div>
      </div>
    </div>
  );
}

export default DashboardHome;
