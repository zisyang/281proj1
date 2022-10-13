mysql -D `grep db_database config.py | cut -d'"' -f 2` -u admin --password=`grep pass config.py | cut -d'"' -f 2`  -h `grep host config.py | cut -d'"' -f 2`

