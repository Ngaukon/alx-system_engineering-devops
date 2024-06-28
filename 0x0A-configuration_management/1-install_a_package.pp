# Install puppet-lint version 2.5.0
package { 'puppet-lint':
  ensure => '2.5.0',
}

# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  path    => ['/usr/bin', '/usr/sbin'],
}
