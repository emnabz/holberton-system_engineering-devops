#webstack debugging
exec { 'debugging':
  path     => ['/bin', '/usr/bin', '/usr/sbin'],
  provider => 'shell',
  command  => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
}
