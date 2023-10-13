import './App.css';
import React, { useState } from 'react';


function App() {

  const [formData, setFormData] = useState({
    name: '',
    email: '',
    username: '',
    password: '',
    confirmPassword: ''
  })

  const handleInputChange = (event) => {
    const {name, value} = event.target;
    setFormData({
      ...formData,
      [name]: value,
    })
  }

  const handleRegister = (event) => {
    event.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      alert('Passwords do not match')
      console.log('Passwords do not match')
      return;
    }

    fetch('http://127.0.0.1:5000/register', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      });
  };

  return (
    <div>
        <h2>Register as an Instructor here</h2>
        <form onSubmit={handleRegister} >
            <label>Full Name:</label>
            <input type="text" name='name' value={formData.name} onChange={handleInputChange} placeholder='first name' /><br /><br />
            <label>Email:</label>
            <input type="text" name='email' value={formData.email} onChange={handleInputChange} placeholder='email@email.com' /><br /><br />
            <label>Username:</label>
            <input type="text" name='username' value={formData.username} onChange={handleInputChange} placeholder='username' /><br /><br />
            <label>Password:</label>
            <input type="password" name='password' value={formData.password} onChange={handleInputChange} placeholder='password' /><br /><br />
            <label>Confirm Password:</label>
            <input type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleInputChange} placeholder="confirm password" /><br /><br />
            <button type='submit'>Register</button>
        </form>

    </div>
    );
}

export default App;
