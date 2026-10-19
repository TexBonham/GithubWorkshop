function countVowels(text) {
  let count = 0;
  for (const ch of text) {
    if ("aeiou".includes(ch)) {
      count++;
    }
  }
  return count;
}

module.exports = { countVowels };
