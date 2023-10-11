/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    // since array is sorted, we can cut search in half by comparing target and middle value in the array
    // if target is > middle value, then search right half and move start index
    // if target is < middle value, then search left half and move end index
    // if target = middle value, return index position of middle value (base-case)

    let start = 0
    let end = nums.length - 1
    
    while (start <= end) {
        let middle = Math.floor((start + end) / 2)
        if (nums[middle] === target) {
            return middle
        }
        if (target < nums[middle]) {
            end = middle - 1
        } else {
            start = middle + 1
        }
    }
    return -1
};