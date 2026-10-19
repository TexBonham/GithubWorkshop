function initials(name) {
  let result = "";
  for (const word of name.split(" ")) {
    result += word[0];
  }
  return result;
}

module.exports = { initials };
