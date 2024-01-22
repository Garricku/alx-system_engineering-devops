# Sets up SSH config file so that you can connect without typing a password

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/root/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/root/.ssh/config',
  line   => 'IdentityFile /root/.ssh/school',
  match  => '^#?IdentityFile',
}
