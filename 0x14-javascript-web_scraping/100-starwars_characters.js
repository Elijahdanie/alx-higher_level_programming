#!/usr/bin/node

// prints all characters of a Star Wars movie

const request = require('request');

const Id = process.argv[2];

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

const parsedUrl = `${apiUrl}${Id}`;

request.get(parsedUrl, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body);
    for (let i = 0; i < data.characters.length; i++) {
      request.get(data.characters[i], (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  } else {
    console.log(err);
  }
});
