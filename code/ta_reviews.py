def get_all_restaurant_href(region_url):

    pattern = re.compile(r"\w*\_\w*")
    region_name = pattern.findinter(region_url)

    for region_n in region_name:
        file = open("TripsAdvisor"+region_u.group(0)+"Url.txt", "w")
        for i in range(0, 100):
            end_of_list = False
            print(str(i))
            url = requests.get(region_url + "-c11-" + str(i*30))
            #print(url.content)
            page_code = BeautifulSoup(url.content, "html.parser")
            all_restaurant_in_page = page_code.findAll("div", id="EATERY_SEARCH_RESULTS")
            restaurant_num_check = all_restaurant_in_page[0].findAll("div", id=re.compile('eatery'))
            if len(restaurant_num_check) < 30:
                end_of_list = True
            k = 0
            unlist_restaurants = []

            for j in range(1, 31):
                try:
                    try:
                        restaurant_url = all_restaurant_in_page[0].findAll("div", attrs = {"data-index": str(j)})
                        restaurant_url = restaurant_url[0].findAll("a", attrs={"target": "_blank"})
                        restaurant_url = restaurant_url[0].attrs["href"]
                        file.write(str(restaurant_url) + "\n")
                    except:
                        pass
                except:
                    end_of_list = True
                    break

            if end_of_list is True:
                break

        file.close()
        return



def get_all_regions_href():
    file = open("TripsAdvisorRegionUrl.txt", "w")

    url = requests.get("https://www.tripadvisor.co.uk/Restaurants-g186217-England.html")
    page_code = BeautifulSoup(url.content, "html.parser")


    region_url = page_code.findAll("div", attrs ={"class":"geo_name"})
    region_url = [region.findAll("a", href = True) for region in region_url]
    pattern = re.compile(r"/\S*html")
    for region in region_url:
        region = pattern.finditer(str(region))
        for r in region:
            file.write(r.group(0) + "\n")

    file.close()
