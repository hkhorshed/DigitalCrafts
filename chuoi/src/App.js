import React, { Component } from 'react';
import Router from './Router';
import { NavLink } from 'react-router-dom';

import './App.css';

import HomePage from './pages/homepage'


const Navigation = (props) => <nav>
  <ul>
    <li><NavLink to='./'>Home</NavLink></li>
    <li><NavLink to='./cart'>Cart</NavLink></li>
  </ul>
</nav> 

class App extends Component {
  render() {
    return (
      <div className="App">
        <Navigation />


        <Router />
      </div>
    );
  }
}

export default App;
