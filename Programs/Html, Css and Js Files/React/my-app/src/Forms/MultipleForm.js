import React from 'react'

const MultipleForm = () => {
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>Controlled Input Forms</label>
        <br /><br />
        <input type="text" placeholder='Enter your name' onChange={getData} value={uname}/>
        <br /><br />
        <input type="email" placeholder='Enter your email' onChange={getData} value={email}/>
        <br /><br />
        <input type="number" placeholder='Enter your age' onChange={getData} value={age}/>
        <br /><br />
        <input type="number" placeholder='Enter your Mobile Number' onChange={getData} value={phone}/>
        <br /><br />
        <input type="submit" />
        <br /><br />
        
        </form>
        <h2>{uname}---{email}---{age}---{phone}</h2>
    </div>
  )
}

export default MultipleForm;
