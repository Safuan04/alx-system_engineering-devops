# Puppet program to instal flask.

package {'flask':
  ensure => '2.1.0'
  force  => yes
}