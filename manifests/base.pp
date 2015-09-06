
package {"nginx":
    ensure => present,
}


file {"rm-nginx-default":
    path => '/etc/nginx/sites-enabled/default',
    ensure => absent,
    require => Package['nginx'],
}

file {"setup-nginx-codebase":
    path => '/etc/nginx/sites-enabled/codebase_nginx',
    ensure => present,
    require => Package['nginx'],
    source => "/vagrant/codebase_nginx",
}
