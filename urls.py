from googlesearch import search

def get_google_search_results(query, num_results=10):
    links = []
    for result in search(query, num=num_results, stop=num_results, pause=2):
        links.append(result)
    return links

def main():
    # قائمة بالدوركات الخاصة بثغرة WebDav
    webdav_dorks = [
        "intitle:index.of /webdav",
        "inurl:/webdav",
        "filetype:log inurl:/webdav",
        "inurl:admin inurl:webdav",
        "inurl:/webdav/ -admin"
    ]

    num_results = 10  # Adjust this number based on how many results you want to retrieve

    # البحث عن كل دورك في جوجل
    for dork in webdav_dorks:
        query = dork
        print(f"Searching for: {query}")
        links = get_google_search_results(query, num_results)
        
        print(f"Found links for '{dork}':")
        for link in links:
            print(link)
        print()

if __name__ == "__main__":
    main()
