#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const data = JSON.parse(body);
    // Print the title of the movie
    console.log(data.title);
  }
});
