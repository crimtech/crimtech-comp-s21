import logo from './logo.svg';
import './App.css';
import React from 'react';


class Panel extends React.Component {
  constructor(props) {
    super(props);
    this.state = { start_time: 0, ran_once: false, counting: false, true_duration: 0, reaction_time: 0, color: 'green'};
    this.process_click = this.process_click.bind(this);
    this.handle_color = this.handle_color.bind(this);
  
  }
  handle_color = (c) => {
    // TODO: Your code here!
    this.setState({color:c})
  }
  getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
  }

  start_count() {
    // TODO: Your code here!
    this.start_time = window.performance.now()
    console.log("start time: " + this.start_time)
    this.true_duration= 2
    // this.true_duration = this.getRandomInt(2, 7)
    // console.log("true_duration: " + this.true_duration)
    this.setState({counting:true});
    // console.log("counting [start_count]: " + this.counting)
    this.setState({color:"darkred"})
    setTimeout(this.handle_color, 3000, "green")
  }

  toSeconds = (s) => {
    // console.log("s: " + s)
    return s/100000
  }

  end_count() {
    // TODO: Your code here!
    
    // console.log("end_count running")
    if ( (window.performance.now() - this.start_time) > this.true_duration ){ //will run if button is clicked AFTER it turns green
        // console.log("here")
        this.ran_once = true
        this.setState({counting:false});
        
        this.setState({reaction_time: (window.performance.now() - this.true_duration*1000 - this.start_time) } ) 
        console.log("reaction_time: " + this.reaction_time)
        console.log("start_time: " + this.start_time)
        console.log("true duration: " + this.true_duration)
        console.log("current time: " + window.performance.now())
    }
  }
  process_click() { 
    console.log("counting [process_click]: " + this.state.counting)  
    if (this.state.counting) { //we start out not counting
      console.log("stop1")
      this.end_count();
      
    } else {
      this.start_count();
      console.log("stop2")
    }

  }
  render() {
    let msg = "Hello World!";
    // console.log("counting[render]: " + this.state.counting)
    // console.log("color[render]: " + this.state.color)
    if (this.state.counting && this.state.color === "darkred"){
      msg = "wait for green"
    }

    else if (this.state.counting && this.state.color === "green"){
      msg = "Click!"
    }

    else if (this.ran_once){
      msg = "your reaction time is " + this.state.reaction_time + " ms"
    }

    else{
      msg = "Click me to begin!"
    }
    return (
      <div className = "PanelContainer" onClick = {this.process_click} style={ { background: this.state.color}}>
        <div className = "Panel">{msg}</div>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className =  "Header">How Fast is your Reaction Time?</h1>
        <Panel />
        <p>Click as soon as the red box turns green. Click anywhere in the box to start.</p>
    
        
      </header>
    </div>
  );
}

export default App;
