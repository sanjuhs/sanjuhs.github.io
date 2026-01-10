-- normalize.lua
-- Minimal path normalization helper used by the love.js web player.
-- Keeps paths stable across platforms (slashes, ./, ../).

local function normalize(path)
  if type(path) ~= 'string' then
    return path
  end

  -- Normalize separators and collapse duplicates
  path = path:gsub('\\', '/')
  path = path:gsub('/+', '/')

  local isAbs = path:sub(1, 1) == '/'
  local out = {}

  for part in path:gmatch('[^/]+') do
    if part == '..' then
      if #out > 0 then
        table.remove(out)
      end
    elseif part ~= '.' and part ~= '' then
      out[#out + 1] = part
    end
  end

  local res = table.concat(out, '/')
  if isAbs then
    res = '/' .. res
  end
  return res
end

return normalize
