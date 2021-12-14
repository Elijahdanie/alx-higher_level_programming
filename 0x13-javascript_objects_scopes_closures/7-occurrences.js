#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let noOc = 0;
  list.forEach(element => {
    noOc += element === searchElement ? 1 : 0;
  });
  return noOc;
};
