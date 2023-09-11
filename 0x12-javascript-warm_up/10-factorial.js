#!/usr/bin/node

const args = process.argv.slice(2);
const idx = args.indexOf('10-factorial.js') + 1;
const value = args[idx];
let result = 1;

if (isNaN(value)) {
  console.log('1');
} else {
  factorial(value);
}
function factorial (value) {
  if (value !== 1) {
    result *= value;
    return factorial(value - 1);
  } else {
    console.log(result);
  }
}
