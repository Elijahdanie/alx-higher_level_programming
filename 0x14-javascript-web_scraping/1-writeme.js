#!/usr/bin/node
// writes content to a file
const fs = require('fs');

fs.writeFile(process.argv[1], process.argv[2], 'utf-8', (err) => {
  if (err) { console.log(err); }
});
