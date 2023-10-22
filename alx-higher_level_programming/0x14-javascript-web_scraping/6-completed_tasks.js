#!/usr/bin/node

// Counts the completed tasks using data from an api call

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  const tasks = JSON.parse(body);
  const dictionary = {};
  for (let i = 0; i < tasks.length; i++) {
    if (!dictionary[tasks[i].userId]) {
      dictionary[tasks[i].userId] = 0;
    }
    if (tasks[i].completed === true) {
      dictionary[tasks[i].userId] += 1;
    }
  }
  console.log(dictionary);
});
