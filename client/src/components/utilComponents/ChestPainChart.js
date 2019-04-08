
export const data = {
  labels: ['20-40', '40-60', '60+',],
  datasets: [{
    label: '# female typical',
    data: [1, 2, 3, 4, 5, 6],
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
    data: [7, 8, 9, 10, 11, 12],
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
    data: [13, 14, 15, 16, 17, 18],
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
    data: [19, 20, 21, 22, 23, 24],
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
    data: [1, 2, 3, 4, 5, 6],
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
    data: [7, 8, 9, 10, 11, 12],
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
    data: [13, 14, 15, 16, 17, 18],
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
    data: [19, 20, 21, 22, 23, 24],
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
    }],
  },
  responsive: true,
  maintainAspectRatio: false,
};

