import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import ContextWrapper from "./Context/ContextWrapper";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <ContextWrapper>
      <App />
    </ContextWrapper>
  </React.StrictMode>
);

