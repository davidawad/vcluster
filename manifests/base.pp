package {'nginx':
    ensure => present,
}


file {'rm-nginx-default':
    ensure  => absent,
    path    => '/etc/nginx/sites-enabled/default',
    require => Package['nginx'],
}

file {'setup-nginx-codebase':
    ensure  => present,
    path    => '/etc/nginx/sites-enabled/codebase_nginx',
    require => Package['nginx'],
    source  => '/vagrant/codebase_nginx',
}
