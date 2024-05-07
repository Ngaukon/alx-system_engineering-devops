#!/usr/bin/env ruby
# This scripts accepts one argument and passes it to a regular expression,

puts ARGV[0].scan(/hbt{2,5}n/).join
