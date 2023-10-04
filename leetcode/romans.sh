read num
# https://leetcode.com/problems/integer-to-roman/roman

pairs=(
    "M 1000"
    "D 500"
    "C 100"
    "L 50"
    "X 10"
    "V 5"
    "I 1"
)

i=0
out=""
while [ $num -gt 0 ]; do
    set ${pairs[i]}
    if [ $[num - $2] -ge 0 ]; then
        num=$[num - $2]
        out="$out$1"
    else
        i=$[i + 1]
    fi
done

echo $out
