type,host,port = string.match(ngx.var.request_uri, "/([a-z]*)/([a-zA-Z0-9.-]*)/([0-9]*)$")

local file = os.getenv('AKHET_RUN_DIR') .. type .. '@' .. host .. '@' .. port

function file_exists(file)
  local f = io.open(file, "rb")
  if f then f:close() end
  return f ~= nil
end

if host then
  if port then
    if file_exists(file) then
      ngx.var.request_host     = host;
      ngx.var.request_port     = port;
      return "yes";
    else
      ngx.log(ngx.ERR, "AKHET: Host " .. host .. " with port " .. port .. " not allowd for " .. type)
    end
  end
end
return "no";
