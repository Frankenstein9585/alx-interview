#!/usr/bin/node
const request = require('request');
function getTitle (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  request.get(url, async (error, response, body) => {
    if (error) {
      console.error('Error occurred while making GET request:');
      console.error(error);
    } else {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      const characterPromises = characters.map(character => {
        return new Promise((resolve, reject) => {
          request.get(character, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              const characterData = JSON.parse(body);
              resolve(characterData);
            }
          });
        });
      });

      try {
        const charactersData = await Promise.all(characterPromises);

        charactersData.forEach(characterData => {
          console.log(characterData.name);
        });
      } catch (error) {
        console.error('Something Happened');
        console.error(error);
      }
    }
  });
}

const movieId = process.argv[2];
getTitle(movieId);
