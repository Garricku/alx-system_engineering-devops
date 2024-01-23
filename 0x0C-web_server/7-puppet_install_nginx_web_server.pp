# puppet code to config nginx

class { 'nginx':
  listen_port => '80',
}

nginx::resource::vhost { 'default':
  www_root => '/var/www/html',
  index_files => ['index.html'],
  proxy => 'http://localhost:8080',
  proxy_redirect => 'off',
  rewrite_to_https => true,
  ssl => false,
  ssl_cert => '',
  ssl_key => '',
  ssl_chain => '',
  ssl_port => '',
  ssl_protocols => '',
  ssl_ciphers => '',
  ssl_session_cache => '',
  ssl_session_tickets => '',
  ssl_session_timeout => '',
  ssl_stapling => '',
  ssl_stapling_verify => '',
  ssl_trusted_certificate => '',
  ssl_verify_client => '',
  ssl_verify_depth => '',
  access_log_enabled => true,
  access_log_format => 'combined',
  access_log_file => '/var/log/nginx/access.log',
  error_log_file => '/var/log/nginx/error.log',
  error_log_level => 'warn',
  server_name => '_',
  listen_options => '',
