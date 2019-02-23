from TripAdvisorReviews import get_all_restaurant_href
from TripAdvisorReviews import get_all_regions_href
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#get_all_regions_href()

RegionUrls = open("TripsAdvisorRegionUrl.txt", "r")
for region in RegionUrls:
    get_all_restaurant_href(region)

Pring("Parsing All Completed")
#     print(region)
#
# pattern = re.compile(r"\w*\_\w*")
# region = "/Restaurants-g186338-London_England.html"
#
# matches = pattern.finditer(region)
#
# for match in matches:
#     print(match.group(0))
