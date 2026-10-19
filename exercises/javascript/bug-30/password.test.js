const test = require("node:test");
const assert = require("node:assert/strict");
const { isLongEnough } = require("./password");

test("long password is fine", () => {
  assert.deepEqual(isLongEnough("correcthorse"), true);
});

test("exactly 8 is fine", () => {
  assert.deepEqual(isLongEnough("abcdefgh"), true);
});

test("7 characters is too short", () => {
  assert.deepEqual(isLongEnough("abcdefg"), false);
});

test("empty is too short", () => {
  assert.deepEqual(isLongEnough(""), false);
});
