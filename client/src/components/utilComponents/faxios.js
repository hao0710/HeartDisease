// export const data1= {
//     data: [{
//         x: 1,
//         y: 145,
//       },
//       {
//         x: 1,
//         y: 160,
//       },
//       {
//         x: 1,
//         y: 120,
//       }]
// };

export const data1= {
    
    data: [{
        x: 1,
        y: 145,
      },
      {
        x: 1,
        y: 160,
      },
      {
        x: 1,
        y: 120,
      }],

    methods: {
        getMessage() {
        const path = 'http://localhost:5000/datasets/blood';
        axios.get(path)
            .then((res) => {
            this.data = res.data.datasets;
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
        },
    },
    created () {
        getMessage();
    },
};
    