import { API } from 'aws-amplify'

export async function getSensorData(time) {
  let data = await API.get('dashboardapi', '/sensorData/' + time, {
  }).then(resp => {
    console.log(resp);
    return resp;
  }).catch(err => {
    console.log('Errrorr');
    console.log(err);
  });
  console.log(data);
  return data;
}