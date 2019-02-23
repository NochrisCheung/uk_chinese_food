# Parse all links to stories from search result
def bbc_links_parse():
    from bs4 import BeautifulSoup
    import requests

    url = requests.get("https://www.bbc.co.uk/search?q=levi%27s+jeans&sa_f=search-product&scope=")
    page_code = BeautifulSoup(url.content, 'html.parser')

    bbc_links = page_code.find_all('ol', attrs={"class": "search-results results"})
    bbc_links = bbc_links[0].find_all('a', attrs={"class": "rs_touch"})
    bbc_links = [link.attrs["href"] for link in bbc_links]

    all_bbc_stories = []
    for link in bbc_links:
        all_bbc_stories = all_bbc_stories + bbc_stories_parse(link)
        print(len(all_bbc_stories))

    return all_bbc_stories


# Parse stories from each web page
def bbc_stories_parse(story_link):
    from bs4 import BeautifulSoup
    import requests
    import unicodedata

    print(story_link)
    url = requests.get(story_link)
    page_code = BeautifulSoup(url.content, 'html.parser')

    bbc_stories = page_code.findAll("div", attrs={"class": "story-body__inner"})
    # print[len(bbc_stories)]
    if len(bbc_stories) == 0:
        bbc_stories = page_code.findAll("div", attrs={"class": "vxp-media__body"})

    bbc_stories = bbc_stories[0].findAll("p")
    bbc_stories = [story.text for story in bbc_stories]

    return bbc_stories
