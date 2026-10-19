const test = require("node:test");
const assert = require("node:assert/strict");
const { initials } = require("./initials");

test("capitalized name", () => {
  assert.equal(initials("Ada Lovelace"), "AL");
});

test("lowercase name is capitalized", () => {
  assert.equal(initials("grace hopper"), "GH");
});

test("three words", () => {
  assert.equal(initials("katherine coleman johnson"), "KCJ");
});

test("single word", () => {
  assert.equal(initials("linus"), "L");
});
