#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (error, response, responseBody) => {
    if (error) {
      console.log(error);
    }
    const charactersURLs = JSON.parse(responseBody).characters;
    const charactersNamesPromises = charactersURLs.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseError, promiseResponse, charactersBody) => {
          if (promiseError) {
            reject(promiseError);
          }
          resolve(JSON.parse(charactersBody).name);
        });
      }));

    Promise.all(charactersNamesPromises)
      .then(names => console.log(names.join('\n')))
      .catch(allErrors => console.log(allErrors));
  });
}
