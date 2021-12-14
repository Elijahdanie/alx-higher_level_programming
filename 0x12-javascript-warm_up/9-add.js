#!/usr/bin/node

function add (a, b) {
  console.log(`${(a + b)}`);
}

const firstVal = parseInt(process.argv[2]);
const secondVal = parseInt(process.argv[3]);

add(firstVal, secondVal);
