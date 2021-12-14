#!/usr/bin/node
const Basesquare = require('./5-square');

class Square extends Basesquare {
  charPrint (c) {
    const charP = c || 'X';
    let draw = '';
    for (let i = 0; i < this.height; i++) {
      draw = '';
      for (let j = 0; j < this.width; j++) {
        draw += charP;
      }
      console.log(draw);
    }
  }
}
module.exports = Square;
