function is_debug(host)
{
  if(host.indexOf('localhost')>=0 || host.indexOf('127.0.0.1')>=0)
  {

    return true;
  }

  return false;
}
