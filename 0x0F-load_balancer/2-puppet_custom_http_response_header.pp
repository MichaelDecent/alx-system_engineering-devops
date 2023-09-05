# this manifest installs Nginx and adds a custom header to Nginx

exec {'apt-update':
  command => '/usr/bin/apt update',
}

#installs nginx
package {'nginx':
  ensure          => 'installed',
  provider        => 'apt',
  install_options => ['--force-yes'],
  }

# Configres Nginx with a customized header
file {'/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => '
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  add_header X-Served-By \$hostname;

  root /var/www/html;
  index index.html index.htm index.nginx-debian.html;

  server_name _;

  location / {
      try_files \$uri \$uri/ =404;
  }
}
',
  notify  => Exec['nginx-test'],
}

# Test the configuration file of Nginx
exec {'nginx-test':
  command     => '/usr/sbin/nginx -t',
  refreshonly => true,
  require     => Package['nginx'],
  notify      => Exec['nginx-restart'],
}

  # Restarts Nginx 
exec {'nginx-restart':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  }
