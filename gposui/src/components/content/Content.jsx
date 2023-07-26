
import React from 'react'

import styles from './content.module.css'
import { Outlet } from "react-router-dom";

function Content() {
  return (
    <div className={styles.content} >
        <Outlet />
    </div>
  )
}



export default Content