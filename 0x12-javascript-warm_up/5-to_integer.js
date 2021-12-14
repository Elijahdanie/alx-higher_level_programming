#!/usr/bin/node

const firstArgs = process.argv[2];
if (!isNaN(firstArgs)) {
  console.log(`My number: ${parseInt(firstArgs)}`);
} else {
  console.log('Not a number');
}
