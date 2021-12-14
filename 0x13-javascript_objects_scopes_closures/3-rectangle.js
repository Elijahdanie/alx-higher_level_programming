#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let draw = '';
    for (let i = 0; i < this.height; i++) {
      draw = '';
      for (let j = 0; j < this.width; j++) {
        draw += 'X';
      }
      console.log(draw);
    }
  }
}
module.exports = Rectangle;
