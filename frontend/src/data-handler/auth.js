const DataHandler = () => {
    const API = process.env.BACKEND_URI

    const createAccount = (username, email, password) => {
        fetch(`${API}/user`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: {
                first_name: firstName,
                last_name: lastName,
                email: email,
                password: password
            }
        }).then(res => {
            return res.json()
        }).catch(() => {
            console.error("bad connection")
        })
    }

    const getUser = (email) => {
        return fetch(`${API}/user`, {
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

    const createUser = (email, firstName, lastName) => {
        
    }
}

export default DataHandler