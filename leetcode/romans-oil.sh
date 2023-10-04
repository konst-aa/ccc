read num
# https://leetcode.com/problems/integer-to-roman/

const pairs = [ 
    ["M", 1000],
    ["D", 500],
    ["C", 100],
    ["L", 50],
    ["X", 10],
    ["V", 5],
    ["I", 1]
]
var i = 0
var out = ""
while ( num > 0 ) {
    var c, v = pairs[i]
    if ( num - v >= 0 ) {
        setvar num = num - v
        setvar out = "$out$c"
    } else {
        setvar i += 1
    }
}

echo $out
