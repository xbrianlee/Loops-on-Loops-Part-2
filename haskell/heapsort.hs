-- Heap Sort in Haskell
-- Note: Use ":set +s" to see computation time and memory usage.

module Main where

import Data.Graph.Inductive.Internal.Heap(
  Heap(..),insert,findMin,deleteMin)

import System.IO

main = do
  theInput <- readFile "input.txt"
  putStrLn (heapsort theInput)    
 
build :: Ord a => [(a,b)] -> Heap a b
build = foldr insert Empty
 
toList :: Ord a => Heap a b -> [(a,b)]
toList Empty = []
toList h = x:toList r
           where (x,r) = (findMin h,deleteMin h)
 
heapsort :: Ord a => [a] -> [a]
heapsort = (map fst) . toList . build . map (\x->(x,x))