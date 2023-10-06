/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // use RegEx on argument 's' to remove all non-alphanumeric characters
    // check start and end of string for matching characters
    // if no match, return false
    // keep iterating through string and return true if all matches
      
    const newStr = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();

    let start = 0
    let end = newStr.length - 1

    while (start < end) {
        if (newStr[start] !== newStr[end]) {
            return false
        }
        start++
        end--
    }
   return true
};