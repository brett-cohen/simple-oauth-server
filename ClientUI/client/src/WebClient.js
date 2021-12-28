import axios from "axios";


const getRandomFromAPI = () => {
    return axios.get("http://localhost:8001/protected_api/random")
        .then((response) => response.data)
        .catch((error) => error)
}

const getTokenFromAuth = () => {
    axios.get("http://localhost:8000/auth_server/token")
        .then((response) => {
            console.log(response)
        })
}

export {getRandomFromAPI, getTokenFromAuth}