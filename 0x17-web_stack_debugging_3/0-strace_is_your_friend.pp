# Puppet manifest to fix Apache 500 error by restarting Apache service

# Define an exec resource to restart the Apache service
exec { 'restart-apache':
  command      => '/usr/sbin/service apache2 restart', 
  path         => '/usr/bin:/bin',
  refreshonly  => true, # Specify that this exec resource should only run when notified
}

# Define the Apache service
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['restart-apache'], # Subscribe to the restart-apache exec to trigger restart
}
