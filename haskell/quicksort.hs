-- Quicksort in Haskell
-- Note: Use ":set +s" to see computation time and memory usage.

module Main where

import System.IO

main = do
  theInput <- readFile "input.txt"
  putStrLn (quicksort theInput)       

quicksort :: Ord a => [a] -> [a]
quicksort []     = []
quicksort (p:xs) = (quicksort lesser) ++ [p] ++ (quicksort greater)
    where
        lesser  = filter (< p) xs
        greater = filter (>= p) xs