const test = require("node:test");
const assert = require("node:assert/strict");
const { repeatString } = require("./repeat");

test("repeats ab three times", () => {
  assert.deepEqual(repeatString("ab", 3), "ababab");
});

test("repeat once", () => {
  assert.deepEqual(repeatString("x", 1), "x");
});

test("zero times is empty", () => {
  assert.deepEqual(repeatString("hi", 0), "");
});

test("repeats a space twice", () => {
  assert.deepEqual(repeatString(" ", 2), "  ");
});
