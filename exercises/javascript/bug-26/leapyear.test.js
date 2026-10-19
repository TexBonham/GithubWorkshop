const test = require("node:test");
const assert = require("node:assert/strict");
const { isLeapYear } = require("./leapyear");

test("2024 is a leap year", () => {
  assert.deepEqual(isLeapYear(2024), true);
});

test("2023 is not", () => {
  assert.deepEqual(isLeapYear(2023), false);
});

test("1900 is not", () => {
  assert.deepEqual(isLeapYear(1900), false);
});

test("2000 is", () => {
  assert.deepEqual(isLeapYear(2000), true);
});
