const test = require("node:test");
const assert = require("node:assert/strict");
const { lastItem } = require("./last");

test("last of three numbers", () => {
  assert.deepEqual(lastItem([1, 2, 3]), 3);
});

test("last of strings", () => {
  assert.deepEqual(lastItem(["a", "b"]), "b");
});

test("single element", () => {
  assert.deepEqual(lastItem([9]), 9);
});

test("empty array gives undefined", () => {
  assert.deepEqual(lastItem([]), undefined);
});
