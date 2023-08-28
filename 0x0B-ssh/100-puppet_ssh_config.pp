
file {'~/.ssh/school':
content => 'Host ubuntu
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
'
}
