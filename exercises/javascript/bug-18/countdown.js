function countdown(n) {
  const result = [];
  for (let i = n; i > 1; i--) {
    result.push(i);
  }
  return result;
}

module.exports = { countdown };
