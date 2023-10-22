#!/usr/bin/node

const [_, __, arg1] = process.argv;

const n = parseInt(arg1);

if (isNaN(n)) {
  console.log("Missing size");
} else {
  for (let i = 0; i < n; i++) {
    let row = "";
    for (let j = 0; j < n; j++) {
      row += "X";
    }
    console.log(row);
  }
}
