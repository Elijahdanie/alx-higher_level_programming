#!/usr/bin/node
// This displays the status code of a
// request

const req = require('request');

const url = process.argv[1];

req.get(url, (err, res, body) => {
  if (err) { console.log(err); } else { console.log(`code: ${res.statusCode}`); }
});
