# solving: https://leetcode.com/problems/longest-substring-without-repeating-characters/
defmodule Solution do
  @spec length_of_longest_substring(s :: String.t()) :: integer
  def length_of_longest_substring(s) do
    input_chars = String.to_charlist(s)
    {_, _, best, _} = Enum.reduce(input_chars, {%{}, 0, 0, 0}, &reduce_fn/2)
    best
  end

  def reduce_fn(char, {positions, past, best, index}) do
    new_index = index + 1
    val = Map.get(positions, char, 0)
    new_past = max(val, past)
    new_best = max(new_index - new_past, best)
    {Map.put(positions, char, new_index), new_past, new_best, new_index}
  end
end

"aab"
|> Solution.length_of_longest_substring()
|> IO.inspect()
