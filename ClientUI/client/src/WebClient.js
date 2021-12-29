import axios from "axios";


const getRandomFromAPI = () => {
    return axios.get("http://localhost:8001/protected_api/random")
        .then((response) => response.data)
        .catch((error) => error)
}

export {getRandomFromAPI}