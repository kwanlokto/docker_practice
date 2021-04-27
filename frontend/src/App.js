import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';

import { Login } from './routes/Login';
import React from 'react';
import { SignUp } from './routes/SignUp'

export default function App() {
  return (
    <Router>
      <div>
        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/signup">
            <SignUp />
          </Route>
          <Route path="/">
          </Route>
        </Switch>
      </div>
    </Router>
  );
}
