import React, { useEffect, useRef, useState } from 'react'
import './TitleCards.css'
import cards_data from '../../assets/cards/Cards_data'
import {Link} from 'react-router-dom'



const TitleCards = ({title, category}) => {

  const [apiData, setApiData] = useState({});

  const cardsRef = useRef();

  const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZjQ2NzA0MzNiOWM2NmVjODAxYmM4YmUxZWIwMzlhMiIsInN1YiI6IjY2NWRiOGMyNjBlZGRkMTY5NWEwMjZhYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.x48FUJDKeJnO4C6ie_kr32Gamm6X9IcRZY-MEvvBqqg'
    }
  };

  const handleWheel = (event)=>{
    event.preventDefault();
    cardsRef.current.scrollLeft += event.deltaY
  }

  useEffect(()=>{

    fetch(`https://api.themoviedb.org/3/movie/${category?category:"now_playing"}?language=en-US&page=1`, options)
    .then(response => response.json())
    .then(response => 
      
      setApiData(response.results))
    .catch(err => console.error(err));

    cardsRef.current.addEventListener('wheel',handleWheel)

})
  return (
    <div className='title-cards'>
      <h2>{title?title:"Popular on CSFlix"}</h2>
      <div className="card-list" ref={cardsRef}>
        {cards_data.map((card,index)=>{
          return <Link to={`/details/${card.id}`} className="card" key={index}>
            {/* <img src={'https://image.tmdb.org/t/p/w500'+card.backdrop_path} alt="" />
            <p>{card.original_title}</p>  */}
            <img src={card.image} alt="" />
            <p>{card.name}</p>
          </Link>
        })}
      </div>
    </div>
  )
}

export default TitleCards



