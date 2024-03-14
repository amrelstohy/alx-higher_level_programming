#!/usr/bin/node

const a = process.argv[2];

function fac (a) {
  if (a > 1) {
    return (fac(a - 1) * a);
  } else {
    return (1);
  }
}

if (isNaN(a)) {
  console.log('1');
} else {
  console.log(fac(parseInt(a)));
}
