#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length <= 2) {
  console.log('Usage: node get_characters_names.js <film_id>');
  process.exit(1);
}

const filmId = process.argv[2];

function fetchCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
}

request(`${API_URL}/films/${filmId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  
  const film = JSON.parse(body);
  const characterPromises = film.characters.map(fetchCharacterName);

  Promise.all(characterPromises)
    .then(names => {
      console.log(names.join('\n'));
    })
    .catch(allError => {
      console.error(allError);
    });
});
