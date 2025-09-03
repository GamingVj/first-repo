import logo from './logo.svg';
import './App.css';
import Booklist from './Booklist';
import BookList2 from './Booklist2';
import BookList3 from './Booklist3';

function App() {
  return (
    <div className="App">
      {/* <Booklist /> */}
      <h2>This is without using map </h2>
      <BookList2 />
      <h2>This is with using map </h2>
      <BookList3 />

    </div>
  );
}

export default App;
