# this manifest installs Nginx and adds a custom header to Nginx 
 
exec {'apt-update': 
  command => '/usr/bin/apt update', 
} 
 
# installs nginx 
package {'nginx': 
  ensure          => 'installed', 
  provider        => 'apt', 
  install_options => ['--force-yes'], 
} 
 
# Configres Nginx with a customized header 
file_line {'add header': 
  ensure => 'present', 
  path   => '/etc/nginx/sites-available/default', 
  line   => '\tadd_header X-Served-By ${hostname};', 
  after  => 'server_name _;', 
} 
 
# starts running nginx 
service {'nginx': 
  ensure => 'running', 
  require => Package['nginx'], 
}
