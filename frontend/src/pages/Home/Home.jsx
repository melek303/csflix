import React from 'react'
import './Home.css'
import Navbar from '../../components/NavBar/Navbar'
import hero_banner from '../../assets/hero_banner.jpg'
import hero_title from '../../assets/hero_title.png'
import play_icon from '../../assets/play_icon.png'
import info_icon from '../../assets/info_icon.png'
import TitleCards from '../../components/TitleCards/TitleCards'
import Footer from '../../components/Footer/Footer'

const Home = () => {
  return (
    <div className='home'>
      <Navbar/>
      <div className="for-you-cards">
        <TitleCards title={"Selected for you"} />
      </div>
      <div className="more-cards">
        <TitleCards title={"BlockbusterMovie"} category={"top_rated"}/>
        <TitleCards title={"Only on CSFlix"} category={"popular"}/>
        <TitleCards title={"Upcoming"} category={"upcoming"}/>
      </div>
      <Footer/>
    </div>
  )
}

export default Home;
