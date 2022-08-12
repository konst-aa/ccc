-- Translation of my python stub, also broken
{- import Data.List ( tails )
import Data.Foldable (for_)

inp :: IO Int
inp = readLn

inl :: IO [Int]
inl = do
    input <- getLine
    let nums = words input
    return $ map read nums

insr :: IO String
insr = do
    getLine

chunk :: [a] -> Int -> [b]
chunk l n = do
    [take n item | item <- tails $ l, length item <= n]
    
-- solving: https://codeforces.com/contest/1698/problem/B
main :: IO()
main = do
    num_tests <- inp
    for_ [1..num_tests] (\_ -> do
        input <- inl
        sizes <- inl
        let num_piles = head input
        let operations = input!!1

        if operations == 0 then 
            print (div (num_piles - 1) 2)
        else do
            a <- chunk 3 sizes
            b <- flip map a (\l -> do
                if l!!1 > l!!0 + l!!2 then 1
                else 0) 
            c <- sum b
            print c)-}