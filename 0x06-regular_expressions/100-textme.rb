#!/usr/bin/env ruby
from = ARGV[0].scan(/\[from:(.*?)\]/)[0]
to = ARGV[0].scan(/\[to:(.*?)\]/)[0]
flags = ARGV[0].scan(/\[flags:(.*?)\]/)[0]
c = ","
puts from[0] + c + to[0] + c + flags[0]
