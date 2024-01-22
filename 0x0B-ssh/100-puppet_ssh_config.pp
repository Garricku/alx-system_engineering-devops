# Sets up SSH config file so that you can connect without typing a password

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/ect/ssh/ssh_config',
  line   => '	IdentityFile ~/.ssh/school',
}
