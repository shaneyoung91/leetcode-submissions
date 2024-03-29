/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    // create variable to hold prefix
    // iterate over strings
    // nested loop to compare characters for current and next word in strs array
    
    let prefix = ""
    
    // base-case
    if (strs.length === 0) {
        return prefix
    }
    
    for (let i = 0; i < strs[0].length; i++) {
        const char = strs[0][i]
        for (let j = 1; j < strs.length; j++) {
            if (strs[j][i] !== char) {
                return prefix
            }
        }
            prefix += char
        }
    return prefix
}