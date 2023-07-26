import React from 'react'
import styles from './squarecard.module.css'

function SquareCard() {
  return (
    <div className="col-12 col-lg-4">
        <div className={styles.squareInside}>
            <div className={styles.squareItem}>
              <h5>Activity Regarding</h5>
              <a href="#">View All</a>
            </div>
            
        </div>
    </div>
  )
}

export default SquareCard