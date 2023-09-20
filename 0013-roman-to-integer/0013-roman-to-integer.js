/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const symbol = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }
    
    let num = 0
    
    for (let i = 0; i < s.length; i++) {
        const current = symbol[s[i]]
        const next = symbol[s[i+1]]
        if (current < next) {
            num -= current
        } else {
            num += current
        }
    }
    return num
};