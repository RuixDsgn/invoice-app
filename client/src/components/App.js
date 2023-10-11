import './App.css';
import React, { useState } from 'react';


function App() {

  const [formData, setFormData] = useState({
    name: '',
    email: '',
    username: '',
    password: ''
  })

  const handleInputChange = (event) => {
    const {name, value} = event.target;
    setFormData({
      ...formData,
      [name]: value,
    })
  }

  const handleSubmit = (event) => {
    event.preventDefault()

    fetch('/', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(formData)
    })
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
    })
  }

  const handleRegister = (event) => {
    event.preventDefault()
    const formData = new FormData(event.target)
    const data = {}
    formData.forEach((value, key) => {
      data[key] = value
    })
    console.log("Register form data:", data)
  }

  return (
    <div>
        <h2>Register as an Instructor here</h2>
        <form onSubmit={handleRegister} >
            <label>Name:</label>
            <input type="text" name='name' value={formData.name} onChange={handleInputChange} placeholder='name' /><br /><br />
            <label>Email:</label>
            <input type="text" name='email' value={formData.email} onChange={handleInputChange} placeholder='email@email.com' /><br /><br />
            <label>Username:</label>
            <input type="text" name='username' value={formData.username} onChange={handleInputChange} placeholder='username' /><br /><br />
            <label>Password:</label>
            <input type="text" name='password' value={formData.password} onChange={handleInputChange} placeholder='password' /><br /><br />
            <button type='submit' onClick={handleSubmit}>Register</button>
        </form>

    </div>
    );
}

export default App;
