import React from 'react'
import './Home.css'
import Navbar from '../../components/NavBar/Navbar'
import Footer from '../../components/Footer/Footer'
import { useParams } from 'react-router-dom'

const Home = () => {
  const { iduser } = useParams();
  console.log('iduser:', iduser);
  return (
    <div className='home' >
      <Navbar iduser={iduser}/>
      
      <Footer/>
    </div>
  )
}


export default Home ;
