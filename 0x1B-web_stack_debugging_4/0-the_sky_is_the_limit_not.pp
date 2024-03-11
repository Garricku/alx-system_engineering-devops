# Install Nginx package (if not already installed)
package { 'nginx':
  ensure  => installed,
}

# Configure Nginx site with minimal rate limiting
file { '/etc/nginx/sites-available/mywebsite':
  ensure  => present,
  content => '
    server {
      listen 80;
      server_name mywebsite.com;

      location / {
        proxy_pass http://my_upstream;
        # Remove rate limiting for all requests
        limit_req off;
      }
    }
  ',
}

# Create symbolic link to enable the site
file { '/etc/nginx/sites-enabled/mywebsite':
  ensure  => link,
  target  => '/etc/nginx/sites-available/mywebsite',
}

# Validate Nginx configuration
exec { 'nginx-config-test':
  command => 'nginx -t',
  path    => '/usr/sbin',
  onlyif  => 'test -f /etc/nginx/sites-available/mywebsite',
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-enabled/mywebsite'],
}
