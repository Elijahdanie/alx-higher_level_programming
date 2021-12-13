#!/usr/bin/node

if (process.argv.length <= 3) {
    console.log('0');
} else {
    let arg = process.argv.slice(2);
    console.log(arg.sort(function (a, b) { return b - a })[1]);
}
