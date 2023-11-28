#!/usr/bin/env ruby
puts ARGV[0].scan(/from:[A-Za-z]+|from:\+[0-9]{11}/).join + "," + ARGV[0].scan(/to:[A-Za-z]+|to:\+[0-9]{11}/).join + "," + ARGV[0].scan(/flags:............/).join
