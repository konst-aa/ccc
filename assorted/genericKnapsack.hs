import Data.Array((!), listArray)

knapsack :: [Int] -> [Int] -> Int -> Int
knapsack w v cols = maximum $ map (\i -> r ! (i,cols)) [1..rows]
    where
        rows = length w
        w' = listArray (1, rows) w
        v' = listArray (1, rows) v
        r = listArray ((0, 0), (rows, cols)) $ concat $ map (\x -> map (f x) [0..cols]) [0..rows]
        f row 0 = 0
        f 0 col = 0
        f row col 
          | col < currWeight = above
          | otherwise = max above $ v' ! row + r ! (row-1, col - currWeight)
          where 
              above = r ! (row-1, col)
              currWeight = w' ! row


main :: IO ()
main = do
    putStrLn "Weights"
    weights <- getLine
    putStrLn "Values"
    values <- getLine
    putStrLn "Capacity"
    capacity <- getLine
    let w = map read $ words weights :: [Int]
    let v = map read $ words values :: [Int]
    let c = read capacity :: Int
    putStrLn $ show $ knapsack w v c
