if (!(Test-Path $home/.ssh)) {
    mkdir $home/.ssh
}

cp ./id_rsa $home/.ssh/
cp ./id_rsa.pub $home/.ssh/