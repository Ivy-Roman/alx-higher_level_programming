#!/usr/bin/node
const Rectangle = require('./5-rectangle');

module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.width; col += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
