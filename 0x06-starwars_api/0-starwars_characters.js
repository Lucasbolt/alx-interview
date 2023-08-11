#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

async function getCharactersNames(filmId) {
    const charactersUrl = `${API_URL}/films/${filmId}/characters`;
    const charactersResponse = await request(charactersUrl);
    if (charactersResponse.statusCode !== 200) {
        throw new Error(`Error getting characters for film ${filmId}: ${charactersResponse.text}`);
    }

    const charactersJson = await charactersResponse.json();
    const charactersNames = charactersJson.map(character => character.name);
    return charactersNames;
}

if (process.argv.length < 3) {
    console.log('Usage: node get-characters-names.js <film_id>');
    return;
}

const filmId = process.argv[2];
const charactersNames = await getCharactersNames(filmId);
console.log(charactersNames.join(', '));
