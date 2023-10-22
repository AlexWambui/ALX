#!/usr/bin/node

// Script that writes to a file

const fs = require('fs');
const filePath = process.argv[2];
const contentToWrite = process.argv[3];
fs.writeFile(filePath, contentToWrite, err => {
  if (err) {
    console.error(err);
  }
});
