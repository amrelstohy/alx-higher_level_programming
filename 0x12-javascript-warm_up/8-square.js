#!/usr/bin/node

const size = process.argv[2];

console.log = function () {
  process.stdout.write(Array.prototype.join.call(arguments, '') + '');
};

if (isNaN(size)) {
  console.log('Missing size\n');
} else {
  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      console.log('x');
    }
    console.log('\n');
  }
  console.log('\n');
}
