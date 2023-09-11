#!/usr/bin/node

const args = process.argv.slice(2);
const idx = args.indexOf('5-to_integer.js') + 1;
const value = args[idx];

if ((typeof value === 'undefined') || isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(value));
}
