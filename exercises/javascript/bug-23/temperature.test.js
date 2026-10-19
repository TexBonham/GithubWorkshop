const test = require("node:test");
const assert = require("node:assert/strict");
const { celsiusToFahrenheit } = require("./temperature");

test("water boils at 212", () => {
  assert.deepEqual(celsiusToFahrenheit(100), 212);
});

test("water freezes at 32", () => {
  assert.deepEqual(celsiusToFahrenheit(0), 32);
});

test("minus 40 is the same in both", () => {
  assert.deepEqual(celsiusToFahrenheit(-40), -40);
});

test("body temperature", () => {
  assert.deepEqual(celsiusToFahrenheit(37), 98.6);
});
