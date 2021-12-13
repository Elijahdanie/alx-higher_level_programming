#!/usr/bin/node

function add(a, b) {
    console.log(`${(a + b)}`);
}

let first_val = parseInt(process.argv[2]);
let second_val = parseInt(process.argv[3]);

add(first_val, second_val);
