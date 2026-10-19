function clamp(value, min, max) {
  if (value < min) {
    return max;
  }
  if (value > max) {
    return max;
  }
  return value;
}

module.exports = { clamp };
