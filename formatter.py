import json

urls = []
total_urls = []


# Create json file with the views by url
def writeViews(body):
    if body is not None:
        url = str(body).split('/', 1)[1]
        urls.append(url)

    num_views = {i: urls.count(i) for i in urls}
    with open('num_views.json', 'w') as outfile:
        json.dump(num_views, outfile, indent=2)


# Create the json file with the total views
def writeTotalViews(body):
    if body is not None:
        url = str(body).split('/', 1)[1]
        total_urls.append(url)
        tot_views = {'Total Views': len(urls)}
        with open('tot_views.json', 'w') as outfile:
            json.dump(tot_views, outfile, indent=2)
