service { 'apache2':
  ensure  => 'running',
}

# Correct the permission on the configuration file
file { '/etc/apache2/httpd.conf':
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('my_module/httpd.conf.erb'),  # Use your own template
  notify  => Service['apache2'],
}

# Ensure the mod_php module is loaded
exec { 'load_mod_php':
  command => '/usr/sbin/a2enmod php5',  # Adjust as needed
  creates => '/etc/apache2/mods-enabled/php5.load',
  require => File['/etc/apache2/httpd.conf'],
  notify  => Service['apache2'],
}
