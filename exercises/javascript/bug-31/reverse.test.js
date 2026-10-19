const test = require("node:test");
const assert = require("node:assert/strict");
const { reverseString } = require("./reverse");

test("reverses abc", () => {
  assert.deepEqual(reverseString("abc"), "cba");
});

test("single letter", () => {
  assert.deepEqual(reverseString("x"), "x");
});

test("empty string", () => {
  assert.deepEqual(reverseString(""), "");
});

test("palindrome stays the same", () => {
  assert.deepEqual(reverseString("level"), "level");
});
