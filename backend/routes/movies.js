import express from 'express';
import { appDataSource } from '../datasource.js';
import Movie from '../entities/movie.js';

const router = express.Router();

router.get('/', function (req, res) {
  appDataSource
  .getRepository(Movie)
  .find({})
  .then(function (movies) {
    res.json({ movies: movies });
  });
});


router.get('/:id', function (req, res) {
  appDataSource
  .getRepository(Movie)
  .find({id: req.params.userId })
  .then(function () {
    res.json(Movie[req.params.userId])
    res.status(204).json({ message: 'HTTP 200 OK' });
  })
  .catch(function () {
    res.status(500).json({ message: 'HTTP 404 NOT FOUND' });
  });
});

router.post('/new', function (req, res) {

  const movieRepository = appDataSource.getRepository(Movie);
  const newMovie = movieRepository.create({
    id : req.body.id,
    original_title: req.body.original_title,
    release_date: req.body.release_date,
    backdrop_path: req.body.backdrop_path,
    original_language: req.body.original_language,
    genre_ids: req.body.genre_ids,
    key: req.body.key,
  });

  movieRepository
  .save(newMovie)
  .then(function (savedMovie) {
    res.status(201).json({
      message: 'Movie successfully created',
      id: savedMovie.id,
    });
  })
  .catch(function (error) {
    console.error(error);
    if (error.code === '23505') {
      res.status(400).json({
        message: `User with name "${newMovie.name}" already exists`,
      });
    } else {
      res.status(500).json({ message: 'Error while creating the Movie' });
    }
  });
});   



export default router;