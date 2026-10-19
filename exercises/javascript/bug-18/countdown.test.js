const test = require("node:test");
const assert = require("node:assert/strict");
const { countdown } = require("./countdown");

test("counts down from 3", () => {
  assert.deepEqual(countdown(3), [3, 2, 1]);
});

test("countdown from 1 is just [1]", () => {
  assert.deepEqual(countdown(1), [1]);
});

test("countdown from 0 is empty", () => {
  assert.deepEqual(countdown(0), []);
});
