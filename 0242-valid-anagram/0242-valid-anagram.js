/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    // check that s.length and t.length are equal (base-case)
    // create hash tables with key-value pairs for 's' and 't'
    // iterate through s and t to tally each characters
    // iterate through hash table and compare # of characters
    // if not equal - return false, else return true
    
    if (s.length !== t.length) {
        return false
    }
    
    const sTable = {}
    const tTable = {}
    
    for (let char of s) {
        sTable[char] = (sTable[char] || 0) + 1
    }
    
    for (let char of t) {
        tTable[char] = (tTable[char] || 0) + 1
    }
    
    for (let char in sTable) {
        if (sTable[char] !== tTable[char]) {
            return false;
        }
    }
    
    return true;
};