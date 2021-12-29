import {getRandomFromAPI, getTokenFromAuth} from "./WebClient";
import {useState} from "react";

function App(){
  const [randomNum, setRandomNum] = useState("")

  return <div>
    <button onClick={() => getRandomFromAPI().then(response => setRandomNum(response))}>Get random number</button>
    <p>Random Number: {randomNum}</p>
  </div>
}

export default App;