#!/usr/bin/node

const args = process.argv.slice(2);
const idx = args.indexOf('7-multi_c.js') + 1;
const value = args[idx];
let i;

if ((typeof value === 'undefined') || isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < Number(value); i++) {
    console.log('C is fun');
  }
}
