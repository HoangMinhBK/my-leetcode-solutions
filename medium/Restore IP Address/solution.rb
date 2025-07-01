# @param {String} s
# @return {String[]}
def restore_ip_addresses(s)
  @valid_ips = []
  @s = s

  def dfs(slice_start, slice_end, current)
      return if slice_start >= @s.length || slice_end >= @s.length

      ip_part = @s[slice_start..slice_end]
      return if ip_part.length > 1 && ip_part[0] == '0' # Don't include part like '023', '011'
      return if ip_part.to_i > 255
      
      current << ip_part
      if current.length == 4 # Time to evaluate the current IP address
          if slice_end == @s.length - 1
              @valid_ips << current.join(".")
          end
          current.pop
          return
      end

      dfs(slice_end+1, slice_end+1, current)
      dfs(slice_end+1, slice_end+2, current)
      dfs(slice_end+1, slice_end+3, current)
      current.pop
  end

  dfs(0, 0, [])
  dfs(0, 1, [])
  dfs(0, 2, [])
  @valid_ips
end