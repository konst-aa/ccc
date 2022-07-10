-- Translation of my python stub

inp :: IO Int
inp = readLn

inl :: IO [Int]
inl = do
    input <- getLine
    let nums = words input
    return $ map read nums

insr :: IO String
insr = do
    input <- getLine
    return input

-- solving: https://codeforces.com/contest/1698/problem/B
main :: IO()
main = do
    num_tests <- inp
    [test | _ <- [1..num_tests]]

-- half-digested code that ill finish later

test :: IO()
test = do
    input <- inlt
    sizes <- inlt
    let 
        num_piles = first input
        operations = last input
    in
        if operations == 0
            then print ((num_piles - 1) `div` 2)
        else

