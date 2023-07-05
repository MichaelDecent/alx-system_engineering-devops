#!/usr/bin/env ruby

# matches a Repetition Token

puts ARGV[0].scan(/hbt{2,5}n/).join
