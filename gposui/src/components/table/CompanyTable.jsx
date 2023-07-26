import * as React from "react";
import style from './company.module.css'
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import tabledata  from "../../data/tabledata";


export default function CompanyTable() {
  return (
    <TableContainer component={Paper} className={style.tableContainer}>
      <Table  aria-label="simple table">
        <TableHead className={style.theadRow}>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell >Product</TableCell>
            <TableCell >Code</TableCell>
            <TableCell >Category</TableCell>
            <TableCell >Price</TableCell>
            <TableCell >Brand Name</TableCell>
            <TableCell >Cost</TableCell>
            <TableCell >Quantity</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {tabledata.map((tabledata) => (
            <TableRow
              key={tabledata.id}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {tabledata.id}
              </TableCell>
              <TableCell >{tabledata.product}</TableCell>
              <TableCell >{tabledata.code}</TableCell>
              <TableCell >{tabledata.category}</TableCell>
              <TableCell >{tabledata.price}</TableCell>
              <TableCell >{tabledata.brand_name}</TableCell>
              <TableCell >{tabledata.cost}</TableCell>
              <TableCell >{tabledata.quantity}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
