import logo from './logo.svg';
import './App.css';
import { getSensorData,fetchAllSensorData} from './services/sensorData.service';


async function getData()
{
  let data = await fetchAllSensorData();
  return data;
}
 function App() {
  getData();

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
