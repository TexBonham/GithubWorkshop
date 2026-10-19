const test = require("node:test");
const assert = require("node:assert/strict");
const { sumArray } = require("./sum");

test("sums 1, 2, 3", () => {
  assert.deepEqual(sumArray([1, 2, 3]), 6);
});

test("sums a single number", () => {
  assert.deepEqual(sumArray([10]), 10);
});

test("empty array sums to 0", () => {
  assert.deepEqual(sumArray([]), 0);
});

test("handles negatives", () => {
  assert.deepEqual(sumArray([5, -2]), 3);
});
