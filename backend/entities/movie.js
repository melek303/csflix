import typeorm from 'typeorm';

const Movie = new typeorm.EntitySchema({
  name: 'movie',
  columns: {
    id: {
      primary: true,
      type: Number,
      unique: true,
    },
    original_title: {
      type: String,
    },
    release_date: {
        type: String,
    },

    backdrop_path: {
        type: String,
    },

    original_language: {
        type: String,
    },

    genre_ids: {
        type: String,
    },

    key: {
        type: String,
    },

  },
});

export default Movie;
