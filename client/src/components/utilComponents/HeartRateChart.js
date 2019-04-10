import {heartRate} from './Dataset';
export const data = {
  labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
  datasets: [{
    label: 'female',
    data:heartRate.female,
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255,99,132,1)',
    borderWidth: 3,
  },
  {
    label: 'male',
    data:heartRate.male,
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 3,
  }],
};

export const options = {
  scales: {
    xAxes: [{
      type: 'linear',
      display: true,
      position: 'bottom',
      scaleLabel: {
        display: true,
        labelString: 'Age',
        fontStyle: 'bold',
      },
      // ticks:{fontStyle:'bold',fontColor:'#000000'}
    }],
    yAxes: [{
      type: 'linear',
      display: true,
      position: 'bottom',
      scaleLabel:{
        display: true,
        labelString: 'heartRate',
        fontStyle: 'bold',
      },
  }],
  },
  responsive: true,
  maintainAspectRatio: false,
};

