/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    // nested for loop
    // check current and next value
    // if current and next value are equal, return true
    // keep iterating through the array
    // if no dupes, return false
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] === nums [j]) {
                return true
            }
        }
    }
    return false
};