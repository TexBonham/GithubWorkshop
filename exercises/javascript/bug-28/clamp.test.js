const test = require("node:test");
const assert = require("node:assert/strict");
const { clamp } = require("./clamp");

test("value inside the range", () => {
  assert.deepEqual(clamp(5, 0, 10), 5);
});

test("value too small", () => {
  assert.deepEqual(clamp(-5, 0, 10), 0);
});

test("value too big", () => {
  assert.deepEqual(clamp(50, 0, 10), 10);
});

test("value equal to min", () => {
  assert.deepEqual(clamp(0, 0, 10), 0);
});
