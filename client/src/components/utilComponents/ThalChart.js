
export const data = {
    labels: ['3.0', '6.0','7.0'],
    datasets: [{
      data: [164,18,115],
      backgroundColor: [
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(255, 159, 64, 0.5)',
      ],
      borderColor: [
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
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
  
  