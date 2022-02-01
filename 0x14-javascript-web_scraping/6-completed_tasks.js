#!/usr/bin/node

// this computes the number of teask
// completed by user id

const request = require('request');

const apiUrl = process.argv[2];

const finalObj = {};

request.get(apiUrl, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    body = JSON.parse(body);
    for (let j = 0; j < body.length; j++) {
      const todo = body[j];
      if (todo.completed) {
        if (finalObj[todo.userId] === undefined) {
          finalObj[todo.userId] = 1;
        } else {
          finalObj[todo.userId] += 1;
        }
      }
    }
    console.log(finalObj);
  } else {
    console.log(err);
  }
});
