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
insr = do getLine

chunk :: [t] -> Int -> Int -> Bool -> [[t]]
chunk l size step leftover =
    [take size item | item <- tails l,  (not (null item) && leftover) || length item >= size]
    
-- solving:
main :: IO()
main = do print (chunk [1,2,3,4,5] 3 1 True)