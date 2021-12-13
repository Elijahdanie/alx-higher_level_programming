#!/usr/bin/node

let x = process.argv[2];
let line = '';
if (!isNaN(x)) {
    x = parseInt(x);
    if (x != undefined) {
        for (let i = 0; i < x; i++) {
            line = '';
            for (let j = 0; j < x; j++) {
                line += 'X'
            }
            console.log(`${line}`);
        }
    }
} else {
    console.log('Missing size');
}
