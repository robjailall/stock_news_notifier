from datetime import datetime, timedelta

news_sources = {
    "treasury_emergency_loans": {
        "url": lambda: "https://home.treasury.gov/policy-issues/cares/preserving-jobs-for-american-industry/loans-to-air-carriers-eligible-businesses-and-national-security-businesses",
        "element_selector": {"id": "national-loans"}
    },
    # "development_finance_corp_loi": {
    #     "url": lambda: "https://www.dfc.gov/search/node?keys=letter%20of%20interest",
    #     "element_selector": {
    #         "class": "region-content"
    #     }
    # },
    # "hhs_warp_speed": {
    #     "url": lambda: "https://search.hhs.gov/searchblox/servlet/SearchServlet?HHS=Search&adsCname=HHS&adsDisplay=true&cname=hhsgov_only&startdate=3&startdate=0&default=AND&facet=true&page=1&pagesize=30&query=Warp%2520speed%2520contract%2520&tune=true&tune.0=10&tune.1=8&tune.2=2&tune.3=5&tune.4=365&tune.5=30&xsl=json",
    #     "format": "json",
    #     "element_selector": {
    #         "key_chain": ["results", "result"],
    #         "result_key_filter": ["title", "description"]
    #     },
    #     # "element_selector": {"id": "results_list"},
    #     "redirect_url": lambda: "https://tinyurl.com/y3vge6wa"
    # },
    "spac_filings": {
        #  curl -v -X POST https://efts.sec.gov/LATEST/search-index -d '{"dateRange":"5y","startdt":"2020-07-11","enddt":"2020-07-16","category":"all","locationType":"located","locationCode":"all","forms":["424B4","8K"],"page":"1","from":0}'
        "url": lambda: "https://efts.sec.gov/LATEST/search-index",
        "redirect_url": lambda: "https://www.sec.gov/edgar/search/?r=el#/q=&dateRange=custom&startdt={}&enddt={}&category=all&locationType=located&locationCode=all&ciks=&entityName=&forms=424B4&page=1&SIC=6770".format(
            (datetime.now() - timedelta(days=55)).date().strftime("%Y-%m-%d"),
            (datetime.now() - timedelta(days=50)).date().strftime("%Y-%m-%d")),
        # "element_selector": {"id": "hits"},
        "element_selector": {
            "key_chain": ["hits", "hits"],
            "result_key_filter": ["_source"]
        },
        "method": "POST",
        "payload": lambda: '{{"q":"","dateRange":"custom","startdt":"{}","enddt":"{}","category":"all","locationType":"located","locationCode":"all","ciks":"","entityName":"","forms":["424B4","8k"],"page":"1","SIC":"6770","from":0}}'.format(
            (datetime.now() - timedelta(days=55)).date().strftime("%Y-%m-%d"),
            (datetime.now() - timedelta(days=50)).date().strftime("%Y-%m-%d")),
        "format": "json"
    },
}