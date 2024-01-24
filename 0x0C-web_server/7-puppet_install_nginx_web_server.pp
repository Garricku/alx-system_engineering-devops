# puppet code to config nginx

class { 'nginx':
  manage_repo       => true,
}

nginx::resource::vhost { 'default':
  www_root          => '/var/www/html',
  listen_port       => '80',
  redirect_to_https => false,
  proxy             => false,
  index_files       => ['index.html'],
  error_log_file    => '/var/log/nginx/error.log',
  access_log_file   => '/var/log/nginx/access.log',
  server_name       => 'localhost',
  ssl               => false,
}
