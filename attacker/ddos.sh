xargs -I % -P 5 curl -I $DOS_TARGET < <(printf '%s\n' {1..10})