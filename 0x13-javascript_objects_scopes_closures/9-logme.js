#!/usr/bin/node

let count = 0;
exports.logMe = function (item) {
  return (console.log(`${count++}: ${item}`));
};
