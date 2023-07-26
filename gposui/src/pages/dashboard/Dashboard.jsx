import React from "react";
import Content from "../../components/content/Content";
import Sidebar from "../../components/sidebar/Sidebar";
import Topbar from "../../components/topbar/Topbar";
import Style from "./dashboard.module.css";

function Dashboard() {
  return (
    <div className={Style.dashboard}>
      <Sidebar />
      <div className="container-fluid g-0">
        <Topbar />
       <div className={Style.contentWrapper}>
       <Content />
       </div>
      </div>
    </div>
  );
}

export default Dashboard;
