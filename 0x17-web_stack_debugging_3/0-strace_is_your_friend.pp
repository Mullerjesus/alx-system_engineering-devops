# Puppet manifest to correct incorrect `phpp` file extensions to `php` in the WordPress configuration file (`wp-settings.php`)

exec { 'fix-phpp-to-php-in-wp-settings':
  command   => 'sed -i.bak "s/phpp/php/g" /var/www/html/wp-settings.php',
  path      => ['/usr/local/bin', '/usr/bin', '/bin', '/usr/sbin', '/sbin'],
  onlyif    => 'grep -q "phpp" /var/www/html/wp-settings.php',
}
