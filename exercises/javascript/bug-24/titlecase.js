function titleCase(sentence) {
  const words = sentence.split(" ");
  const result = words.map((word) => {
    return word[0].toUpperCase() + word.slice(1).toLowerCase();
  });
  return result.join("");
}

module.exports = { titleCase };
