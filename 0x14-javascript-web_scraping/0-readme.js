#!/usr/bin/node
// this reads the conent of a file
const fs = require('fs');

const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8', (err, data) => {
  if (!err) { console.log(data); } else { console.log(err); }
});
