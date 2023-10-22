#!/usr/bin/node

const [_, __, arg1] = process.argv;

const x = parseInt(arg1);

if (isNaN(x)) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < x; i++) {
    console.log("C is fun");
  }
}
