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
  const user = localStorage.getItem('user.token');

  return axios
    .get(`${API}/user/${user.id}/account`)
    .then((res) => {
      return res;
    })
    .catch((error) => {
      logHTTPError(error);
    });
};

export const createNewAccount = async (username, password) => {
  const user = localStorage.getItem('user.token');

  return axios
    .post(`${API}/user/${user.id}/account`, {
      username: username,
      password: password,
    })
    .then((res) => {
      return res;
    })
    .catch((error) => {
      logHTTPError(error);
    });
};
