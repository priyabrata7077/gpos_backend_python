import React from "react";
import Chart from "react-apexcharts";
import style from './area.module.css'

function AreaChart(props) {
  const series = [
    {
      data: [2.3, 3.1, 4.0, 5.7, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 10.1],
    },
  ];

  const options = {
    chart: {
      type: "area",
      sparkline: {
        enabled: false,
        },
        background: '#fff',
        toolbar:{
            show:false
        }
    },
    plotOptions: {
      bar: {
        borderRadius: 10,
        dataLabels: {
          position: "top", // top, center, bottom
        },
      },
    },
    legend:{
        show:false
    },
   
    dataLabels: {
      enabled: false,
      formatter: function (val) {
        return val + "%";
      },
      offsetY: -20,
      style: {
        fontSize: "12px",
        colors: ["#304758"],
      },
    },

    grid:{
        show:false
    },
    tooptip:{
        enabled:false
    },
   
    yaxis: {
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
      labels: {
        show: false,
        formatter: function (val) {
          return val + "%";
        },
      },
    },

    colors: [function({ value, seriesIndex, w }) {
        if (value < 55) {
            return '#0dcaf073'
        } else {
            return '#0dcaf08c'
        }
      }, function({ value, seriesIndex, w }) {
        if (value < 111) {
            return '#0dcaf073'
        } else {
            return '#0dcaf08c'
        }
      }]
  
  };
  return (
    
      <Chart options={options} type="area" series={series}   className={style.areaChart}/>
   
  );
}

export default AreaChart;
