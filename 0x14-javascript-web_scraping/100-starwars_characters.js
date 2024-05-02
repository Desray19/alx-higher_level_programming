#!/usr/bin/node

const request = require('request');
const util = require('util');
const get = util.promisify(request.get);

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

async function fetchFilmAndCharacters (id) {
  try {
    const filmResponse = await get(url + id);
    const filmData = JSON.parse(filmResponse.body);
    const characterUrls = filmData.characters;

    const characterPromises = characterUrls.map(async (characterUrl) => {
      const characterResponse = await get(characterUrl);
      const characterData = JSON.parse(characterResponse.body);
      return characterData.name;
    });

    const characterNames = await Promise.all(characterPromises);
    console.log(characterNames.join('\n'));
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

fetchFilmAndCharacters(id);
