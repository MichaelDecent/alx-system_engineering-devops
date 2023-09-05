# this manifest installs Nginx and adds a custom header to Nginx
web_server {
  exec {'apt-update':
  command => 'sudo apt update',
  }

  #installs nginx
  package { 'nginx':
    ensure          => 'installed',
    provider        => 'apt',
    install_options => ['--force-yes'],
    }

  # adds fire wall
  firewall { 'allow nginx':
    port   => 80,
    proto  => 'tcp',
    action => 'accept',
  }

  # Configres Nginx with a customized header
  file { '/etc/nginx/sites-available/default':
    ensure  => 'present',
    content => template('nginx_config.erb'),
    notify  => Exec['nginx-test'],
  }

  # Test the configuration file of Nginx
  exec { 'nginx-test':
    command     => 'sudo nginx -t',
    refreshonly => true,
    notify      => Exec['nginx-restart'],
  }

  # Restarts Nginx 
  exec { 'nginx-restart':
    command     => 'sudo service nginx restart',
    refreshonly => true,
  }

}

