-- Insertion Sort in Haskell

insertion_sort :: (a -> a -> Bool) -> [a] -> [a]
insertion_sort pred []     = []
insertion_sort pred (x:xs) = insert pred x (insertion_sort pred xs)
insert :: (a -> a -> Bool) -> a -> [a] -> [a]
insert pred x [] = [x]
insert pred x (y:ys)
  | pred x y = (x:y:ys)
  | otherwise = y:(insert pred x ys)