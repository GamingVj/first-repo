import React from 'react'

const SingleProduct = ({item}) => {
  return (
    <div>
      <h3>Id:{item.id}</h3>
      <h3>Name:{item.name}</h3>
      <img src= {item.image} alt='Img Not Found' width="200px"/>
      <h3>Price:{item.price}</h3>
    </div>
  )
}

export default SingleProduct
