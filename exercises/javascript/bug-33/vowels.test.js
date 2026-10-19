const test = require("node:test");
const assert = require("node:assert/strict");
const { countVowels } = require("./vowels");

test("lower case word", () => {
  assert.deepEqual(countVowels("banana"), 3);
});

test("capital vowel counts", () => {
  assert.deepEqual(countVowels("Apple"), 2);
});

test("no vowels", () => {
  assert.deepEqual(countVowels("rhythm"), 0);
});

test("all capitals", () => {
  assert.deepEqual(countVowels("AEIOU"), 5);
});
