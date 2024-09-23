#!/usr/bin/node
const request = require('request');

/**
 * Function to make a GET request and return a promise that
 * resolves with the parsed JSON response.
 * @param   {String} url - The URL to make the request to.
 * @returns {Promise}    - A promise that resolves with the parsed JSON data.
 */
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

/**
 * Main function to print all character names from a given Star Wars movie.
 * The movie ID is passed as a command-line argument.
 */
async function main() {
  const args = process.argv;

  if (args.length < 3) {
    console.error('Usage: ./0-starwars_characters.js <movie_id>');
    return;
  }

  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

  try {
    // Fetch movie data
    const movie = await makeRequest(movieUrl);

    if (!movie.characters) {
      console.error('No characters found for this movie.');
      return;
    }

    // Fetch and print each character's name
    for (const characterUrl of movie.characters) {
      const character = await makeRequest(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error.message);
  }
}

main();

