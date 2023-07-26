import React, { useState, useEffect } from "react";
import styles from "./sale.module.css";
import { Link } from "react-router-dom";
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import Button from "@mui/material/Button";
import businessdata from "../../data/businessdata";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import DeleteIcon from "@mui/icons-material/Delete";
// import DeleteOutlineOutlinedIcon from '@mui/icons-material/DeleteOutlineOutlined';
import DriveFileRenameOutlineOutlinedIcon from "@mui/icons-material/DriveFileRenameOutlineOutlined";
import axios from 'axios';

function createData(id, qty, purchase_rate, mrp, sale_rate,sub_total) {
  return { id, qty, purchase_rate, mrp, sale_rate,sub_total };
}

function SaleList() {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    const fetchSales = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/sales");
        if (Array.isArray(response.data)) {
          const Sales = response.data.map((sale) =>
            createData(
              sale.id,
              sale.qty,
              sale.purchase_rate,
              sale.mrp,
              sale.sale_rate,
              sale.sub_total,
            )
          );
          setRows(Sales);
        } else {
          console.error("Response data is not an array:", response.data);
          setRows([]);
        }
      } catch (error) {
        console.error(error);
      }
    };
    fetchSales();
  }, []);


  return (
    <>
      <div className={styles.main}>
        <div className={styles.Pagetitle}>
          <h1>Sale List</h1>
          <Link to="../store">
            <Button variant="contained">Add Sale</Button>
          </Link>
        </div>
        <div className="mt-4">
          <TableContainer component={Paper} className={styles.tableContainer}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
              <TableHead className={styles.theadRow}>
                <TableRow>
                  <TableCell>Bill ID</TableCell>
                  <TableCell>Quantity</TableCell>
                  <TableCell>Purchase Rate</TableCell>
                  <TableCell>MRP</TableCell>
                  <TableCell>Sale Rate</TableCell>
                  <TableCell>Total</TableCell>
                  <TableCell>Action</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {rows.map((row) => (
                  <TableRow
                    key={row.name} scope="row"
                    sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                  >
                    
                    <TableCell>{row.id}</TableCell>
                    <TableCell>{row.qty}</TableCell>
                    <TableCell>{row.purchase_rate}</TableCell>
                    <TableCell>{row.mrp}</TableCell>
                    <TableCell>{row.sale_rate}</TableCell>
                    <TableCell>{row.sub_total}</TableCell>
                    <TableCell>
                    <Link to='#'>
                     <Tooltip title="Edit">
                        <IconButton  className={styles.actionBtn}>
                          <DriveFileRenameOutlineOutlinedIcon />
                        </IconButton>
                      </Tooltip>
                     </Link>
                     <Tooltip title="Delete">
                        <IconButton
                          data-bs-toggle="modal"
                          data-bs-target="#exampleModal"
                          className={`ms-2 ${styles.actionBtn}`}
                        >
                          <DeleteIcon />
                        </IconButton>
                      </Tooltip>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
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
    </>
  );
}

export default SaleList;
