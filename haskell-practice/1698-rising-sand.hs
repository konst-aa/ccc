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

-- solving:
main :: IO()
main = do
    
