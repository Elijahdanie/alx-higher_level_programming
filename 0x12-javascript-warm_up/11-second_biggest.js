#!/usr/bin/node

if (process.argv.length <= 3) {
    console.log('1');
} else {
    let arg = process.argv.slice(2);
    console.log(arg.sort(function(a, b){return a - b})[1]);
}
