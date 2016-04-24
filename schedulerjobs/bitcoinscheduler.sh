#run the compare_traffic job every hour
#this job will be run as part of crontab
psql -U postgres -d bitcount -a -f compare_traffic.sql
echo schedulerjobran
