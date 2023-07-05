#!/usr/bin/env ruby

# matches a Repetition Token

puts ARGV[0].scan(/hbt?{1,}n/).join
