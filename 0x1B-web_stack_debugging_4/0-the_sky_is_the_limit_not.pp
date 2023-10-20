# The puppet script increases the amount of traffic the nginx server can handle

exec { 'update-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart the nginx service
-> exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
