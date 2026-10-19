function evenNumbers(numbers) {
  const result = [];
  for (const n of numbers) {
    if (n % 2 === 1) {
      result.push(n);
    }
  }
  return result;
}

module.exports = { evenNumbers };
