# Increase the amount of traffic nginx server can handle

# Increase ULIMIT of default file
exec { 'fix--for-nginx':
  # Change ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/defaultnginx',
  # Path for sed command
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  # Restart service
  command => '/etc/init.d/nginx restart',
  # Specify path for init.d script
  path    => '/etc/init.d/',
}
