const test = require("node:test");
const assert = require("node:assert/strict");
const { cartTotal } = require("./cart");

test("one item with quantity 3", () => {
  assert.deepEqual(cartTotal([{ price: 2, quantity: 3 }]), 6);
});

test("two items", () => {
  assert.deepEqual(cartTotal([{ price: 5, quantity: 1 }, { price: 1, quantity: 4 }]), 9);
});

test("empty cart is 0", () => {
  assert.deepEqual(cartTotal([]), 0);
});

test("quantity 0 costs nothing", () => {
  assert.deepEqual(cartTotal([{ price: 9, quantity: 0 }]), 0);
});
