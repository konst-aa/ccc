import qualified Data.Set as Set

folder :: (Set.Set Char, Int) -> Char -> (Set.Set Char, Int)
folder (seen, best) char
    | Set.member char seen = (Set.delete char seen, best)
    | Set.size seen + 1 > best = (Set.insert char seen, best + 1)
    | otherwise = (Set.insert char seen, best) 

-- solving: https://leetcode.com/problems/longest-substring-without-repeating-characters/
main :: IO()
main = do 
    let (_, best) = Prelude.foldl folder (Set.empty, 0) "abacde"
    print best