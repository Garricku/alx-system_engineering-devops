# This manifest configures Nginx to include a custom HTTP header in its HTTP response.
# The name of the custom HTTP header is X-Served-By, and the value is the hostname of the server Nginx is running on.

# Install Nginx
class { 'nginx': }

# Configure Nginx
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "add_header X-Served-By $hostname;\n",
  notify  => Service['nginx'],
}
