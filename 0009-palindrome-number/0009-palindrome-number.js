/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    // use toString method
    // use reverse method
    // check if both are equal...return true or false
    if (x.toString() === x.toString().split("").reverse().join("") ) {
        return true
    } else {
        return false
    }
};