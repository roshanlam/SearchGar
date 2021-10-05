import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {Flip, ToastContainer} from 'react-toastify';
import {HelmetProvider} from 'react-helmet-async';
import 'normalize.css';
import 'react-toastify/dist/ReactToastify.css';
import 'styles/main.scss';
import 'core-js/es/map';
import 'core-js/es/set';
import 'raf/polyfill';

ReactDOM.render(
  <React.StrictMode>
      <HelmetProvider>
          <App/>
      </HelmetProvider>
      <ToastContainer
      autoClose={3000}
      closeOnClick
      draggable
      hideProgressBar
      newestOnTop
      pauseOnFocusLoss
      pauseOnHover
      position="top-right"
      rtl={false}
      transition={Flip}
      />
  </React.StrictMode>,
  document.getElementById('root')
);
