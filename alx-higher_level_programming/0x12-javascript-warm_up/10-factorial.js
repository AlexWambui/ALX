#!/usr/bin/node

function factorial(n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const [_, __, arg1] = process.argv;
const num = parseInt(arg1);

console.log(factorial(num));
