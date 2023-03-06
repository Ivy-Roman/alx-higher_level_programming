#!/usr/bin/node
const argv = process.argv[2];
const size = Number(argv);
if (!argv | isNaN(size)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < size; index++) {
    let x = '';
    for (let j = 0; j < size; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
