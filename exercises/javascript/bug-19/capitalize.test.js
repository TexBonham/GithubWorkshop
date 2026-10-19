const test = require("node:test");
const assert = require("node:assert/strict");
const { capitalize } = require("./capitalize");

test("capitalizes hello", () => {
  assert.deepEqual(capitalize("hello"), "Hello");
});

test("single letter", () => {
  assert.deepEqual(capitalize("a"), "A");
});

test("already capitalized stays the same", () => {
  assert.deepEqual(capitalize("World"), "World");
});

test("empty string stays empty", () => {
  assert.deepEqual(capitalize(""), "");
});
