import { auth_subject, status_subject } from '~/observables';

import Axios from 'axios';

const address = 'http://localhost:5000'; // TODO: use process env
export const axios = Axios.create();

/**
 * Converts an object of query paremeters to a valid query string
 *
 * @param {Object} query_parameters
 * @returns {string} The query string
 */
const parse_query_parameters = (query_parameters) => {
  let query_string = '';
  query_string += '?';
  for (const [key, value] of Object.entries(query_parameters)) {
    if (Array.isArray(value)) {
      query_string += `${key}=${JSON.stringify(value)}&`;
    } else if (value != null) {
      query_string += `${key}=${value}&`;
    }
  }

  query_string = query_string.substring(0, query_string.length - 1);
  return query_string;
};

/**
 * Handles any axios exception
 * https://stackoverflow.com/questions/49967779/axios-handling-errors
 *
 * @param {any} error The error object
 */
export const handle_axios_exception = (error) => {
  if (error.response) {
    // Request made and server responded
    if (error.response.status === 440) {
      auth_subject.next({ status: 'ERROR' });
      throw new Error(
        'Login credentials expired. Please login again to refresh your session',
      );
    }

    status_subject.next(error.response.data);
    throw new Error(error.response.data.message);
  } else if (error.request) {
    // The request was made but no response was received
    console.log('The request was made but no response was made');
    console.log(error.request);
    throw new Error(
      'Router API: Failed to connect to Router API. Make sure mars-gateway is running on docker. If this issue persists, please restart the app.',
    );
  } else {
    // Something happened in setting up the request that triggered an Error
    console.log('Request Setup Error', error.message);
    throw new Error(error.message); // TODO: haven't tested
  }
};

/**
 * Makes a GET request to the backend at the specified route with the specified query parameters
 *
 * @param {string} path The relative path to the desired endpoint
 * @param {Object} query_parameters The object with the query parameters
 * @returns {any} The GET request response
 */
export const get_request = (path, query_parameters = {}) => {
  return axios
    .get(address + path + parse_query_parameters(query_parameters), {
      headers: { authorization: localStorage.getItem('user.token') },
    })
    .catch(handle_axios_exception);
};

/**
 * Makes a PATCH request to the backend at the specified route with the specified query parameters
 *
 * @param {string} path The relative path to the desired endpoint
 * @param {Object} patch_body The body of the request
 * @param {Object} query_parameters The object with the query parameters
 * @returns {any} The PUT request response
 */
export const patch_request = (path, patch_body = {}, query_parameters = {}) => {
  return axios
    .patch(
      address + path + parse_query_parameters(query_parameters),
      patch_body,
      {
        headers: { authorization: localStorage.getItem('user.token') },
      },
    )
    .catch(handle_axios_exception);
};

/**
 * Makes a POST request to the backend at the specified route with the specified query parameters
 *
 * @param {string} path The relative path to the desired endpoint
 * @param {Object} post_body The body of the request
 * @param {Object} query_parameters The object with the query parameters
 * @returns {any} The POST request response
 */
export const post_request = (path, post_body = {}, query_parameters = {}) => {
  return axios
    .post(
      address + path + parse_query_parameters(query_parameters),
      post_body,
      {
        headers: { authorization: localStorage.getItem('user.token') },
      },
    )
    .catch(handle_axios_exception);
};

/**
 * Makes a PUT request to the backend at the specified route with the specified query parameters
 *
 * @param {string} path The relative path to the desired endpoint
 * @param {Object} put_body The body of the request
 * @param {Object} query_parameters The object with the query parameters
 * @returns {any} The PUT request response
 */
export const put_request = (path, put_body = {}, query_parameters = {}) => {
  return axios
    .put(address + path + parse_query_parameters(query_parameters), put_body, {
      headers: { authorization: localStorage.getItem('user.token') },
    })
    .catch(handle_axios_exception);
};

/**
 * Makes a DELETE request to the backend at the specified route with the specified query parameters
 *
 * @param {string} path The relative path to the desired endpoint
 * @param {Object} query_parameters The object with the query parameters
 * @returns {any} The DELETE request response
 */
export const delete_request = (path, query_parameters = {}) => {
  return axios
    .delete(address + path + parse_query_parameters(query_parameters), {
      headers: { authorization: localStorage.getItem('user.token') },
    })
    .catch(handle_axios_exception);
};
