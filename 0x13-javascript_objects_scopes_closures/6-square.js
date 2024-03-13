#!/usr/bin/node

/**
 * class that defines a rectangle
 */

const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  charPrint (c) {
    let ch = 'X';
    if (c) {
      ch = c;
    }
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(ch);
      }
      console.log('');
    }
  }
};
