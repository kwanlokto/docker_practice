import { axios_delete, axios_get, axios_post } from './base';

/* Functions for User */
export const userLogin = async (email, password) => {
  return axios_post('/user/login', { email, password });
};

export const userSignup = async (email, password, firstName, lastName) => {
  return axios_post('/user/signup', {
    first_name: firstName,
    last_name: lastName,
    email: email,
    password: password,
  });
};

/* Functions for Accounts */
export const getAllAccounts = async () => {
  return axios_get('/account');
};

export const createNewAccount = async (name) => {
  return axios_post('/account', {
    name: name,
  });
};

export const deleteAccount = async (account_id) => {
  return axios_delete(`/account/${account_id}`);
};

export const createTransaction = async (account_id, operation, value) => {
  return axios_post(`/account/${account_id}/transaction`, {
    operation: operation,
    value: value,
  });
};

export const getAllTransactions = async (account_id) => {
  return axios_get(`/account/${account_id}/transaction`);
};
