#!/usr/bin/node

const args = process.argv.slice(2);
const idx = args.indexOf('9-add.js') + 1;
const a = args[idx];
const b = args[idx + 1];

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return console.log('NaN');
  } else {
    return console.log(Number(a) + Number(b));
  }
}
add(a, b);
