import React from 'react'
import Home from './pages/Home/Home.jsx'
import {Routes,Route} from 'react-router-dom'
import Details from './pages/Details/Details.jsx'


const App = () => {
  return (
    <div>
      <Routes>
        <Route path='/' element={<Home/>}></Route>
        <Route path='/details/:id' element={<Details/>}></Route>
      </Routes>
    </div>
  )
}

export default App
