#install nginx package with puppet
package { 'nginx':
  ensure => 'installed',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('nginx/default.conf.erb'),
  require => Package['nginx']
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-available/default.conf.erb':
  source  => 'puppet:///modules/nginx/default.conf.erb',
  ensure  => 'file',
}

file { '/usr/share/nginx/html/custom_404.html':
  ensure  => 'file',
  content => 'Ceci n'est pas une page',
  require => Package['nginx'],
}

nginx::resource::location { 'redirect_me':
  location => '/redirect_me',
  content  => 'return 301 https://www.example.new_page;',
  require  => Package['nginx']
  notify   => Service['nginx'],
}

class { 'nginx':
  lsiten_port => 80,
}

nginx::resource::location { 'custom_404':
  location => '/custom_404.html',
  content  => '',
  require  => Package['nginx'],
}

class { 'nginx':
  package_manage => false,
  service_manage => false,
}
