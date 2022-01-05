# Kills a process named killmenow
file exec {'pkill killmenow':
  path  => '/usr/bin:/usr/sbin:/bin',
}
