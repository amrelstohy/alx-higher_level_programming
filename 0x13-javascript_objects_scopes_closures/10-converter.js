#!/usr/bin/node

exports.converter = function (base) {
  function f (nb) {
    return (nb.toString(base));
  }
  return (f);
};
