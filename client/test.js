const axios = require('axios')

const testFlaskAPI = () => {
    const path = 'http://github_api:2064/trending';
    axios.get(path)
      .then((res) => {
        const data = res.data
        // console.log(data.items[0].built_by)
        console.log(data)
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      })
}
testFlaskAPI()