const axios = require('axios')

const response = {}
async function testFlaskAPI() {
    const path = 'http://github_api:2064/api/trending';
    return axios.get(path)
      .then((res) => {
        const data = res.data
        console.log(`REQUEST COMPLETE ! STATUS CODE: ${data.status_code}`)
        // console.log(data.items[0].built_by)
        return data

      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        return {}
      })
}
async function results(){
  response.data = await testFlaskAPI()
  console.log(response)
}
results()