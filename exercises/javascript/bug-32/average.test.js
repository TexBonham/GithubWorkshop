const test = require("node:test");
const assert = require("node:assert/strict");
const { average } = require("./average");

test("average of 2, 4, 6", () => {
  assert.deepEqual(average([2, 4, 6]), 4);
});

test("single number", () => {
  assert.deepEqual(average([7]), 7);
});

test("fractional result", () => {
  assert.deepEqual(average([1, 2]), 1.5);
});

test("negatives", () => {
  assert.deepEqual(average([-2, 2]), 0);
});
