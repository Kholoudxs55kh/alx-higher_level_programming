#!/usr/bin/node

const { dict } = require('./101-data'), Arr = Object.entries(dict), Obj = {};
Arr.forEach(element => {
  if (Obj[element[1]]) {
    Obj[element[1]].push(element[0]);
  } else {
    Obj[element[1]] = [element[0]];
  }
});

console.log(Obj);
