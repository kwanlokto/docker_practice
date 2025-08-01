import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';

import { AccountDetail } from './routes/Account';
import { Dashboard } from './routes/Dashboard';
import { Login } from './routes/Login';
import { ProtectedRoute } from './routes/ProtectedRoute';
import { SignUp } from './routes/SignUp';

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
