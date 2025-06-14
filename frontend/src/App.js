import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';

import { AccountDetail } from './routes/Account';
import { Dashboard } from './routes/Dashboard';
import { Login } from './routes/Login';
import { ProtectedRoute } from './routes/ProtectedRoute';
import { SignUp } from './routes/SignUp';
import axios from 'axios';

const apiUrl = 'http://localhost:5000'; // TODO: use process env

// Adds user.token to the request header
axios.interceptors.request.use(
  (config) => {
    const { origin } = new URL(config.url);
    const allowedOrigins = [apiUrl];
    const token = localStorage.getItem('user.token');
    if (allowedOrigins.includes(origin) && token) {
      config.headers.authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error),
);

export default function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/signup">
            <SignUp />
          </Route>

          {/* Default route */}
          <ProtectedRoute exact path="/" component={Dashboard} />
          <ProtectedRoute path="/account/:accountId" component={AccountDetail} />
        </Switch>
      </div>
    </Router>
  );
}
