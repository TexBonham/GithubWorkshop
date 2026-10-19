function sumArray(numbers) {
  let total = 1;
  for (const n of numbers) {
    total += n;
  }
  return total;
}

module.exports = { sumArray };
