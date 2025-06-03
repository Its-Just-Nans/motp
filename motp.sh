#!/bin/bash

# https://motp.sourceforge.net/
# https://motp.n4n5.dev/
# https://github.com/Its-Just-Nans/motp

if [ ! -f "$HOME/motp-hex" ]; then
    echo "$HOME/motp-hex is not found - the MOTP code will be incorrect"
fi

if [ ! -f "$HOME/motp-pin" ]; then
    echo "$HOME/motp-pin is not found - the MOTP code will be incorrect"
fi


secret=$(cat "$HOME/motp-hex")
pin=$(cat "$HOME/motp-pin")

epoch_time=$(date +%s)
counter=$((epoch_time / 10))
string_to_hash="${counter}${secret}${pin}"
hash=$(echo -n "$string_to_hash" | md5sum | cut -c1-6)

echo "$hash"
