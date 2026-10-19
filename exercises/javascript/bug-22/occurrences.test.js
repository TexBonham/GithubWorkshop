const test = require("node:test");
const assert = require("node:assert/strict");
const { countOccurrences } = require("./occurrences");

test("counts two a letters", () => {
  assert.deepEqual(countOccurrences(["a", "b", "a"], "a"), 2);
});

test("counts numbers", () => {
  assert.deepEqual(countOccurrences([1, 1, 1, 2], 1), 3);
});

test("missing target gives 0", () => {
  assert.deepEqual(countOccurrences(["x", "y"], "z"), 0);
});

test("empty array gives 0", () => {
  assert.deepEqual(countOccurrences([], "a"), 0);
});
