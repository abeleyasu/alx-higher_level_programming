#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];
const wedgeAntillesId = '18';

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;

    // Iterate through the films and check for Wedge Antilles presence
    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    });

    // Print the number of films where Wedge Antilles is present
    console.log(count);
  }
});
