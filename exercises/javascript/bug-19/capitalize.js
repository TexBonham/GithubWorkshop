function capitalize(word) {
  if (word.length === 0) {
    return word;
  }
  return word[0].toUpperCase() + word.slice(0);
}

module.exports = { capitalize };
