#!/usr/bin/node

let x = process.argv[2];
if (!isNaN(x)) {
    x = parseInt(x);
    if (x != undefined) {
        for (let i = 0; i < x; i++) {
            console.log('C is fun');
        }
    }
}
else {
    console.log('Missing number of occurrences');
}
