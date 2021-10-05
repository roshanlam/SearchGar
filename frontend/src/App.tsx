import React, {FC, lazy} from 'react';
import {BrowserRouter as Router, Redirect, Route, Switch} from 'react-router-dom';
import {Layout} from './components';
import {ROUTES} from './constants/routes';
import CreateAccount from './pages/CreateAccount';
import Home from './pages/Home';
import Progress from './pages/Progress';
import SignIn from './pages/SignIn';
import SignOut from './pages/SignOut';

const App: FC = () => {
  return (
      <Router>
        <Layout>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path={ROUTES.createAccount} render={() => <CreateAccount disabled />} />
            <Route path={ROUTES.homepage} component={Home}/>
            <Route path={ROUTES.progress} component={Progress} />
            <Route exact path={ROUTES.signin} component={SignIn} />
            <Route exact path={ROUTES.signout} component={SignOut} />
            <Redirect to="/" />
          </Switch>
        </Layout>
      </Router>
  );
};

export default App;