export const logHTTPError = (error) => {
  let msg = '';
  if (error.response) {
    // Request made and server responded
    console.error(error.response.data);
    console.error(error.response.status);
    console.error(error.response.headers);
    return error.response;
  } else if (error.request) {
    // The request was made but no response was received
    console.error(error.request);
    msg = error.request;
  } else {
    // Something happened in setting up the request that triggered an Error
    console.error('Error', error.message);
    msg = error.message;
  }
  throw Error(msg)
};
