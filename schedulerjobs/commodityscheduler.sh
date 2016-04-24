#run the compare_traffic job once  day
#purpose of this job is to update the commodity transform table with updated
#data from the day.
#this job will be run as part of crontab
psql -U postgres -d bitcount -a -f commodityTransform.sql
echo schedulercommodityTransformran
