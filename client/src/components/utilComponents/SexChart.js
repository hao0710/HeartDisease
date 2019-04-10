
export const data = {
    labels: ['Female', 'Male',],
    datasets: [{
      label: '# female ',
      data: [96,297],
      backgroundColor: [
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
      ],
      borderColor: [
        'rgba(255,99,132,1)',
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
        // scaleLabel: {
        //   display: true,
        //   labelString: 'Age Group',
        //   fontStyle: 'bold',
        // },
        // ticks:{fontStyle:'bold',fontColor:'#000000'}
      }]
    },
    responsive: true,
    maintainAspectRatio: false,
  };
  
  