-- Translation of my python stub
import Data.List (tails)
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
    input <- getLine
    return input

chunk :: List -> Integer -> [List]
chunk l n =
    filter (\x -> length x == n) [item | item <- tails $ l]

-- solving:
main :: IO()
main = do