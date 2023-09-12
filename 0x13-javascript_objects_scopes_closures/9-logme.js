#!/usr/bin/node

exports.logMe = function (item) {
  const arr = [];
  arr.push(item);
  const count = arr.length;
  return (console.log(`${count}: ${item}`));
};
