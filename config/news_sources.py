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
    # "spac_filings": {
    #     #  curl -v -X POST https://efts.sec.gov/LATEST/search-index -d '{"dateRange":"5y","startdt":"2020-07-11","enddt":"2020-07-16","category":"all","locationType":"located","locationCode":"all","forms":["424B4","8K"],"page":"1","from":0}'
    #     "url": lambda: "https://efts.sec.gov/LATEST/search-index",
    #     "redirect_url": lambda: "https://www.sec.gov/edgar/search/?r=el#/q=&dateRange=custom&startdt={}&enddt={}&category=all&locationType=located&locationCode=all&ciks=&entityName=&forms=424B4&page=1&SIC=6770".format(
    #         (datetime.now() - timedelta(days=55)).date().strftime("%Y-%m-%d"),
    #         (datetime.now() - timedelta(days=50)).date().strftime("%Y-%m-%d")),
    #     # "element_selector": {"id": "hits"},
    #     "element_selector": {
    #         "key_chain": ["hits", "hits"],
    #         "result_key_filter": ["_source"]
    #     },
    #     "method": "POST",
    #     "payload": lambda: '{{"q":"","dateRange":"custom","startdt":"{}","enddt":"{}","category":"all","locationType":"located","locationCode":"all","ciks":"","entityName":"","forms":["424B4","8k"],"page":"1","SIC":"6770","from":0}}'.format(
    #         (datetime.now() - timedelta(days=55)).date().strftime("%Y-%m-%d"),
    #         (datetime.now() - timedelta(days=50)).date().strftime("%Y-%m-%d")),
    #     "format": "json"
    # },
    "covid_ca_volunteer_94115": {
        "url": lambda: "https://myturnvolunteer.ca.gov/s/sfsites/aura?r=15&aura.ApexAction.execute=1",
        "redirect_url": lambda: "https://myturnvolunteer.ca.gov/s/sfsites/aura?r=15&aura.ApexAction.execute=1",
        "element_selector": {
            "key_chain": ["actions"],
            "result_key_filter": ["returnValue"]
        },
        "method": "POST",
        "payload": lambda: 'message=%7B%22actions%22%3A%5B%7B%22id%22%3A%22189%3Ba%22%2C%22descriptor%22%3A%22aura%3A%2F%2FApexActionController%2FACTION%24execute%22%2C%22callingDescriptor%22%3A%22UNKNOWN%22%2C%22params%22%3A%7B%22namespace%22%3A%22skedvm%22%2C%22classname%22%3A%22LocationController%22%2C%22method%22%3A%22getLocationsByTags%22%2C%22params%22%3A%7B%22type%22%3A%22General%20Support%22%2C%22tags%22%3A%5B%22a3It00000001ocOEAQ%22%2C%22a3It00000001ocnEAA%22%2C%22a3It00000001ocYEAQ%22%5D%2C%22lat%22%3A37.7877522%2C%22lon%22%3A-122.4382307%2C%22max%22%3A50%7D%2C%22cacheable%22%3Afalse%2C%22isContinuation%22%3Afalse%7D%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%228WYDoRiNKzw4em08r-Gg4A%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%22wVxIbCAtfa9TUPXbbfmRlA%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.pageURI=%2Fs%2F%23search&aura.token=undefined',
        "format": "json",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Accept": "*/*",
            "Accept-Language": "en-us",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "myturnvolunteer.ca.gov",
            "Origin": "https://myturnvolunteer.ca.gov",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Referer": "https://myturnvolunteer.ca.gov/s/",
            "Content-Length": "978",
            "Connection": "keep-alive",
            "Cookie": "renderCtx=%7B%22pageId%22%3A%221c197c3d-cbe6-4c69-90ac-908f2aa73bbe%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%22f5c37b15-72c4-4421-af84-37960d2fa7e0%22%2C%22audienceIds%22%3A%22%22%7D; _ga=GA1.2.279432795.1609113614; _gat_gtag_UA_21974567_38=1; _gat_gtag_UA_3419582_2=1; _gid=GA1.2.849401557.1615227220; nmstat=d6179bd7-8eea-91da-10e4-fca126cf7138; pctrk=a1b2e779-7598-4483-b388-3d5804ec92d6; CookieConsentPolicy=0:0; _ga_RJPGSHNVCG=GS1.1.1615227219.1.1.1615227354.0; bm_sv=FFE62D854A710FAC1507DD7CCD4C6086~PReV2Wd6bf1f7lJqSoyZNfug2XGN5bJKG8OQZxnpAaGyLAW+1RZguUuiUj7KMO7c3iu4wvKv7H1nrmkHEHGcYz3ENC8t173JgrbosbhJA/FTHi1Q38aL9J9a1EKZO++p3XHYF5iJeN3//5KmXljPgw==; _abck=76CF50A8B9683FEF3DD66522373B0206~0~YAAQDXpCFwWUtRJ4AQAAr2sLEwUVb/bn1ifeRPp6ZgBMMELYiFyewyvAqpC2QTTeENiKTBmmKJUsQC0BrUAaBzepqtA9vr7YHd/Vxi4IOYUbUf+rks3PIRaYVmxH6m3pq4NCiCZ9eV9Irlm5m5jcrQKYRTePBtN1nq6afiBzK0yn7z7CeGnT8DF+K/YWBgsnX+JhK/VNNGlLxdzcQc/cr5/2ARMP4VsFoj8kdeTxYPfOCRNnpLZL6iiTg5GwrLUWJeidTaNtMdipqIQCjqmVaHmXo9CRVuf0pKqIB5OX7UqUtu1LGQ230yqmVxyFjF3Bu+XREDNVgLr/OZ7TuROJ957JbZVJoyDmnSevxPP1hUFaLCoVdQPZhSN+Auz3pnQTkhEf8IizsIAPnG9uRjVdqFcZQDH0~-1~-1~-1; ak_bmsc=8697F9C4EBB232BDC227431D728C707317427A0D524400005269466078CD5414~plIkFcQihSnmEGBN3aJSK8aoRx9bd503JFIQzBGCwM8Xgm3t3sFjPXZlkawHxQVsE2SCNuanf02Jc/vKh3lFXu35T8VYB5fPkqZkHE4+L4KSgLS4Op2kfH6Np8nlhUxKHGvowdDIGqqlRVV33ad8DO0lmn3gTvFtuSEoNjC0h7fUkiM5s2aUDuYpMrKjckr+poncVM5r62Guwx0U4/FMrh2ohPBX4isOv88vX97F4sXEA=; bm_sz=B7D161A8D66E74B845A3F19E99E5DF5B~YAAQDXpCFwSUtRJ4AQAAr2sLEwvD6wFUn0KHp38N3md3xuMgvPoKAv1WWm9zGpN5LsYvflgoJQJx41qvSmCsqMwVLJqRzPk/RTUj6q3nfg6Ul4r4WWlDQY2Gh9LDOz0W3wkYFe9Xbg0O42TSRTxKDiq2Q8abEsI/iNrFJPLP9cICcYcWsPH4mmQrShc=; _ga_HPRCS5B3HR=GS1.1.1614894971.1.1.1614894982.0; _fbp=fb.1.1614143042605.1252045291",
            "X-SFDC-Request-Id": "200063000000bbe8db",
            "X-SFDC-Page-Scope-Id": "54259842-0224-4a70-a77d-7f4399bc7f7d"
        }
    },
    "covid_ca_volunteer_96150": {
        "url": lambda: "https://myturnvolunteer.ca.gov/s/sfsites/aura?r=15&aura.ApexAction.execute=1",
        "redirect_url": lambda: "https://myturnvolunteer.ca.gov/s/sfsites/aura?r=15&aura.ApexAction.execute=1",
        "element_selector": {
            "key_chain": ["actions"],
            "result_key_filter": ["returnValue"]
        },
        "method": "POST",
        "payload": lambda: 'message=%7B%22actions%22%3A%5B%7B%22id%22%3A%22180%3Ba%22%2C%22descriptor%22%3A%22aura%3A%2F%2FApexActionController%2FACTION%24execute%22%2C%22callingDescriptor%22%3A%22UNKNOWN%22%2C%22params%22%3A%7B%22namespace%22%3A%22skedvm%22%2C%22classname%22%3A%22LocationController%22%2C%22method%22%3A%22getLocationsByTags%22%2C%22params%22%3A%7B%22type%22%3A%22General%20Support%22%2C%22tags%22%3A%5B%22a3It00000001ocOEAQ%22%2C%22a3It00000001ocYEAQ%22%2C%22a3It00000001ocnEAA%22%5D%2C%22lat%22%3A38.8864448%2C%22lon%22%3A-119.9971769%2C%22max%22%3A50%7D%2C%22cacheable%22%3Afalse%2C%22isContinuation%22%3Afalse%7D%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%228WYDoRiNKzw4em08r-Gg4A%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%22wVxIbCAtfa9TUPXbbfmRlA%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.pageURI=%2Fs%2F%23search&aura.token=undefined',
        "format": "json",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Accept": "*/*",
            "Accept-Language": "en-us",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "myturnvolunteer.ca.gov",
            "Origin": "https://myturnvolunteer.ca.gov",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Referer": "https://myturnvolunteer.ca.gov/s/",
            "Content-Length": "978",
            "Connection": "keep-alive",
            "Cookie": "renderCtx=%7B%22pageId%22%3A%221c197c3d-cbe6-4c69-90ac-908f2aa73bbe%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%22f5c37b15-72c4-4421-af84-37960d2fa7e0%22%2C%22audienceIds%22%3A%22%22%7D; _ga=GA1.2.279432795.1609113614; _gat_gtag_UA_21974567_38=1; _gat_gtag_UA_3419582_2=1; _gid=GA1.2.849401557.1615227220; nmstat=d6179bd7-8eea-91da-10e4-fca126cf7138; pctrk=a1b2e779-7598-4483-b388-3d5804ec92d6; CookieConsentPolicy=0:0; _ga_RJPGSHNVCG=GS1.1.1615227219.1.1.1615227354.0; bm_sv=FFE62D854A710FAC1507DD7CCD4C6086~PReV2Wd6bf1f7lJqSoyZNfug2XGN5bJKG8OQZxnpAaGyLAW+1RZguUuiUj7KMO7c3iu4wvKv7H1nrmkHEHGcYz3ENC8t173JgrbosbhJA/FTHi1Q38aL9J9a1EKZO++p3XHYF5iJeN3//5KmXljPgw==; _abck=76CF50A8B9683FEF3DD66522373B0206~0~YAAQDXpCFwWUtRJ4AQAAr2sLEwUVb/bn1ifeRPp6ZgBMMELYiFyewyvAqpC2QTTeENiKTBmmKJUsQC0BrUAaBzepqtA9vr7YHd/Vxi4IOYUbUf+rks3PIRaYVmxH6m3pq4NCiCZ9eV9Irlm5m5jcrQKYRTePBtN1nq6afiBzK0yn7z7CeGnT8DF+K/YWBgsnX+JhK/VNNGlLxdzcQc/cr5/2ARMP4VsFoj8kdeTxYPfOCRNnpLZL6iiTg5GwrLUWJeidTaNtMdipqIQCjqmVaHmXo9CRVuf0pKqIB5OX7UqUtu1LGQ230yqmVxyFjF3Bu+XREDNVgLr/OZ7TuROJ957JbZVJoyDmnSevxPP1hUFaLCoVdQPZhSN+Auz3pnQTkhEf8IizsIAPnG9uRjVdqFcZQDH0~-1~-1~-1; ak_bmsc=8697F9C4EBB232BDC227431D728C707317427A0D524400005269466078CD5414~plIkFcQihSnmEGBN3aJSK8aoRx9bd503JFIQzBGCwM8Xgm3t3sFjPXZlkawHxQVsE2SCNuanf02Jc/vKh3lFXu35T8VYB5fPkqZkHE4+L4KSgLS4Op2kfH6Np8nlhUxKHGvowdDIGqqlRVV33ad8DO0lmn3gTvFtuSEoNjC0h7fUkiM5s2aUDuYpMrKjckr+poncVM5r62Guwx0U4/FMrh2ohPBX4isOv88vX97F4sXEA=; bm_sz=B7D161A8D66E74B845A3F19E99E5DF5B~YAAQDXpCFwSUtRJ4AQAAr2sLEwvD6wFUn0KHp38N3md3xuMgvPoKAv1WWm9zGpN5LsYvflgoJQJx41qvSmCsqMwVLJqRzPk/RTUj6q3nfg6Ul4r4WWlDQY2Gh9LDOz0W3wkYFe9Xbg0O42TSRTxKDiq2Q8abEsI/iNrFJPLP9cICcYcWsPH4mmQrShc=; _ga_HPRCS5B3HR=GS1.1.1614894971.1.1.1614894982.0; _fbp=fb.1.1614143042605.1252045291",
            "X-SFDC-Request-Id": "200063000000bbe8db",
            "X-SFDC-Page-Scope-Id": "54259842-0224-4a70-a77d-7f4399bc7f7d"
        }
    },
    "covid_ca_volunteer_94203": {
        "url": lambda: "https://myturnvolunteer.ca.gov/s/sfsites/aura?r=15&aura.ApexAction.execute=1",
        "redirect_url": lambda: "https://myturnvolunteer.ca.gov/s/sfsites/aura?r=15&aura.ApexAction.execute=1",
        "element_selector": {
            "key_chain": ["actions"],
            "result_key_filter": ["returnValue"]
        },
        "method": "POST",
        "payload": lambda: 'message=%7B%22actions%22%3A%5B%7B%22id%22%3A%22180%3Ba%22%2C%22descriptor%22%3A%22aura%3A%2F%2FApexActionController%2FACTION%24execute%22%2C%22callingDescriptor%22%3A%22UNKNOWN%22%2C%22params%22%3A%7B%22namespace%22%3A%22skedvm%22%2C%22classname%22%3A%22LocationController%22%2C%22method%22%3A%22getLocationsByTags%22%2C%22params%22%3A%7B%22type%22%3A%22General%20Support%22%2C%22tags%22%3A%5B%22a3It00000001ocOEAQ%22%2C%22a3It00000001ocYEAQ%22%2C%22a3It00000001ocnEAA%22%5D%2C%22lat%22%3A38.8864448%2C%22lon%22%3A-119.9971769%2C%22max%22%3A50%7D%2C%22cacheable%22%3Afalse%2C%22isContinuation%22%3Afalse%7D%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%228WYDoRiNKzw4em08r-Gg4A%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%22wVxIbCAtfa9TUPXbbfmRlA%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.pageURI=%2Fs%2F%23search&aura.token=undefined',
        "format": "json",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Accept": "*/*",
            "Accept-Language": "en-us",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "myturnvolunteer.ca.gov",
            "Origin": "https://myturnvolunteer.ca.gov",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Referer": "https://myturnvolunteer.ca.gov/s/",
            "Content-Length": "978",
            "Connection": "keep-alive",
            "Cookie": "renderCtx=%7B%22pageId%22%3A%221c197c3d-cbe6-4c69-90ac-908f2aa73bbe%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%22f5c37b15-72c4-4421-af84-37960d2fa7e0%22%2C%22audienceIds%22%3A%22%22%7D; _ga=GA1.2.279432795.1609113614; _gat_gtag_UA_21974567_38=1; _gat_gtag_UA_3419582_2=1; _gid=GA1.2.849401557.1615227220; nmstat=d6179bd7-8eea-91da-10e4-fca126cf7138; pctrk=a1b2e779-7598-4483-b388-3d5804ec92d6; CookieConsentPolicy=0:0; _ga_RJPGSHNVCG=GS1.1.1615227219.1.1.1615227354.0; bm_sv=FFE62D854A710FAC1507DD7CCD4C6086~PReV2Wd6bf1f7lJqSoyZNfug2XGN5bJKG8OQZxnpAaGyLAW+1RZguUuiUj7KMO7c3iu4wvKv7H1nrmkHEHGcYz3ENC8t173JgrbosbhJA/FTHi1Q38aL9J9a1EKZO++p3XHYF5iJeN3//5KmXljPgw==; _abck=76CF50A8B9683FEF3DD66522373B0206~0~YAAQDXpCFwWUtRJ4AQAAr2sLEwUVb/bn1ifeRPp6ZgBMMELYiFyewyvAqpC2QTTeENiKTBmmKJUsQC0BrUAaBzepqtA9vr7YHd/Vxi4IOYUbUf+rks3PIRaYVmxH6m3pq4NCiCZ9eV9Irlm5m5jcrQKYRTePBtN1nq6afiBzK0yn7z7CeGnT8DF+K/YWBgsnX+JhK/VNNGlLxdzcQc/cr5/2ARMP4VsFoj8kdeTxYPfOCRNnpLZL6iiTg5GwrLUWJeidTaNtMdipqIQCjqmVaHmXo9CRVuf0pKqIB5OX7UqUtu1LGQ230yqmVxyFjF3Bu+XREDNVgLr/OZ7TuROJ957JbZVJoyDmnSevxPP1hUFaLCoVdQPZhSN+Auz3pnQTkhEf8IizsIAPnG9uRjVdqFcZQDH0~-1~-1~-1; ak_bmsc=8697F9C4EBB232BDC227431D728C707317427A0D524400005269466078CD5414~plIkFcQihSnmEGBN3aJSK8aoRx9bd503JFIQzBGCwM8Xgm3t3sFjPXZlkawHxQVsE2SCNuanf02Jc/vKh3lFXu35T8VYB5fPkqZkHE4+L4KSgLS4Op2kfH6Np8nlhUxKHGvowdDIGqqlRVV33ad8DO0lmn3gTvFtuSEoNjC0h7fUkiM5s2aUDuYpMrKjckr+poncVM5r62Guwx0U4/FMrh2ohPBX4isOv88vX97F4sXEA=; bm_sz=B7D161A8D66E74B845A3F19E99E5DF5B~YAAQDXpCFwSUtRJ4AQAAr2sLEwvD6wFUn0KHp38N3md3xuMgvPoKAv1WWm9zGpN5LsYvflgoJQJx41qvSmCsqMwVLJqRzPk/RTUj6q3nfg6Ul4r4WWlDQY2Gh9LDOz0W3wkYFe9Xbg0O42TSRTxKDiq2Q8abEsI/iNrFJPLP9cICcYcWsPH4mmQrShc=; _ga_HPRCS5B3HR=GS1.1.1614894971.1.1.1614894982.0; _fbp=fb.1.1614143042605.1252045291",
            "X-SFDC-Request-Id": "200063000000bbe8db",
            "X-SFDC-Page-Scope-Id": "54259842-0224-4a70-a77d-7f4399bc7f7d"
        }
    },
    "covid_ca_volunteer_94089": {
        "url": lambda: "https://myturnvolunteer.ca.gov/s/sfsites/aura?r=15&aura.ApexAction.execute=1",
        "redirect_url": lambda: "https://myturnvolunteer.ca.gov/s/sfsites/aura?r=15&aura.ApexAction.execute=1",
        "element_selector": {
            "key_chain": ["actions"],
            "result_key_filter": ["returnValue"]
        },
        "method": "POST",
        "payload": lambda: 'message=%7B%22actions%22%3A%5B%7B%22id%22%3A%22188%3Ba%22%2C%22descriptor%22%3A%22aura%3A%2F%2FApexActionController%2FACTION%24execute%22%2C%22callingDescriptor%22%3A%22UNKNOWN%22%2C%22params%22%3A%7B%22namespace%22%3A%22skedvm%22%2C%22classname%22%3A%22LocationController%22%2C%22method%22%3A%22getLocationsByTags%22%2C%22params%22%3A%7B%22type%22%3A%22General%20Support%22%2C%22tags%22%3A%5B%22a3It00000001ocOEAQ%22%2C%22a3It00000001ocYEAQ%22%2C%22a3It00000001ocnEAA%22%5D%2C%22lat%22%3A37.4110966%2C%22lon%22%3A-122.0181762%2C%22max%22%3A50%7D%2C%22cacheable%22%3Afalse%2C%22isContinuation%22%3Afalse%7D%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%228WYDoRiNKzw4em08r-Gg4A%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%22wVxIbCAtfa9TUPXbbfmRlA%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.pageURI=%2Fs%2F%23search&aura.token=undefined',
        "format": "json",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Accept": "*/*",
            "Accept-Language": "en-us",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "myturnvolunteer.ca.gov",
            "Origin": "https://myturnvolunteer.ca.gov",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Referer": "https://myturnvolunteer.ca.gov/s/",
            "Content-Length": "978",
            "Connection": "keep-alive",
            "Cookie": "renderCtx=%7B%22pageId%22%3A%221c197c3d-cbe6-4c69-90ac-908f2aa73bbe%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%22f5c37b15-72c4-4421-af84-37960d2fa7e0%22%2C%22audienceIds%22%3A%22%22%7D; _ga=GA1.2.279432795.1609113614; _gat_gtag_UA_21974567_38=1; _gat_gtag_UA_3419582_2=1; _gid=GA1.2.849401557.1615227220; nmstat=d6179bd7-8eea-91da-10e4-fca126cf7138; pctrk=a1b2e779-7598-4483-b388-3d5804ec92d6; CookieConsentPolicy=0:0; _ga_RJPGSHNVCG=GS1.1.1615227219.1.1.1615227354.0; bm_sv=FFE62D854A710FAC1507DD7CCD4C6086~PReV2Wd6bf1f7lJqSoyZNfug2XGN5bJKG8OQZxnpAaGyLAW+1RZguUuiUj7KMO7c3iu4wvKv7H1nrmkHEHGcYz3ENC8t173JgrbosbhJA/FTHi1Q38aL9J9a1EKZO++p3XHYF5iJeN3//5KmXljPgw==; _abck=76CF50A8B9683FEF3DD66522373B0206~0~YAAQDXpCFwWUtRJ4AQAAr2sLEwUVb/bn1ifeRPp6ZgBMMELYiFyewyvAqpC2QTTeENiKTBmmKJUsQC0BrUAaBzepqtA9vr7YHd/Vxi4IOYUbUf+rks3PIRaYVmxH6m3pq4NCiCZ9eV9Irlm5m5jcrQKYRTePBtN1nq6afiBzK0yn7z7CeGnT8DF+K/YWBgsnX+JhK/VNNGlLxdzcQc/cr5/2ARMP4VsFoj8kdeTxYPfOCRNnpLZL6iiTg5GwrLUWJeidTaNtMdipqIQCjqmVaHmXo9CRVuf0pKqIB5OX7UqUtu1LGQ230yqmVxyFjF3Bu+XREDNVgLr/OZ7TuROJ957JbZVJoyDmnSevxPP1hUFaLCoVdQPZhSN+Auz3pnQTkhEf8IizsIAPnG9uRjVdqFcZQDH0~-1~-1~-1; ak_bmsc=8697F9C4EBB232BDC227431D728C707317427A0D524400005269466078CD5414~plIkFcQihSnmEGBN3aJSK8aoRx9bd503JFIQzBGCwM8Xgm3t3sFjPXZlkawHxQVsE2SCNuanf02Jc/vKh3lFXu35T8VYB5fPkqZkHE4+L4KSgLS4Op2kfH6Np8nlhUxKHGvowdDIGqqlRVV33ad8DO0lmn3gTvFtuSEoNjC0h7fUkiM5s2aUDuYpMrKjckr+poncVM5r62Guwx0U4/FMrh2ohPBX4isOv88vX97F4sXEA=; bm_sz=B7D161A8D66E74B845A3F19E99E5DF5B~YAAQDXpCFwSUtRJ4AQAAr2sLEwvD6wFUn0KHp38N3md3xuMgvPoKAv1WWm9zGpN5LsYvflgoJQJx41qvSmCsqMwVLJqRzPk/RTUj6q3nfg6Ul4r4WWlDQY2Gh9LDOz0W3wkYFe9Xbg0O42TSRTxKDiq2Q8abEsI/iNrFJPLP9cICcYcWsPH4mmQrShc=; _ga_HPRCS5B3HR=GS1.1.1614894971.1.1.1614894982.0; _fbp=fb.1.1614143042605.1252045291",
            "X-SFDC-Request-Id": "200063000000bbe8db",
            "X-SFDC-Page-Scope-Id": "54259842-0224-4a70-a77d-7f4399bc7f7d"
        }
    },

}
'''

curl 'https://myturnvolunteer.ca.gov/s/sfsites/aura?r=22&aura.ApexAction.execute=1' \
-X 'POST' \
-H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8' \
-H 'Accept: */*' \
-H 'Accept-Language: en-us' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Host: myturnvolunteer.ca.gov' \
-H 'Origin: https://myturnvolunteer.ca.gov' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15' \
-H 'Referer: https://myturnvolunteer.ca.gov/s/' \
-H 'Content-Length: 978' \
-H 'Connection: keep-alive' \
-H 'Cookie: renderCtx=%7B%22pageId%22%3A%224d72295e-92a7-4b09-9a8d-fe789ec4b457%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%22f5c37b15-72c4-4421-af84-37960d2fa7e0%22%2C%22audienceIds%22%3A%22%22%7D; _ga=GA1.2.279432795.1609113614; _gid=GA1.2.849401557.1615227220; nmstat=d6179bd7-8eea-91da-10e4-fca126cf7138; pctrk=a1b2e779-7598-4483-b388-3d5804ec92d6; CookieConsentPolicy=0:0; _ga_RJPGSHNVCG=GS1.1.1615227219.1.1.1615227354.0; _abck=76CF50A8B9683FEF3DD66522373B0206~0~YAAQDXpCFwWUtRJ4AQAAr2sLEwUVb/bn1ifeRPp6ZgBMMELYiFyewyvAqpC2QTTeENiKTBmmKJUsQC0BrUAaBzepqtA9vr7YHd/Vxi4IOYUbUf+rks3PIRaYVmxH6m3pq4NCiCZ9eV9Irlm5m5jcrQKYRTePBtN1nq6afiBzK0yn7z7CeGnT8DF+K/YWBgsnX+JhK/VNNGlLxdzcQc/cr5/2ARMP4VsFoj8kdeTxYPfOCRNnpLZL6iiTg5GwrLUWJeidTaNtMdipqIQCjqmVaHmXo9CRVuf0pKqIB5OX7UqUtu1LGQ230yqmVxyFjF3Bu+XREDNVgLr/OZ7TuROJ957JbZVJoyDmnSevxPP1hUFaLCoVdQPZhSN+Auz3pnQTkhEf8IizsIAPnG9uRjVdqFcZQDH0~-1~-1~-1; bm_sz=B7D161A8D66E74B845A3F19E99E5DF5B~YAAQDXpCFwSUtRJ4AQAAr2sLEwvD6wFUn0KHp38N3md3xuMgvPoKAv1WWm9zGpN5LsYvflgoJQJx41qvSmCsqMwVLJqRzPk/RTUj6q3nfg6Ul4r4WWlDQY2Gh9LDOz0W3wkYFe9Xbg0O42TSRTxKDiq2Q8abEsI/iNrFJPLP9cICcYcWsPH4mmQrShc=; _ga_HPRCS5B3HR=GS1.1.1614894971.1.1.1614894982.0' \
-H 'X-SFDC-Request-Id: 718766000000774bdf' \
-H 'X-SFDC-Page-Scope-Id: 1ff42952-c1e4-4e33-84fb-2ea37544b8c3' \
--data 'message=%7B%22actions%22%3A%5B%7B%22id%22%3A%22188%3Ba%22%2C%22descriptor%22%3A%22aura%3A%2F%2FApexActionController%2FACTION%24execute%22%2C%22callingDescriptor%22%3A%22UNKNOWN%22%2C%22params%22%3A%7B%22namespace%22%3A%22skedvm%22%2C%22classname%22%3A%22LocationController%22%2C%22method%22%3A%22getLocationsByTags%22%2C%22params%22%3A%7B%22type%22%3A%22General%20Support%22%2C%22tags%22%3A%5B%22a3It00000001ocOEAQ%22%2C%22a3It00000001ocYEAQ%22%2C%22a3It00000001ocnEAA%22%5D%2C%22lat%22%3A37.4110966%2C%22lon%22%3A-122.0181762%2C%22max%22%3A50%7D%2C%22cacheable%22%3Afalse%2C%22isContinuation%22%3Afalse%7D%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%228WYDoRiNKzw4em08r-Gg4A%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%22wVxIbCAtfa9TUPXbbfmRlA%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.pageURI=%2Fs%2F%23search&aura.token=undefined'
'''
