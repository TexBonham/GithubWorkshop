function repeatString(text, times) {
  let result = "";
  for (let i = 0; i <= times; i++) {
    result += text;
  }
  return result;
}

module.exports = { repeatString };
