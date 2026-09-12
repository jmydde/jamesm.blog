python3 scripts/validate-tags.py && hugo --cleanDestinationDir && python3 scripts/link-audit.py && rsync -avz --delete public/ root@jamesm.blog:/var/www/vhosts/jamesm.blog/httpdocs/
