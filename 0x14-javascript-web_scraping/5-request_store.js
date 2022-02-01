#!/usr/bin/node

// This module gets the content of a
// webpage and stores it in a file

const fs = require('fs');
const request = require('request');

const url = process.argv[1];
const filepath = process.argv[2];

request.get(url, (err, res, body) => {
  if (!err && res.statusCode == 200) {
    fs.writeFile(filepath, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(err);
  }
});
