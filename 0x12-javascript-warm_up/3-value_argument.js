#!/usr/bin/node

const args = process.argv.slice(2);
const idx = args.indexOf('3-value_argument.js') + 1;
const value = args[idx];

if (typeof value !== 'undefined') {
  console.log(value);
} else {
  console.log('No argument');
}
