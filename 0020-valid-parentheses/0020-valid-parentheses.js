/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // create stack of empty str
    // create object with key-value pairs for brackets
    // if s contains the opening bracket, add to stack
    // remove from stack if corresponding closing bracket matches
    // else return false
    // return empty stack if true
    
    let stack = ""
    const brackets = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
       
    for (let char of s) {
        if (char in brackets) {
            stack += brackets[char]
        } else {
            if (stack.slice(-1) === char) {
                stack = stack.slice(0, -1)
            } else {
                return false
            }
        }
    }
    return stack === ""
};