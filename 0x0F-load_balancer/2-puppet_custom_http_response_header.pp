# Creating a custom HTTP header response with Puppet

# First Update Package
exec { 'apt-update':
    command => '/usr/bin/apt-get -y update',
    path    => ['/usr/bin', '/bin'],
}

# Installing Nginx Package
package { 'nginx':
    ensure => installed,
}

# Creating a custom HTTP header response
file_line { 'adding custom header X-Served-By':
    ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    line    => "\tadd_header X-Served-By ${hostname};",
    after   => 'server_name _;',
    notify  => Service['nginx'], # Restart Nginx when the file is updated
    require => Package['nginx'],  # Ensure Nginx is installed first
}

# Ensuring Nginx is running
service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}
