#!/usr/bin/node

const args = process.argv.slice(2);
const idx = args.indexOf('8-square.js') + 1;
const value = args[idx];
let i;

if ((typeof value === 'undefined') || isNaN(value)) {
  console.log('Missing size');
} else {
  for (i = 0; i < Number(value) && Number(value) > 0; i++) {
    console.log('X'.repeat(value));
  }
}
