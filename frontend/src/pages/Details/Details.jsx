import React, { useEffect, useState } from 'react'
import './Details.css'
import back_arrow_icon from '../../assets/back_arrow_icon.png'
import { useNavigate, useParams } from 'react-router-dom'


const Details = () => {
    const {id} = useParams();

    const navigate = useNavigate();

    const options = {
        method: 'GET',
        headers: {
        accept: 'application/json',
        Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZjQ2NzA0MzNiOWM2NmVjODAxYmM4YmUxZWIwMzlhMiIsInN1YiI6IjY2NWRiOGMyNjBlZGRkMTY5NWEwMjZhYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.x48FUJDKeJnO4C6ie_kr32Gamm6X9IcRZY-MEvvBqqg'
        }
      };
    
    const [apiData, setApiData] = useState({
        name : "",
        key: "",
        published_at: "",
        typeof: ""
    });


    useEffect (()=>{
        fetch(`https://api.themoviedb.org/3/movie/${id}/videos?language=en-US`, options)
        .then(response => response.json())
        .then(response => setApiData(response.results[0]))
        .catch(err => console.error(err));
      },[])

  return (
    <div className='details'>
      <img src={back_arrow_icon} alt="" onClick={()=>{navigate(-1)}}/>
      <iframe width='90%' height='90%' src={`https://www.youtube.com/embed/${apiData.key}`}
      title = 'trailer' frameBorder='0' allowFullScreen> </iframe>
    <div className="details-info">
        <p>{apiData.published_at.slice(0,10)}</p>
        <p>{apiData.name}</p>
        <p>{apiData.type}</p>
    </div>
    </div>
  )
}

export default Details
