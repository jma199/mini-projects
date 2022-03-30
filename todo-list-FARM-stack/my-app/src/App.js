import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import TodoView from './components/TodoListView.js';

function App() {

  const [todoList, setTodoList] = useState([{}])
  const [title, setTitle] = useState('')
  const [desc, setDesc] = useState('')

  /*useEffect allows us to read todo list from database */
  // Read all todo items
  useEffect(() => {
    axios.get('https://localhost:8000/api/todo')
      .then(res => {setTodoList(res.data)
      })
  });

  // Post a todo items
  const addTodoHandler = () => {
    axios.post('https://localhost:8000/api/todo', {'title': title, 'description': desc})
    .then(res => console.log(res))
  };

  return (
    <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{"width": "400px", "background-color": "white", "margin-top": "15px"}}>
      <h1 className="car text-white bg-primary mb-1" styleName="max-width: 20rem;">Task Manager</h1>
      <h6 className="card text-white bg-primary mb-3">FastAPI - React - MongoDB</h6>
    <div className="card-body">
      <h5 className="card text-white bg-dark mb-3">Add Your Task</h5>
      <span className="card-text">
        <input className="mb-2 form-control titleIn" onChange={event => setTitle(event.target.value)} placeholder='Title'/>
        <input className="mb-2 form-control desIn" onChange={event => setDesc(event.target.value)} placeholder='Description'/>
        <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius': '50px', "font-weight":"bold"}} onClick={addTodoHandler}>Add Task</button>
      </span>
      <h5 className="card text-white bg-dark mb-3">Your tasks</h5>
      <div>
      <TodoView todoList={todoList} />
      </div>
      </div>
      <h6 className="card text-dark bg-warning py-1 mb-0">Copyright 2022, All rights reserved &copy;</h6>
    </div>
  );
}

export default App;