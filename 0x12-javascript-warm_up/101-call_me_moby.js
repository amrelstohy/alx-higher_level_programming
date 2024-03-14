#!/usr/bin/node

let i = 0;

exports.callMeMoby = function (x, theFunction) {
  while (i < x) {
    theFunction();
    i++;
  }
};
