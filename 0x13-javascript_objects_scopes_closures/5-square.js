#!/usr/bin/node

/**
 * class that defines a rectangle
 */

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (w) {
    super(w, w);
  }
};
