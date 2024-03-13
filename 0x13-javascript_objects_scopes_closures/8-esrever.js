#!/usr/bin/node

exports.esrever = function (list) {
  const liste = [];
  let k = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    liste[k] = list[i];
    k++;
  }
  return (liste);
};
