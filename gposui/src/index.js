import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import AddOwnerUi from './screens/addOwner'
import AddBusinessUi from './screens/addBusiness'
import {BrowserRouter ,Routes , Route } from 'react-router-dom'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import { QueryClientProvider , QueryClient } from 'react-query';
import SignInUi from './screens/signUp';
import DashBoardUI from './screens/dashBoard';
const root = ReactDOM.createRoot(document.getElementById('root'));
const queryClient = new QueryClient()
root.render(
  <React.StrictMode>
  <QueryClientProvider client = {queryClient}>
    <BrowserRouter>
   
      <Routes>
      <Route exact path={"/"} element = {<SignInUi />}></Route>
      <Route exact path={"/register-owner"} element={<AddOwnerUi/>} ></Route>
      <Route exact path={"/register-business"} element={<AddBusinessUi/>} ></Route>
      <Route exact path = {"/dashboard"} element={<DashBoardUI />}></Route>
      </Routes>
    </BrowserRouter>
    </QueryClientProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
