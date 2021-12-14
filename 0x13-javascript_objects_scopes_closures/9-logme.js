#!/usr/bin/node

exports.logMe = (function (item) {
  let formerNum = 0;
  return (item) => {
    formerNum++;
    console.log(`${formerNum} : ${item}`);
  };
})();
