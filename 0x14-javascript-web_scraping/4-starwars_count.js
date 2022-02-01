#!/usr/bin/node

const request = require('request');

const api_Url = 'https://swapi-api.hbtn.io/api/';

const characterUrl = `${api_Url}people/18/`;

const parseurl = `${process.argv[2]}`;

request.get(parseurl, (err, res, body) => {
  if (!err && res.statusCode == 200) {
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
  } else if (err) {
    console.log(err);
  }
});
