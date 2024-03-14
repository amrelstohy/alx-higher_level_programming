#!/usr/bin/node

const a = process.argv;

if (a.length === 2 || a.length === 3) {
  console.log(0);
} else {
  a.sort();
  a.reverse();
  console.log(a[1]);
}
