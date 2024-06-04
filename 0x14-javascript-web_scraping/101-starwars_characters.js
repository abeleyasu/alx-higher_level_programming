#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API to get the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  // Function to get character names in order
  const getCharacterNames = (index) => {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.error(err);
      } else {
        const character = JSON.parse(charBody);
        console.log(character.name);
        getCharacterNames(index + 1);
      }
    });
  };

  // Start fetching character names
  getCharacterNames(0);
});
