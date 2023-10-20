# Configures Nginx to handle thousands of requests per
# minutes

$data = 'keepalive_timeout 65;\
\topen_file_cache max=200000 inactive=20s;\
\topen_file_cache_valid 30s;\
\topen_file_cache_min_uses 2;\
\topen_file_cache_errors on;'

exec {'configure_nginx1':
  provider => 'shell',
  cwd      => '/etc/nginx/',
  command  => "sed -i s/'keepalive_timeout 65;'/'${data}'/g  nginx.conf"
}

exec {'configure_nginx2':
  provider => 'shell',
  cwd      => '/etc/nginx/',
  command  => "sed -i s/'# multi_accept on'/'multi_accept on'/g nginx.conf"
}

exec {'restart_nginx':
  provider => 'shell',
  command  => 'service nginx restart',
  require  => Exec['configure_nginx1','configure_nginx2']
}

