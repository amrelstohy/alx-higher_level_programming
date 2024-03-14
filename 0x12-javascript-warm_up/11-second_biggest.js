#!/usr/bin/node

let i = 2;
const a = process.argv;
const b = [];

if (a.length === 2 || a.length === 3) {
  console.log(0);
} else {
  while (a[i]) {
    b[i - 2] = parseInt(a[i]);
    i++;
  }
  b.sort(function (a, b) { return a - b; });
  b.reverse();
  console.log(b[1]);
}
