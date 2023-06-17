/**
 * @param {string} val1
 * @return {Object}
 */
var expect = function(val1) {
    return {
        toBe: function(val2) {  
            if (val1 !== val2) {
                throw new Error("Not Equal")
            }
            return true
        },
        notToBe: function(val2) {
            if (val1 === val2) {
                throw new Error("Equal")
            }
            return true
        },
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */