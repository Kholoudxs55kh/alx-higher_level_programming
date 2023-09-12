#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  Array.from(list).forEach(element => {
    if (element === searchElement) {
      counter += 1;
    }
  });
  return counter;
};
