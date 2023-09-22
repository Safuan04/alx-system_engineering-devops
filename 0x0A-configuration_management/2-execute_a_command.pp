# Puppet program that kills a process named killmenow.

exec {'killmenow':
  command => 'pkill',
  path    => '/usr/bin:/usr/sbin:/bin',
}