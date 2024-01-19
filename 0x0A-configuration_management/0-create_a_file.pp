# Creates a file in /tmp called school with the contents "I love Puppet"

file { '/tmp/school':
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
