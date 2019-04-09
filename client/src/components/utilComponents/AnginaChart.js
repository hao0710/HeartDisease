
export const data = {
  labels: ['20-40', '40-60', '60+',],
  datasets: [{
    label: '# female yes',
    data: [0, 15, 7],
    backgroundColor: [
      'rgba(255, 206, 86, 1)',
      'rgba(255, 206, 86, 1)',
      'rgba(255, 206, 86, 1)',
      'rgba(255, 206, 86, 1)',
    ],
    borderColor: [
      'rgba(255,99,132,1)',
      'rgba(255,99,132,1)',
      'rgba(255,99,132,1)',
      'rgba(255,99,132,1)',
    ],
    borderWidth: 3,
  },{
    label: '# female no',
    data: [5, 42, 27],
    backgroundColor: [
      'rgba(75, 192, 192, 0.5)',
      'rgba(75, 192, 192, 0.5)',
      'rgba(75, 192, 192, 0.5)',
      'rgba(75, 192, 192, 0.5)',
    ],
    borderColor: [
      'rgba(255,99,132,1)',
      'rgba(255,99,132,1)',
      'rgba(255,99,132,1)',
      'rgba(255,99,132,1)',
    ],
    borderWidth: 3,
  },
  {
    label: '# male yes',
    data: [3, 52, 20],
    backgroundColor: [
      'rgba(255, 206, 86, 1)',
      'rgba(255, 206, 86, 1)',
      'rgba(255, 206, 86, 1)',
      'rgba(255, 206, 86, 1)',
    ],
    borderColor: [
      'rgba(54, 162, 235, 1)',
      'rgba(54, 162, 235, 1)',
      'rgba(54, 162, 235, 1)',
      'rgba(54, 162, 235, 1)',
    ],
    borderWidth: 3,
  },{
    label: '# male no',
    data: [6, 95, 25],
    backgroundColor: [
      'rgba(75, 192, 192, 0.5)',
      'rgba(75, 192, 192, 0.5)',
      'rgba(75, 192, 192, 0.5)',
      'rgba(75, 192, 192, 0.5)',
    ],
    borderColor: [
      'rgba(54, 162, 235, 1)',
      'rgba(54, 162, 235, 1)',
      'rgba(54, 162, 235, 1)',
      'rgba(54, 162, 235, 1)',
    ],
    borderWidth: 3,
  }],
};

export const options = {
  scales: {
    yAxes: [{
      ticks: {
        beginAtZero: true,
      },
      scaleLabel: {
        display: true,
        labelString: 'Counting',
        fontStyle: 'bold',
      },
    }],
    xAxes: [{
      display: true,
      position: 'bottom',
      scaleLabel: {
        display: true,
        labelString: 'Age Group',
        fontStyle: 'bold',
      },
      // ticks:{fontStyle:'bold',fontColor:'#000000'}
    }]
  },
  responsive: true,
  maintainAspectRatio: false,
};

