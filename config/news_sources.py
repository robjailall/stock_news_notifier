news_sources = {
    "treasury_emergency_loans": {
        "url": "https://home.treasury.gov/policy-issues/cares/preserving-jobs-for-american-industry/loans-to-air-carriers-eligible-businesses-and-national-security-businesses",
        "element_selector": {"id": "national-loans"}
    },
    "development_finance_corp_loi": {
        "url": "https://www.dfc.gov/search/node?keys=letter%20of%20interest",
        "element_selector": {
            "class": "region-content"
        }
    },
    "hhs_warp_speed": {
        "url": "https://search.hhs.gov/searchblox/servlet/SearchServlet?HHS=Search&adsCname=HHS&adsDisplay=true&cname=hhsgov_only&startdate=3&startdate=0&default=AND&facet=true&page=1&pagesize=30&query=Warp%2520speed%2520contract%2520&tune=true&tune.0=10&tune.1=8&tune.2=2&tune.3=5&tune.4=365&tune.5=30&xsl=json",
        "format": "json",
        "element_selector": {
            "key_chain": ["results", "result"],
            "result_key_filter": ["title", "description"]
        },
        # "element_selector": {"id": "results_list"},
        "redirect_url": "https://tinyurl.com/y3vge6wa"
    }
}