import React, { useEffect, useRef, useState } from 'react'
import './Navbar.css'
import logo from '../../assets/logo.png'
import search_bar from '../../assets/search_icon.svg'
import bell_icon from '../../assets/bell_icon.svg'
import profile_img from '../../assets/profile_img.png'
import caret_icon from '../../assets/caret_icon.svg'
import { useNavigate } from 'react-router-dom'
import {Routes,Route} from 'react-router-dom'
import { Link } from 'react-router-dom'



const Navbar = () => {

  const navigate = useNavigate();

  const navRef = useRef();

  const [query, setQuery] = useState();

  const [showFilterBar, setShowFilterBar] = useState(false);

  const handleInputChange = (e) => {
    const text = e.target.value;

    setQuery(text);
    setShowFilterBar(text.trim().length > 0);
  };

  const handleSearch = () => {

  };

  useEffect(()=>{
    window.addEventListener('scroll', ()=>{
      if (window.scrollY >= 80 ){
        navRef.current.classList.add('nav-dark')
      }else{
        navRef.current.classList.remove('nav-dark')
      }
    })

  },[])

  return (
    <div ref= {navRef} className='navbar'>
      <div className="navbar-left">
        <img src={logo} alt="" onClick={()=>{navigate(0)}} />
        <ul>
            <li onClick={()=>{navigate(0)}}>Home</li>
            <Link to='/movies' >
              <li> All Movies</li>
            </Link>
        </ul>
      </div>
      <div className="navbar-right">
        <div className="search-bar">
          <input
            type="text"
            placeholder="Rechercher..."
            className="search-input"
            value={query}
            onChange={handleInputChange}
          />
          <img src={search_bar} alt="" className='icons' onClick={handleSearch} />
        </div> 
        <div className="filtrage">
          {showFilterBar && (
            <div className="filter-bar">
              
            </div>
          )}
        </div>
        <div className="navbar-profile">
          <img src={profile_img} alt="" className='profile'/>
          <img src={caret_icon} alt="" className='profile'/>
          <div className="dropdown">
            <p>Sign out of CSFlix</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Navbar
