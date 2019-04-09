
export const data = {
  labels: ['20-40', '40-60', '60+',],
  datasets: [{
    label: '# female normal',
    data: [5, 26, 1],
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
    label: '# female having ST-T',
    data: [0, 2, 15],
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
  },{
    label: '# female probable or definite',
    data: [0, 29, 18],
    backgroundColor: [
      'rgba(153, 102, 255, 0.5)',
      'rgba(153, 102, 255, 0.5)',
      'rgba(153, 102, 255, 0.5)',
      'rgba(153, 102, 255, 0.5)',
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
    label: '# male normal',
    data: [5, 76, 17],
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
    label: '# male having ST-T',
    data: [0, 1, 0],
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
  },{
    label: '# male probable or definite',
    data: [4, 70, 28],
    backgroundColor: [
      'rgba(153, 102, 255, 0.5)',
      'rgba(153, 102, 255, 0.5)',
      'rgba(153, 102, 255, 0.5)',
      'rgba(153, 102, 255, 0.5)',
    ],
    borderColor: [
      'rgba(54, 162, 235, 1)',
      'rgba(54, 162, 235, 1)',
      'rgba(54, 162, 235, 1)',
      'rgba(54, 162, 235, 1)',
    ],
    borderWidth: 3,
  },],
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

