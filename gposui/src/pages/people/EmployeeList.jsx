import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import Button from '@mui/material/Button';

function createData(id, name, email, phone, address, adhaar) {
  return { id, name, email, phone, address, adhaar };
}

function EmployeeList() {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    const fetchEmployees = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/business/employee/add");
        if (Array.isArray(response.data)) {
          const employees = response.data.map((employee) =>
            createData(
              employee.id,
              employee.name,
              employee.email,
              employee.phone,
              employee.address,
              employee.adhaar,
            )
          );
          setRows(employees);
        } else {
          console.error("Response data is not an array:", response.data);
          setRows([]);
        }
      } catch (error) {
        console.error(error);
      }
    };
    fetchEmployees();
  }, []);

    const handleDeleteBtn = async (id) => {
      try {
        await axios.get(`http://127.0.0.1:8000/business/employee/delete/${id}`);
        setRows(prevRows => prevRows.filter(employee => employee.id !== id));
      } catch (error) {
        console.error(error);
      }
    };
   

  
  return (
    <TableContainer>
      <button>
        <Link to="../add_employee">Add Employee</Link>
      </button>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell>Email</TableCell>
            <TableCell>Phone</TableCell>
            <TableCell>Address</TableCell>
            <TableCell>Adhaar</TableCell>
            <TableCell>Action</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.email}</TableCell>
              <TableCell>{row.phone}</TableCell>
              <TableCell>{row.address}</TableCell>
              <TableCell>{row.adhaar}</TableCell>
              <TableCell>
                <Link to={`../edit_employee/${row.id}`}>
                  <Button startIcon={<EditIcon />} />
                </Link>
                <Button
                  className="fa fa-trash-o text-danger d-inline mx-3"
                  aria-hidden="true"
                  onClick={() => handleDeleteBtn(row.id)}
                >
                  <DeleteIcon />
                </Button>
                
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default EmployeeList;
