# @param {String} s
# @param {String} t
# @return {String}
def min_window(s, t)
    return "" if s.length < t.length
    freq = Hash.new(0)
    t.each_char { |char| freq[char] += 1 }
    required = freq.size
    formed = 0

    left = 0
    right = 0
    
    window_counts = Hash.new(0)

    res = s #initial val for res

    valid_once = false
    while right < s.length
        char = s[right]
        window_counts[char] += 1
        if freq.key?(char) && window_counts[char] == freq[char]
        formed += 1
        end

        while formed == required # a window is valid
            # shrink left side of the window

            valid_once = true
            if res.length > right - left + 1
                res = s[left..right]
            end

            left_char = s[left]
            window_counts[left_char] -= 1
            # if the slided value is in "t", mark the current window is not valid
            if freq.key?(left_char) && window_counts[left_char] < freq[left_char]
                formed -= 1
            end
            left += 1
        end
        right += 1
    end
    return "" unless valid_once
    res
end