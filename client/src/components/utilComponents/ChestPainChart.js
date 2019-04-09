
export const data = {
  labels: ['20-40', '40-60', '60+',],
  datasets: [{
    label: '# female typical',
    data: [0, 2, 2],
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
    label: '# female atypical',
    data: [1, 14, 3],
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
    label: '# female non-anginal',
    data: [1, 19, 12],
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
    label: '# female asymptomatic',
    data: [3, 22, 17],
    backgroundColor: [
      'rgba(255, 159, 64, 0.5)',
      'rgba(255, 159, 64, 0.5)',
      'rgba(255, 159, 64, 0.5)',
      'rgba(255, 159, 64, 0.5)',

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
    label: '# male typical',
    data: [2, 11, 6],
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
    label: '# male atypical',
    data: [2, 25, 4],
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
    label: '# male non-anginal',
    data: [2, 38, 9],
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
  },
  {
    label: '# male asymptomatic',
    data: [3, 73, 26],
    backgroundColor: [
      'rgba(255, 159, 64, 0.5)',
      'rgba(255, 159, 64, 0.5)',
      'rgba(255, 159, 64, 0.5)',
      'rgba(255, 159, 64, 0.5)',

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

