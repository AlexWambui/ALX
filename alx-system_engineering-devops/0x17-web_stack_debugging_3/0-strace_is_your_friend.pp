# Using strace to automate and fix an Apache 500 error

$file_path = '/var/www/html/wp-settings.php'

#replace "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin','/usr/bin']
}
