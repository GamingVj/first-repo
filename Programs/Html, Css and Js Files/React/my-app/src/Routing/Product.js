import React from 'react'
import { useState } from 'react'
import {ProductsInfo} from './ProductsInfo'
import SingleProduct from './SingleProduct'

const Product = () => {
    var [items, setItems] = useState(ProductsInfo)
  return (
    <div>
        {items.map((item)=>{
            return (<SingleProduct item={item}/>)
        })}
      
    </div>
  )
}

export default Product
