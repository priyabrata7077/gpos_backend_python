import React, { useRef, useState } from "react";
import Style from "./sidebar.module.css";
import { RxHamburgerMenu } from "react-icons/rx";
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import DashboardCustomizeOutlinedIcon from "@mui/icons-material/DashboardCustomizeOutlined";
import EventNoteOutlinedIcon from "@mui/icons-material/EventNoteOutlined";
import { Link } from "react-router-dom";
import StoreMallDirectoryOutlinedIcon from '@mui/icons-material/StoreMallDirectoryOutlined';
import PeopleAltOutlinedIcon from '@mui/icons-material/PeopleAltOutlined';
import CasesOutlinedIcon from '@mui/icons-material/CasesOutlined';
import RemoveOutlinedIcon from '@mui/icons-material/RemoveOutlined';

function Sidebar() {
  const [spanDisplay, setSpanDisplay] = useState("block");
  const [hamMenu, setHamMenu] = useState("84%");

  const sideBar = useRef();

  const [isOpen, setIsOpen] = useState(false);

  // dropdown
  const handleDropdown = (e) => {
    console.log(e.target);
    {
      !isOpen ? setIsOpen(true) : setIsOpen(false);
    }
  };

  // menubar
  const handleSideMenu = () => {
    const panelWidth = sideBar.current;
    if (panelWidth.style.width === "280px") {
      panelWidth.style.width = "80px";
      setSpanDisplay("none");
      setHamMenu("93%");
    } else {
      panelWidth.style.width = "280px";
      setSpanDisplay("block");
      setHamMenu("84%");
    }
  };

  return (
    <div ref={sideBar} className={Style.sidebar}>
      <div className={Style.logoWrapper}>
        <span>logo</span>

        <RxHamburgerMenu
          onClick={handleSideMenu}
          className={Style.hamMenu}
          size="1.4rem"
          style={{ right: hamMenu }}
        />
      </div>

      <ul className={Style.sideItems}>
        <Link to="summary" className={Style.linkItems}>
          <li>
            <Tooltip title="Dashboard" placement="right-start">
              <IconButton>
                <DashboardCustomizeOutlinedIcon />
              </IconButton>
            </Tooltip>
            <span style={{ display: spanDisplay }} className={Style.spanIcon}>
              Dashboard
            </span>
          </li>
        </Link>

        {/* <Link to="profile" className={Style.linkItems}>
          <li>
            <Tooltip title="Dashboard" placement="right-start">
              <IconButton>
                <DashboardCustomizeOutlinedIcon />
              </IconButton>
            </Tooltip>
            <span style={{ display: spanDisplay }} className={Style.spanIcon}>
              onboard
            </span>
          </li>
        </Link> */}

        <div className="accordion accordion-flush" id="accordionFlushExample">

          <div className={`accordion-item ${Style.accordionItem}`}>
            <li
              className="accordion-button collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#flush-collapseFour"
              aria-expanded="false"
              aria-controls="flush-collapseFour"
            >
              <Tooltip title="Business" placement="right-start">
                <IconButton>
                  <EventNoteOutlinedIcon />
                </IconButton>
              </Tooltip>
              <span style={{ display: spanDisplay }} className={Style.spanIcon}>
                Master
              </span>
            </li>
            <div
              id="flush-collapseFour"
              className="accordion-collapse collapse"
              data-bs-parent="#accordionFlushExample"
            >
              <div className={`accordion-body ${Style.subItem}`}>
                <Link to="company" className="d-flex align-items-center">
                <RemoveOutlinedIcon/><span style={{ display: spanDisplay }} className={Style.spanIcon}> Company</span>
                </Link>
                <Link to="category" className="d-flex align-items-center">
                <RemoveOutlinedIcon/> <span style={{ display: spanDisplay }} className={Style.spanIcon}> Category</span>
                </Link>
              </div>
            </div>
          </div>

          <div className={`accordion-item ${Style.accordionItem}`}>
            <li
              className="accordion-button collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#flush-collapseTwo"
              aria-expanded="false"
              aria-controls="flush-collapseTwo"
            >
              <Tooltip title="Business" placement="right-start">
                <IconButton>
                  <CasesOutlinedIcon />
                </IconButton>
              </Tooltip>
              <span style={{ display: spanDisplay }} className={Style.spanIcon}>
                Business
              </span>
            </li>
            <div
              id="flush-collapseTwo"
              className="accordion-collapse collapse"
              data-bs-parent="#accordionFlushExample"
            >
              <div className={`accordion-body ${Style.subItem}`}>
                <Link to="add_business" className="d-flex align-items-center">
                <RemoveOutlinedIcon/><span style={{ display: spanDisplay }} className={Style.spanIcon}> Add Business</span>
                </Link>
                <Link to="business" className="d-flex align-items-center">
                <RemoveOutlinedIcon/><span style={{ display: spanDisplay }} className={Style.spanIcon}> Business List</span>
                </Link>
              </div>
            </div>
          </div>

          <div className={`accordion-item ${Style.accordionItem}`}>
            <li className="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
              <Tooltip title="Employee Master" placement="right-start">
                <IconButton>
                  <PeopleAltOutlinedIcon />
                </IconButton>
              </Tooltip>
              <span style={{ display: spanDisplay }} className={Style.spanIcon}> People</span>
            </li>
            <div id="flush-collapseOne" className="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
              <div className={`accordion-body ${Style.subItem}`}>
                <Link to="employee_master" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Employee List</span>
                </Link>
                <Link to="add_employee" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Add Employee</span>
                </Link>
                <Link to="customer" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Customer</span>
                </Link>
               
                <Link to="supplier" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Supplier</span>
                </Link>
               
              </div>
            </div>
          </div>

          <div className={`accordion-item ${Style.accordionItem}`}>
            <li className="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree"
              aria-expanded="false"
              aria-controls="flush-collapseThree"
            >
              <Tooltip title="Store" placement="right-start">
                <IconButton>
                  <StoreMallDirectoryOutlinedIcon />
                </IconButton>
              </Tooltip>
              <span style={{ display: spanDisplay }} className={Style.spanIcon}>
                Store
              </span>
            </li>

            <div
              id="flush-collapseThree"
              className="accordion-collapse collapse"
              data-bs-parent="#accordionFlushExample"
            >
              <div className={`accordion-body ${Style.subItem}`}>
                <Link to="store" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Add Store</span>
                </Link>
                <Link to="store_list" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Store List</span>
                </Link>
              </div>
            </div>
          </div>

          <div className={`accordion-item ${Style.accordionItem}`}>
            <li className="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#flush-collapseFive"
              aria-expanded="false"
              aria-controls="flush-collapseFive"
            >
              <Tooltip title="Store" placement="right-start">
                <IconButton>
                  <StoreMallDirectoryOutlinedIcon />
                </IconButton>
              </Tooltip>
              <span style={{ display: spanDisplay }} className={Style.spanIcon}>
                Sale
              </span>
            </li>

            <div
              id="flush-collapseFive"
              className="accordion-collapse collapse"
              data-bs-parent="#accordionFlushExample"
            >
              <div className={`accordion-body ${Style.subItem}`}>
                <Link to="add_sale" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Add Sale</span>
                </Link>
                <Link to="sale_list" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Sale List</span>
                </Link>
              </div>
            </div>
          </div>

          <div className={`accordion-item ${Style.accordionItem}`}>
            <li className="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#flush-collapseSix"
              aria-expanded="false"
              aria-controls="flush-collapseSix"
            >
              <Tooltip title="Store" placement="right-start">
                <IconButton>
                  <StoreMallDirectoryOutlinedIcon />
                </IconButton>
              </Tooltip>
              <span style={{ display: spanDisplay }} className={Style.spanIcon}>
                Purchase
              </span>
            </li>

            <div
              id="flush-collapseSix"
              className="accordion-collapse collapse"
              data-bs-parent="#accordionFlushExample"
            >
              <div className={`accordion-body ${Style.subItem}`}>
                <Link to="invoice" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Invoice</span>
                </Link>
                <Link to="return" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Return</span>
                </Link>
              </div>
            </div>
          </div>

          <div className={`accordion-item ${Style.accordionItem}`}>
            <li className="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#flush-collapseSeven"
              aria-expanded="false"
              aria-controls="flush-collapseSeven"
            >
              <Tooltip title="Store" placement="right-start">
                <IconButton>
                  <StoreMallDirectoryOutlinedIcon />
                </IconButton>
              </Tooltip>
              <span style={{ display: spanDisplay }} className={Style.spanIcon}>
                Inventory
              </span>
            </li>

            <div
              id="flush-collapseSeven"
              className="accordion-collapse collapse"
              data-bs-parent="#accordionFlushExample"
            >
              <div className={`accordion-body ${Style.subItem}`}>
                <Link to="add_inventory" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Add Inventory</span>
                </Link>
                <Link to="inventory_list" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Inventory List</span>
                </Link>
              </div>
            </div>
          </div>

          <div className={`accordion-item ${Style.accordionItem}`}>
            <li className="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#flush-collapseEight"
              aria-expanded="false"
              aria-controls="flush-collapseEight"
            >
              <Tooltip title="Store" placement="right-start">
                <IconButton>
                  <StoreMallDirectoryOutlinedIcon />
                </IconButton>
              </Tooltip>
              <span style={{ display: spanDisplay }} className={Style.spanIcon}>
                Accounting
              </span>
            </li>

            <div
              id="flush-collapseEight"
              className="accordion-collapse collapse"
              data-bs-parent="#accordionFlushExample"
            >
              <div className={`accordion-body ${Style.subItem}`}>
                <Link to="payment" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}> Payment</span>
                </Link>
                <Link to="receipt" className="d-flex align-items-center">
                  <RemoveOutlinedIcon /><span style={{ display: spanDisplay }} className={Style.spanIcon}>Recepit</span>
                </Link>
              </div>
            </div>
          </div>

        </div>
      </ul>
    </div>
  );
}

export default Sidebar;
