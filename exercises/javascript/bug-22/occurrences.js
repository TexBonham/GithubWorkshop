function countOccurrences(items, target) {
  let count = 0;
  for (const item of items) {
    if (item !== target) {
      count++;
    }
  }
  return count;
}

module.exports = { countOccurrences };
