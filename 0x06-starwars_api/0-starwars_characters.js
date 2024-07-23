#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  
  // Step 1: Fetch movie details
  request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err) {
      console.log(err);
      return;
    }
    
    // Parse movie data to get character URLs
    const movie = JSON.parse(body);
    const charactersURLs = movie.characters;
    
    // Step 2: Fetch character names
    const characterRequests = charactersURLs.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (err, _, characterBody) => {
          if (err) {
            reject(err);
          } else {
            const character = JSON.parse(characterBody);
            resolve(character.name);
          }
        });
      });
    });
    
    // Step 3: Resolve promises and print character names
    Promise.all(characterRequests)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(err => {
        console.log(err);
      });
  });
}
