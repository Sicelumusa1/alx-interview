#!/usr/bin/node

const request = require('request');
const process = require('process');

function getCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/films/${movieId}`;
  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error fetching data: ${error.message}`);
      process.exit(1);
    }
    try {
      const filmData = JSON.parse(body);
      const characters = filmData.characters || [];
      fetchCharacter(characters);
    } catch (parseError) {
      console.error(`Error fetching data: ${parseError.message}`);
      process.exit(1);
    }
  });
}

function fetchCharacter (characterUrls) {
  if (characterUrls.length === 0) {
    console.log('No characters found for this movie');
    return;
  }

  let count = 0;

  characterUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(`Error fetching character data: ${error.message}`);
        process.exit(1);
      }
      try {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        count++;
        if (count === characterUrls.length) {
          process.exit(0);
        }
      } catch (parseError) {
        console.error(`Error fetching character data: ${parseError.message}`);
        process.exit(1);
      }
    });
  });
}

if (process.argv.length !== 3) {
  console.error('Usege: node 0_star_wars_characters.js <Movie Id>');
  process.exit(1);
}

const movieId = process.argv[2];
getCharacters(movieId);
