# Kills a process named killmenow
file exec {'pkill -15 killmenow':
  path  => '/usr/bin:/usr/sbin:/bin',
}
