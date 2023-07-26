import axios from 'axios';
function DeleteEmployee(employeeId) {
    axios
      .delete('http://localhost:8000/business/employee/add')
      .then(response => {
        // Perform any additional actions upon successful deletion if needed
  
        // Refresh the employee list or update the state after deletion
        fetchEmployees();
      })
      .catch(error => {
        console.error(error);
      });
  }
 

  export default DeleteEmployee;