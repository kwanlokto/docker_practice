const API = process.env.BACKEND_URI

/* Functions for Accounts */
export const getAllAccounts = async () => {
    const user = localStorage.getItem('user.token')

    return fetch(`${API}/user/${user.id}/account`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        }
    }).then(res => {
        return res.json()
    }).catch(() => {
        console.error("bad connection")
    })
}

export const createNewAccount = async (username, password) => {
    const user = localStorage.getItem('user.token')

    return fetch(`${API}/user/${user.id}/account`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: {
            username: username,
            password: password
        }
    }).then(res => {
        return res.json()
    }).catch(() => {
        console.error("bad connection")
    })
}

export const accountLogin = async (username, password) => {
    const user = localStorage.getItem('user.token')

    return fetch(`${API}/user/${user.id}/account/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: {
            username: username,
            password: password
        }
    }).then(res => {
        return res.json()
    }).catch(() => {
        console.error("bad connection")
    })
}

/* Functions for User */
export const userLogin = async (email) => {
    return fetch(`${API}/user/login`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
        body: {
            email: email,
        }
    }).then(res => {
        return res.json()
    }).catch(() => {
        console.error("bad connection")
    })
}

export const userSignup = async (email, firstName, lastName) => {
    fetch(`${API}/user/signup`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: {
            first_name: firstName,
            last_name: lastName,
            email: email,
        }
    }).then(res => {
        return res.json()
    }).catch(() => {
        console.error("bad connection")
    })
}