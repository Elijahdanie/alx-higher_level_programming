#!/usr/bin/node

let first_args = process.argv[2]
if (!isNaN(first_args)) {
    console.log(`My number: ${parseInt(first_args)}`);
} else {
    console.log('Not a number');
}
