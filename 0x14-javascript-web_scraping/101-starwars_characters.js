#!/usr/bin/node

// prints all characters of a Star Wars movie

const request = require('request');

const Id = process.argv[2];

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

const parsedUrl = `${apiUrl}${Id}`;

request.get(parsedUrl, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const index = 0;
    ordercharacters(data.characters, index);
  } else {
    console.log(err);
  }
});

const ordercharacters = (characters, index) => {
  request.get(characters[index], (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      index++;
      if (index < characters.length) { ordercharacters(characters, index); }
    }
  });
};
