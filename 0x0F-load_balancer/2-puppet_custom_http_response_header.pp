#!/usr/bin/env bash
#install nginx with configurations below

package { 'nginx':
 ensure => installed,
}

file { '/var/www/html':
  ensure => directory,
}

file { '/var/www/html/index.html':
  ensure => present,
  content => 'Hello World!',
}

file {'/var/www/html/404.html':
  ensure => present,
  content => "No page found",
}

file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => '
   server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $hostname;
    root /var/www/html;
    index index.html index.htm;

    location /redirect_me {
     return 301 http://facebook.com/;
    }

    error_page 404 /404.html;
    location /404 {
     root /var/www/html;
     internal;
    }
   }
 ',
}

service  { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/sites-available/default']
}
