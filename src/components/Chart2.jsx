// label={staticData[0].time} data1={staticData[0].TrainData} data2={staticData[0].testData}
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
  } from "chart.js";
  import { Line } from "react-chartjs-2";
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );

  import staticData from "./../data/static.json"
  
  const labels = staticData[1].time;
  
  const options = {
    plugins: {
      legend: {
        position: "bottom",
      },
    },
  };
  
  export const data = {
    labels,
    datasets: [
      {
        label: "AI trainer's angle variations",
        data: staticData[1].TrainData,
        backgroundColor: "#2196F3",
        borderColor: "#2196F3",
        pointRadius: 0,
      },
      {
        label: "User's angle variations",
        data: staticData[1].testData,
        backgroundColor: "#F44236",
        borderColor: "#F44236",
        pointRadius: 0
      },
    ],
  };
  
  const ChartJsExample = () => {
    return (
      <div style={{ width: 600, height: 300, backgroundColor: "white", borderRadius: "16px", padding: "2rem", boxShadow:"rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;"}}>
        <Line options={options} data={data} />
      </div>
    );
  };
  
  export default ChartJsExample;