#!/usr/bin/node

const args = process.argv;
const arr = args.slice(('11-second_biggest.js') + 1);
arr.map(Number).sort();

if (args.slice(2).length <= 1) {
  console.log('0');
} else {
  console.log(Number(arr[arr.length - 2]));
}
