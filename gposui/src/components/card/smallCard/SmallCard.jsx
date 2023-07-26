import React from 'react'
import DonutChart from '../../chart/DonutChart'
import styles from './smallCrad.module.css'

function SmallCard(props) {
  return (
      <div className={styles.cardInside}>
        <div>
          <div className={styles.cardItem} >
            <div className={styles.icons}>
              <span>{props.icons}</span>
            </div>
            <h2>{props.number}<span className='d-block'>{props.title}</span></h2>
          </div>
          <div>{props.graph}</div>
        </div>
        
      </div>
  )
}
export default SmallCard
