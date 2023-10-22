#!/usr/bin/node

// Prints a star wars movie title

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, result, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body);
  console.log(data.title);
});
