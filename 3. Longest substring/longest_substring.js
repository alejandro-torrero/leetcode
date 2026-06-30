function lengthOfLongestSubstring(s) {
  substring = "";
  maxLen = 0;
  for (i = 0; i < s.length; i++) {
    isPresent = substring.indexOf(s[i]);

    if (isPresent < 0) {
      // Char is not present on the string
      console.log(`${s[i]} is not present in ${substring} adding`);
      substring += s[i];
      if (maxLen < substring.length) maxLen = substring.length;
    } else {
      console.log(`${s[i]} is present in ${substring} at ${isPresent}`);
      if (maxLen < substring.length) maxLen = substring.length;

      // Validate if we should keep evaluating
      temp = substring.substring(isPresent + 1, substring.length);
      if (temp.length + (s.length - i - 1) < maxLen) break;
      substring = substring.substring(isPresent + 1, substring.length) + s[i];
    }

    console.log("We have ", substring);
    console.log("Max", maxLen);
  }
  console.log(substring);
  return substring.length;
}

function main() {
  const start = new Date();
  maxLen = lengthOfLongestSubstring("abcabcbb");
  console.log(maxLen);
  maxLen = lengthOfLongestSubstring("bbbbb");
  console.log(maxLen);
  maxLen = lengthOfLongestSubstring("pwwkew");
  console.log(maxLen);
  maxLen = lengthOfLongestSubstring("hkcpmprxxxqw");
  console.log(maxLen);

  console.log("Finish in ", new Date() - start);
}

main();
