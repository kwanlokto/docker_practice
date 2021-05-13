import axios from 'axios'

const API = "http://localhost:5000"

/* Functions for Accounts */
export const getAllAccounts = async () => {
    const user = localStorage.getItem('user.token')

    return axios.get(`${API}/user/${user.id}/account`).then(res => {
        return res.data
    }).catch(() => {
        console.error("bad connection")
    })
}

export const createNewAccount = async (username, password) => {
    const user = localStorage.getItem('user.token')

    return axios.post(`${API}/user/${user.id}/account`, {
        username: username,
        password: password,
    }).then(res => {
        return res.data
    }).catch(() => {
        console.error("bad connection")
    })
}

export const accountLogin = async (username, password) => {
    const user = localStorage.getItem('user.token')

    return axios.post(`${API}/user/${user.id}/account/login`, {
        username: username,
        password: password,
    }).then(res => {
        return res.data
    }).catch(() => {
        console.error("bad connection")
    })
}

/* Functions for User */
export const userLogin = async (email) => {
    axios.post(`${API}/user/login`, { email }).then(res => {
        return res.data
    }).catch(() => {
        console.error("bad connection")
    })
}

export const userSignup = async (email, firstName, lastName) => {
    return axios.post(`${API}/user/signup`, {
        first_name: firstName,
        last_name: lastName,
        email: email
    }).then(res => {
        return res.data
    }).catch(() => {
        console.error("bad connection")
    })
}