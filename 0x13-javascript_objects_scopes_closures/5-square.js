#!/usr/bin/node
const Basesquare = require('./4-rectangle');

class Square extends Basesquare {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
