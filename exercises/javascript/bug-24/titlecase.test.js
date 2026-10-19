const test = require("node:test");
const assert = require("node:assert/strict");
const { titleCase } = require("./titlecase");

test("three words", () => {
  assert.deepEqual(titleCase("hello big world"), "Hello Big World");
});

test("single word", () => {
  assert.deepEqual(titleCase("hello"), "Hello");
});

test("shouting is lowered", () => {
  assert.deepEqual(titleCase("HELLO THERE"), "Hello There");
});

test("already title case", () => {
  assert.deepEqual(titleCase("Good Day"), "Good Day");
});
