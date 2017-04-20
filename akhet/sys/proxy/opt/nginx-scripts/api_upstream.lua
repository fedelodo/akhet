function file_exists(file)
  local f = io.open(file, "rb")
  if f then f:close() end
  return f ~= nil
end

function lines_from(file)
  if not file_exists(file) then return {} end
  lines = {}
  for line in io.lines(file) do
    lines[#lines + 1] = line
  end
  return lines
end

local file = os.getenv('AKHET_API_HOSTS_LIST_FILE')

upstream = nil
if file_exists(file) then
  local lines = lines_from(file)
  upstream_index = math.random(1,#lines)
  upstream = lines[upstream_index]
else
  ngx.log(ngx.ERR,"Missing " .. file)
end

if upstream then
  ngx.var.api_upstream     = upstream;
  return "yes";
end
return "no";
