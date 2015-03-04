-- Insertion Sort in Haskell
-- Note: Use ":set +s" to see computation time and memory usage.
module Main where

import System.IO
import Data.List (insert)

main = do
  theInput <- readFile "input.txt"
  putStrLn (insertionSort theInput) 

insertionSort :: Ord a => [a] -> [a]
insertionSort = foldr insert []