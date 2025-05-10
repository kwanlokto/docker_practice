// components/ProtectedRoute.tsx

import { Redirect, Route } from 'react-router-dom';

import React from 'react';
import { jwtDecode } from 'jwt-decode';

const isTokenValid = (token) => {
    try {
      const { exp } = jwtDecode<{ exp }>(token);
      return exp * 1000 > Date.now();
    } catch {
      return false;
    }
  };
  
export const ProtectedRoute = ({ component: Component, ...rest }) => {
  const token = localStorage.getItem('user.token');

  // You could also add token expiry checks here if needed
  const isAuthenticated = !!token;

  return (
    <Route
      {...rest}
      render={props =>
        isAuthenticated ? (
          <Component {...props} />
        ) : (
          <Redirect to="/login" />
        )
      }
    />
  );
};
