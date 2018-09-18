import React, { Component } from 'react';
import './App.css';

import Navbar from './components/Navbar';
import Form from './components/ContactAdd';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Navbar />
        <br/>
      </div>
    );
  }
}

export default App;
