import React from "react";
import Chart from "react-apexcharts";
import styles from "./chart.module.css";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";

function DonutChart(props) {
  const [age, setAge] = React.useState("");

  const handleChange = (event) => {
    setAge(event.target.value);
  };

  const series = [
    {
      name: "Inflation",
      data: [2.3, 3.1, 4.0, 5.7, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 10.1],
    },
  ];

  const options = {
    chart: {
      height: 350,
      type: "bar",
      toolbar:false
    },
    plotOptions: {
      bar: {
        borderRadius: 10,
        dataLabels: {
          position: "top", // top, center, bottom
        },
      },
    },
    dataLabels: {
      enabled: true,
      formatter: function (val) {
        return val + "%";
      },
      offsetY: -20,
      style: {
        fontSize: "12px",
        colors: ["#304758"],
      },
    },
    xaxis: {
      categories: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
      ],
      position: "top",
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
      crosshairs: {
        fill: {
          type: "gradient",
          gradient: {
            colorFrom: "#D8E3F0",
            colorTo: "#BED1E6",
            stops: [0, 100],
            opacityFrom: 0.4,
            opacityTo: 0.5,
          },
        },
      },
      tooltip: {
        enabled: false,
      },
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
    title: {
      text: "Monthly Inflation in Argentina, 2002",
      floating: true,
      offsetY: 330,
      align: "center",
      style: {
        color: "#444",
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
    <div className={styles.chartInside}>
      <div className={styles.chartTitle}>
        <h5>Total Reven</h5>
      </div>
      <Chart options={options} type="bar" series={series} height={330} />
    </div>
  );
}

export default DonutChart;
