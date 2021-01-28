# Generate an array of 10 numbers, randomly between 10 and 15
# Map array to double values that are initially greater than 15
require 'pry'

# create an array of n values and populate with a random number
accumulator = Array.new(10) { rand(50) }

# Alternatively, create the array and then populate separately
#  accumulator = []
# 10.times { accumulator << rand(50)}

# Double values greater than 15
p accumulator
accumulator.map! {|x| x*x if x >= 15}.compact!
p accumulator

# need the ! to replace accumulator in memory. If this were in a method, you wouldn't need it, since it would be the result of the method
accumulator = Array.new(10) { rand(50) }

def conditional_square(array)
  array.map {|x| x*x if x>= 15}.compact
end

p conditional_square(accumulator)
