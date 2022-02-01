#!/usr/bin/node

// prints the number of movies where the
// character “Wedge Antilles” is present

const request = require('request');

const apiUrl = 'https://swapi-api.hbtn.io/api/';

const characterUrl = `${apiUrl}people/18/`;

const parseurl = `${process.argv[2]}`;

request.get(parseurl, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < data.length; i++) {
      for (let j = 0; j < data[i].characters.length; j++) {
        if (data[i].characters[j] === characterUrl) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(err);
  }
});
