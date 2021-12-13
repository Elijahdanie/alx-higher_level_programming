#!/usr/bin/node

let len = 0;
process.argv.forEach (element => {
    len++;
});
if (len == 2) {
    console.log('No argument');
}
else if (len === 3)
{
    console.log(process.argv[2]);
}
