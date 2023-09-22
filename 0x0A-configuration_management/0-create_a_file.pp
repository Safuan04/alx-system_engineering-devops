file { '/tmp/myfile.txt':
  mode    => '0744',
  owner   => 'www-data',  # Make sure the 'www-data' user exists on your system
  group   => 'www-data',  # Make sure the 'www-data' group exists on your system
  content => 'I love Puppet',
}
