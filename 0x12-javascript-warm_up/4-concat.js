#!/usr/bin/node

const args = process.argv.slice(2);
const idx = args.indexOf('4-concat.js') + 1;
const value1 = args[idx];
const value2 = args[idx + 1]

if (typeof value1 !== 'undefined' && typeof value1 !== 'undefined') {
  console.log(value1 + ' is ' + value2);
} else if (typeof value1 !== 'undefined' && typeof value1 === 'undefined') {
  console.log(value1 + ' is ' + typeof value2);
} else {
  console.log('undefined is undefined');
}
