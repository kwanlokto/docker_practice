import axios from 'axios';

const API = 'http://localhost:5000';

/* Functions for User */
export const userLogin = async (email, password) => {
  return axios
    .post(`${API}/user/login`, { email, password })
    .then((res) => {
      return res;
    })
};

export const userSignup = async (email, password, firstName, lastName) => {
  return axios
    .post(`${API}/user/signup`, {
      first_name: firstName,
      last_name: lastName,
      email: email,
      password: password,
    })
    .then((res) => {
      return res;
    })
};

/* Functions for Accounts */
export const getAllAccounts = async () => {
  return axios
    .get(`${API}/account`)
    .then((res) => {
      return res;
    })

};

export const createNewAccount = async (name) => {
  return axios
    .post(`${API}/account`, {
      name: name,
    })
    .then((res) => {
      return res;
    })
};

export const deleteAccount = async (account_id) => {
  return axios
    .delete(`${API}/account/${account_id}`)
    .then((res) => {
      return res;
    })
};

export const createTransaction = async (account_id, operation, value) => {
  return axios
    .post(`${API}/account/${account_id}/transaction`, {
      operation: operation,
      value: value,
    })
    .then((res) => {
      return res;
    })
}


export const getAllTransactions = async (account_id) => {
  return axios
    .get(`${API}/account/${account_id}/transaction`)
    .then((res) => {
      return res;
    })
}