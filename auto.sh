#! /usr/bin/expect <<EOD
spawn git pull
expect "password:"
send "this_is_my_password_unsafely_stored_in_a_bash_script\r"
interact
EOD