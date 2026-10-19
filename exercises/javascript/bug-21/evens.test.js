const test = require("node:test");
const assert = require("node:assert/strict");
const { evenNumbers } = require("./evens");

test("keeps evens from 1 to 4", () => {
  assert.deepEqual(evenNumbers([1, 2, 3, 4]), [2, 4]);
});

test("all odd gives empty", () => {
  assert.deepEqual(evenNumbers([1, 3, 5]), []);
});

test("zero is even", () => {
  assert.deepEqual(evenNumbers([0, 7]), [0]);
});

test("empty input gives empty", () => {
  assert.deepEqual(evenNumbers([]), []);
});
