// components/ProtectedRoute.tsx

import { Redirect, Route } from 'react-router-dom';

export const ProtectedRoute = ({ component: Component, ...rest }) => {
  const token = localStorage.getItem('user.token');

  // You could also add token expiry checks here if needed
  const isAuthenticated = !!token;

  return (
    <Route
      {...rest}
      render={(props) =>
        isAuthenticated ? <Component {...props} /> : <Redirect to="/login" />
      }
    />
  );
};
