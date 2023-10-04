import qualified Data.Map.Strict as Map

folder :: (Map.Map Char Int, Int, Int, Int) -> Char -> (Map.Map Char Int, Int, Int, Int)
folder (positions, past, best, index) char = do
    let newPast = max (Map.findWithDefault 0 char positions) past
    let newBest = max (index + 1 - newPast) best
    (Map.insert char (index + 1) positions, newPast, newBest, index + 1)

-- solving: https://leetcode.com/problems/longest-substring-without-repeating-characters/
main :: IO()
main = do
    let (_, _, best, _) = Prelude.foldl folder (Map.empty, 0, 0, 0) "aab"
    print best