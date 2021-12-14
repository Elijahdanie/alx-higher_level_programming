#!/usr/bin/node

exports.converter = function (base) {
  return (digit) => {
    return digit.toString(base);
  };
};
