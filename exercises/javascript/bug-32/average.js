function average(numbers) {
  let total = 0;
  for (const n of numbers) {
    total += n;
  return total / numbers.length;
}

module.exports = { average };
