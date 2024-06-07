import React, { useEffect, useState } from 'react';
import './Details.css';
import back_arrow_icon from '../../assets/back_arrow_icon.png';
import { useNavigate, useParams } from 'react-router-dom';
import like_icon from '../../assets/like.png';
import dislike_icon from '../../assets/dislike.png';
import axios from 'axios';


const Details = () => {

  const { iduser, idmovie } = useParams();

  const navigate = useNavigate();


  const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZjQ2NzA0MzNiOWM2NmVjODAxYmM4YmUxZWIwMzlhMiIsInN1YiI6IjY2NWRiOGMyNjBlZGRkMTY5NWEwMjZhYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.x48FUJDKeJnO4C6ie_kr32Gamm6X9IcRZY-MEvvBqqg'
    }
  };

  const [apiData, setApiData] = useState({
    name: "",
    key: "",
    published_at: "",
    type: ""
  });

  useEffect(() => {
    fetch(`https://api.themoviedb.org/3/movie/${idmovie}/videos?language=en-US`, options)
      .then(response => response.json())
      .then(response => setApiData(response.results[0]))
      .catch(err => console.error(err));

  }, [idmovie]);


  const handleLike = (userId, movieId) => {
    return (event) => {
      // Prevent default behavior such as form submission or button click reload
      event.preventDefault();

  
      axios
        .post(`${import.meta.env.VITE_BACKEND_URL}/users/add_like`, { userId, movieId })
        .then((response) => {
          console.log('Film ajouté à la liste liked_movies de l\'utilisateur avec succès');
          // Vous pouvez mettre à jour l'état ici ou effectuer d'autres actions
        })
        .catch((error) => {
          console.error('Erreur lors de l\'ajout du film à la liste liked_movies de l\'utilisateur', error);
        });
    };
  };

  const handleDislike = (userId, movieId) => {
    return (event) => {
      // Prevent default behavior such as form submission or button click reload
      event.preventDefault();

  
      axios
        .post(`${import.meta.env.VITE_BACKEND_URL}/users/add_dislike`, { userId, movieId })
        .then((response) => {
          console.log('Film ajouté à la liste liked_movies de l\'utilisateur avec succès');
          // Vous pouvez mettre à jour l'état ici ou effectuer d'autres actions
        })
        .catch((error) => {
          console.error('Erreur lors de l\'ajout du film à la liste liked_movies de l\'utilisateur', error);
        });
    };
  };

  return (
    <div className='details'>
      <img src={back_arrow_icon} alt="Back" onClick={() => { navigate(-1) }} />
      <iframe width='100%' height='100%' src={`https://www.youtube.com/embed/${apiData.key}`}
        title='trailer' frameBorder='0' allowFullScreen></iframe>
      <div className="details-info">
        <p className='Like' onClick={handleLike(iduser,idmovie)} >:) Like</p>
        <p>{apiData.name}</p>
        <p className='DisLike' onClick={handleDislike(iduser,idmovie)}>:( DisLike </p>
      </div>
    </div>
  );
}



export default Details;
