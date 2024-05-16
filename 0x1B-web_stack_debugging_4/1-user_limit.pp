# the OS security configuration
exec {'config OS security':
command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
