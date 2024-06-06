import React, { useEffect, useRef, useState } from 'react'
import './TitleCards.css'
import cards_data from '../../assets/cards/Cards_data'
import {Link} from 'react-router-dom'



const TitleCards = ({title, category}) => {

  const [movies, setMovies] = useState([]);

  const cardsRef = useRef();

  const handleWheel = (event)=>{
    event.preventDefault();
    cardsRef.current.scrollLeft += event.deltaY
  }

  useEffect(()=>{

    const fetchMovies = async () => {
      try {
        const response = await fetch('http://localhost:8000/movies');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setMovies(data.movies); // Assurez-vous que c'est bien un tableau de films
      } catch (error) {
        console.error('Error fetching movies:', error);
      }
    };

    fetchMovies();

    cardsRef.current.addEventListener('wheel',handleWheel)

})
  return (
    <div className='title-cards'>
      <h2>{title?title:"Popular on CSFlix"}</h2>
      <div className="card-list" ref={cardsRef}>
        {movies.map((movie,index)=>{
          return <Link to={`/details/${movie.id}`} className="card" key={index}>
            <img src={'https://image.tmdb.org/t/p/w500'+movie.backdrop_path} alt="" />
            <p>{movie.original_title}</p> 
            {/* <img src={card.image} alt="" />
            <p>{card.name}</p> */}
          </Link>
        })}
      </div>
    </div>
  )
}

export default TitleCards



