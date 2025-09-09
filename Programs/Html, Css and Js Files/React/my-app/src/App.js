import logo from './logo.svg';
import './App.css';
import Booklist from './Booklist';
import BookList2 from './Booklist2';
import BookList3 from './Booklist3';
import UseStateData from './UseState/UseStateData';
import { UseStateCounter } from './UseState/UseStateCounter';
import React from 'react';
import UseStateWithArrayOfObjects from './UseState/UseStateWithArrayOfObjects';
import UseEffectGithubUsers from './UseEffect/UseEffectGithubUsers';
import ControlledInputForms from './Forms/ControlledInputForms';
import MultipleForm from './Forms/MultipleForm';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Home from './Routing/Home';
import Main from './Routing/Main';
import About from './Routing/About';

function App() {
  return (
    <div className="App">

      <BrowserRouter>
      <Routes>
        <Route path='/' element={<Main/>}>
          <Route path='/home' element={<Home/>}/>
          <Route path='/about' element={<About/>}/>
        </Route>
        </Routes>
        </BrowserRouter>
      {/* <Booklist /> */}
      <h2>This is without using map </h2>
      <BookList2 />
      <h2>This is with using map </h2>
      <BookList3 />
      <h2>This is UseState Counter</h2>
      <useStateData />
      <UseStateCounter />
      <h2>This is UseState with Array of Objects</h2>
      <UseStateWithArrayOfObjects />
      <h2>This is UseEffect with Github Users</h2>
      <UseEffectGithubUsers />
      <h2>This is Controlled Input Forms</h2>
      <ControlledInputForms />
      <h2>This is Multiple Input Forms</h2>
      <MultipleForm />
      

    </div>
  );
}

export default App;
