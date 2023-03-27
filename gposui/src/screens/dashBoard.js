import React from "react";
import { useState } from "react";



const DashBoardUI = () => {

    return (
        <div className='dashboard-container'>
            <button className='dashboard-options' >Setup Store</button>
            <button className='dashboard-options' >Setup Inventory</button>
            <button className='dashboard-options' >Add Employee</button>
        </div>
    )
}

export default DashBoardUI;