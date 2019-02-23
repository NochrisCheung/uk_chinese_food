from ta_reviews import get_all_restaurant_href
from ta_reviews import get_all_regions_href
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
main_dir = os.path.abspath(os.path.join(dname, os.pardir))
code_dir = main_dir + '/data'

#get_all_regions_href()

RegionUrls = open(code_dir & '"TripsAdvisorRegionUrl.txt', 'r')
for region in RegionUrls:
    get_all_restaurant_href(region)

Pring('Parsing All Completed')



#     print(region)
#
# pattern = re.compile(r"\w*\_\w*")
# region = "/Restaurants-g186338-London_England.html"
#
# matches = pattern.finditer(region)
#
# for match in matches:
#     print(match.group(0))
