#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint(c = 'X') {
    if (c === 'C') {
      for (let i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    }
  }
};
