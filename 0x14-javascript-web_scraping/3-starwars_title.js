#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

const parseurl = `${apiUrl}${movieId}`;

request.get(parseurl, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log(err);
  }
});
