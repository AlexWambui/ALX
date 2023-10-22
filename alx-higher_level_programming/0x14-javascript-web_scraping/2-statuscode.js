#!/usr/bin/node

// Prints the status code of a GET request

const request = require('request');
const url = process.argv[2];
request(url, (err, result, body) => {
  if (err) console.error(err);
  console.log('code:', result.statusCode);
});
