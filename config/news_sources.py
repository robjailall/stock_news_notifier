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
        "url": "https://search.hhs.gov/searchblox/servlet/SearchServlet?cname=HHS&facet=true&featuredAds=true&page=1&pagesize=10&query=Warp%2520speed%2520contract%2520&xsl=json",
        "format": "json",
        "redirect_url": "https://search.hhs.gov/searchblox/hhs/index.html?query=Warp%20speed%20contract%20&page=1&pagesize=10&sort=article:modified_time&sortdir=desc&HHS=Search&adsCname=HHS&adsDisplay=true&cname=hhsgov_only&default=AND&tune=true&tune.0=10&tune.1=8&tune.2=2&tune.3=5&tune.4=365&tune.5=30"
    }
}
