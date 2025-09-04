import logo from './logo.svg';
import './App.css';
import Booklist from './Booklist';
import BookList2 from './Booklist2';
import BookList3 from './Booklist3';
import UseStateData from './UseState/UseStateData';
import { UseStateCounter } from './UseState/UseStateCounter';
import React from 'react';
import UseStateWithArrayOfObjects from './UseState/UseStateWithArrayOfObjects';


function App() {
  return (
    <div className="App">
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
      

    </div>
  );
}

export default App;
