import axios from 'axios';
import { logHTTPError } from './logger.js';

const API = 'http://localhost:5000';

/* Functions for User */
export const userLogin = async (email, password) => {
  axios
    .post(`${API}/user/login`, { email, password })
    .then((res) => {
      return res;
    })
    .catch((error) => {
      logHTTPError(error);
    });
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
    .catch((error) => {
      logHTTPError(error);
    });
};

/* Functions for Accounts */
export const getAllAccounts = async () => {
  return axios
    .get(`${API}/account`)
    .then((res) => {
      return res;
    })
    .catch((error) => {
      logHTTPError(error);
    });
};

export const createNewAccount = async (name) => {
  return axios
    .post(`${API}/account`, {
      name: name,
    })
    .then((res) => {
      return res;
    })
    .catch((error) => {
      logHTTPError(error);
    });
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
    .catch((error) => {
      logHTTPError(error);
    });
}


export const getAllTransactions = async (account_id) => {
  return axios
    .get(`${API}/account/${account_id}/transaction`)
    .then((res) => {
      return res;
    })
    .catch((error) => {
      logHTTPError(error);
    });
}