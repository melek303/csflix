import axios from 'axios';

const getAllUsers = async () => {
  try {
    const response = await axios.get(`${import.meta.env.VITE_BACKEND_URL}/users`);
    return response.data.users; // Assurez-vous que la réponse contient une liste d'utilisateurs
  } catch (error) {
    console.error('Erreur lors de la récupération des utilisateurs', error);
    return [];
  }
};

const getLikedMovies = async (userId) => {
    try {
      const users = await getAllUsers();
      const user = users.find(user => user.id === userId);
      if (!user) {
        console.error(`Utilisateur avec l'ID ${userId} introuvable`);
        return [];
      }
      return user.liked_movies; // Retourne la liste des films aimés par l'utilisateur
    } catch (error) {
      console.error('Erreur lors de la récupération des films aimés', error);
      return [];
    }
  };


const getDislikedMovies = async (userId) => {
    try {
      const users = await getAllUsers();
      const user = users.find(user => user.id === userId);
      if (!user) {
        console.error(`Utilisateur avec l'ID ${userId} introuvable`);
        return [];
      }
      return user.liked_movies; // Retourne la liste des films aimés par l'utilisateur
    } catch (error) {
      console.error('Erreur lors de la récupération des films aimés', error);
      return [];
    }
  };


    // Fonction pour calculer la similarité entre deux films
    const calculateSimilarity = (movieA, movieB) => {
    const genresA = new Set(movieA.genre_ids);
    const genresB = new Set(movieB.genre_ids);

    const intersection = new Set([...genresA].filter(genre => genresB.has(genre)));
    const union = new Set([...genresA, ...genresB]);

    return intersection.size / union.size;
    };

    const calculateAverageSimilarity = (targetMovie, likedMovies) => {
        const totalSimilarity = likedMovies.reduce((acc, likedMovie) => {
        return acc + calculateSimilarity(targetMovie, likedMovie);
        }, 0);
        return totalSimilarity / likedMovies.length;
    };

  const updateRecommendedMovies = (updatedLikedMovies,updatedislikedMovies) => {
    if (updatedLikedMovies.length === 0) {
      setRecommendedMovies([]);
      return;
    }

    const likedMoviesObjects = movies.filter(movie => updatedLikedMovies.includes(movie.id));
    const similarities = movies
      .filter(movie => !updatedLikedMovies.includes(movie.id) && !updatedislikedMovies.includes(movie.id))
      .map(movie => ({
        ...movie,
        similarity: calculateAverageSimilarity(movie, likedMoviesObjects)
      }))
      .sort((a, b) => b.similarity - a.similarity);

    setRecommendedMovies(similarities);
  };

  const handleLike = (movieId) => {
    const likedMovie = movies.find(movie => movie.id === movieId);

    if (likedMovie) {
      if (!likedMovies.includes(movieId)) {
        const updatedLikedMovies = [...likedMovies, movieId];
        setLikedMovies(updatedLikedMovies);
        setDislikedMovies(dislikedMovies.filter(id => id !== movieId));

        // Recalculate recommended movies
        updateRecommendedMovies(updatedLikedMovies,dislikedMovies);
      } else {
        const updatedLikedMovies = likedMovies.filter(id => id !== movieId);
        setLikedMovies(updatedLikedMovies);

        // Recalculate recommended movies
        updateRecommendedMovies(updatedLikedMovies,dislikedMovies);
      }
    }
  };

    const handleDislike = (movieId) => {
      if (!dislikedMovies.includes(movieId)) {
        const updateddislikedMovies = [...dislikedMovies, movieId]
        setDislikedMovies(updateddislikedMovies)
        setLikedMovies(likedMovies.filter(id => id !== movieId));
        
        // Recalculate recommended movies
        updateRecommendedMovies(likedMovies.filter(id => id !== movieId),updateddislikedMovies);
        
      } else {
        const updateddislikedMovies=dislikedMovies.filter(id => id !== movieId)
        setDislikedMovies(updateddislikedMovies);
        updateRecommendedMovies(likedMovies,updateddislikedMovies)
      }
    };

  const isLiked = (movieId) => likedMovies.includes(movieId);
  const isDisliked = (movieId) => dislikedMovies.includes(movieId);