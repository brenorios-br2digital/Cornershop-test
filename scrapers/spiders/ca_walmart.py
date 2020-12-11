import scrapy
from scrapy.crawler import CrawlerProcess
import json

from scrapers.items import ProductItem


class CaWalmartSpider(scrapy.Spider):
    name = "ca_walmart"
    allowed_domains = ["walmart.ca"]
    start_urls = [
        "https://www.walmart.ca/en/grocery/fruits-vegetables/fruits/N-3852"]
    baseUrl = 'https://www.walmart.ca'

    branches = [3106, 3124]
    headers = [{
        'Cookie': f'''
                ENV=ak-scus-t1-prod;
                TS01170c9f=01538efd7c6f2e03b9161978f3dc1e473e6763887776617ec126625bbef88338d8a11aed2a1d323c0baafc3e6255f14db5a0a15f46;
                TS017d5bf6=01538efd7c6f2e03b9161978f3dc1e473e6763887776617ec126625bbef88338d8a11aed2a1d323c0baafc3e6255f14db5a0a15f46;
                bstc=VOg2E1R2cJS2df86IPPAo8;
                exp-ck=6V3flk7Xi3l1AN-0L3DwTRU1GpBCe1HbOxV1Jeavw1MZ9tt1NCuxi1Oqgc14X92ox4YJsua5a4vv41dykD11fHfTr2fJumS3lZnE76rwaVg4sGGbM4wx8xe1yI7_k1;
                seqnum=19;
                vtc=Uc-JTxE6pVGBW2hnCjcs5c;
                xpa=2lwWQ|63K3S|6V3fl|7Xi3l|AN-0L|DViIf|DwTRU|GpBCe|HbOxV|Jeavw|LVSOt|MBc1l|MZ9tt|NCuxi|NOaJP|Oqgc1|Q0IHr|X92ox|YJsua|_vY-K|a4vv4|dykD1|fHfTr|fJumS|hcz5Y|jeBOs|lZnE7|mOlOu|rwaVg|sGGbM|sw6qx|wx8xe|yI7_k;
                xpm=1%2B1607533878%2BUc-JTxE6pVGBW2hnCjcs5c~%2B0;
                TS0196c61b=01538efd7c32ed315bbd114a33e4ecc575ebceb1f6deeedf1eab0a39adcf88bacb33a9302cf870b1dfee38cfe54578e8aebc5b00fc;
                akavpau_ca_prod_akamai_vp=1607535726~id=12e876d59508607defba7f65f16f7c35;
                rxVisitor=1607463165268S5SUMOTNT37D10IR5Q0PJ4TNBQQMIURG;
                rxvt=1607537226555|1607535379120; dtPC=-21$135379097_69h-vJLTSWKJXQTEXLFVPCTJUQXOIVPXWWVPH-0;
                _pxde=9de549a468383068a1abfb67419ec718ce5b8020f414dfd24c815b8945a2237e:eyJ0aW1lc3RhbXAiOjE2MDc1MzU0MTkxODAsImZfa2IiOjAsImlwY19pZCI6W119;
                _fbp=fb.1.1607463168492.673750476; _pin_unauth=dWlkPVkyRTNZVEpoTVRNdFlqQTJPUzAwWldSakxXSmtNell0WkRWbU1EbGpZamxqWVdVeQ;
                cto_bundle=Q9xFB19zRW0lMkJ6Tk01U3d0WjhJJTJCU3dtRW8xYjclMkJSZ3FqRGxLMmFVdkxma0w3QWJHZVVxNFFIamJFaHI1Q1hNOWQwM2dFalB6WU1uOHVQMWhXTG9sdnhMdWklMkJZMWJVU1I2RTZtJTJCVU13S0NSQ3hrTlMlMkZmTHdtNHFraFRiV1pLWmNid2xrNg;
                s_ecid=MCMID%7C67974126428989854003572490284746605627;
                s_vi=[CS]v1|2FE7F8818515EEBA-400007B7A3D1B3DD[CE];
                s_visit=1; AMCV_C4C6370453309C960A490D44%40AdobeOrg=-637568504%7CMCIDTS%7C18605%7CMCMID%7C67974126428989854003572490284746605627%7CMCAID%7C2FE7F8818515EEBA-400007B7A3D1B3DD%7CMCOPTOUT-1607542590s%7CNONE%7CMCAAMLH-1608140190%7C9%7CMCAAMB-1608140190%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18612%7CvVersion%7C5.1.1;
                s_cc=true;
                s_gnr=1607535390302-Repeat;
                __gads=ID=bfd93a399836fb58-2226ab447ab80028:T=1607463171:RT=1607535386:S=ALNI_MYHS0pD0Db6IpslZy-FR_pkg8mBhw;
                og_autoship=0;
                _gcl_au=1.1.1429677599.1607463169;
                _px3=d0cf25b187dc2c5acfc6b871eb072671d21dddd5dff97d84d01789d0d12c67f5:VKGZoCyeVBFPobAQRYRerF6kSZTZ2oMrynGp4WF8Xx1Z44TQsIpIKDe1lngIJ2+90qvDHdrQgUryZamBDTBkyA==:1000:m1Moci+KwATZN67y1uogcK31X0xv/v7CCbKMFwKvnoeLFg9ANHAYmfVQy+srXGtbLYaN+9qjWoP4Qrx2rumc3DB2X9gH5wPTsIFPaKWMVLFMDkUwviZwVFLJvP1r7Lmw+Vbd8oZIfxNvQud2oQ6ToqjnXeAWO4QhINVsE7otvjs=;
                _uetsid=eeebf9a0399c11eba6d24d6e8ef1bbd8;
                _uetvid=eeec28e0399c11eb8eaa6d619d095b32;
                _4c_mc_=74ed1c9c-373d-4520-97f5-40501e3ff0cc;
                _ga=GA1.2.630256747.1607463167;
                _gid=GA1.2.833863016.1607463167;
                walmart.locale=en; dtLatC=60;
                dtSa=-; previousBreakpoint=desktop;
                usrState=1; wmt.breakpoint=d;
                headerType=grocery;
                TS011fb5f6=0130aff232e0124c807e45d28963bb987f3a7223834733392143aad7dc9744a8f575f4d39f129dd6b8a248121ff60f6f962929d83a;
                TS0175e29f=0130aff232e0124c807e45d28963bb987f3a7223834733392143aad7dc9744a8f575f4d39f129dd6b8a248121ff60f6f962929d83a;
                TS01f4281b=0130aff232e0124c807e45d28963bb987f3a7223834733392143aad7dc9744a8f575f4d39f129dd6b8a248121ff60f6f962929d83a;
                s_sq=%5B%5BB%5D%5D; authDuration={'"lat":"1607485263764000","lt":"1607485263764000"'};
                defaultNearestStoreId={branch};
                deliveryCatchment={branch};
                localStoreInfo=eyJwb3N0YWxDb2RlIjoiUDdCM1o3IiwibG9jYWxTdG9yZUlkIjoiMzEyNCIsInNlbGVjdGVkU3RvcmVJZCI6IjMxMjQiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IlRodW5kZXIgQmF5IFN1cGVyY2VudHJlIiwiZnVsZmlsbG1lbnRTdG9yZUlkIjoiMzEyNCIsImZ1bGZpbGxtZW50VHlwZSI6IklOU1RPUkVfUElDS1VQIn0=;
                walmart.nearestPostalCode=P7B3Z7;
                walmart.preferredstore={branch};
                walmart.shippingPostalCode=P7B3Z7;
                NEXT_GEN.ENABLED=1;
                cartId=d34a3641-d1c9-4dda-9bcd-e9c5f5eb8526;
                walmart.nearestLatLng="43.60822,-79.69387";
                DYN_USER_ID.ro=5ca84ad4-f199-49b4-8a0c-543a44b7e789;
                BVBRANDID=6610c764-83d6-4a95-bf86-0d86832372f5;
                BVImplmain_site=2036;
                cookiePolicy=true;
                DYN_USER_ID=5ca84ad4-f199-49b4-8a0c-543a44b7e789;
                LT=1607483357377;
                WM_SEC.AUTH_TOKEN=MTAyOTYyMDE419VE21z901+eCBke6kAqFXaY5fgs11z1RrSzrHVw1KEFF+PPZEJ7X2N/yA6v1jPI6xqG4HfJAxmTO9ZC0baNpdFRAJDRiib/NilyxQEdflRc2oCqyXD+Rlub3NXn8otUj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj1Yy1xK8u1ktSlILSxYB5RydR0oSicd8E7RJYYL+Y11PH0io5FWN2P7mWjfETzP0z7b/SoGFgAYL9DGZ8K45WCXb/Ew67/GsLtdlJHpe1JgED7ACF7QTzL/qgSxzrYRB5K7C5ZAKn0VBvKN+J/mYo2Pm64seCgGZHEY1XiZIHfr7CI2ljQKnXXrPQbGONUGGWF/IIE/FkoQBiqMngyju62UUMfDjQelA2l8kWU2EKohBg==;
                _scid=02b83c2f-5f3c-4c53-91b9-a4bf0b01154b;
                _pxvid=ef4ab4ff-399c-11eb-a3c0-0242ac120019;
                og_session_id=af0a84f8847311e3b233bc764e1107f2.630922.1607463175;
                og_session_id_conf=af0a84f8847311e3b233bc764e1107f2.630922.1607463175;
                AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1;
                TBV=13; walmart.id=d22f36f3-8625-4f0b-f0bc-ef7901310c6f;
                dtCookie=-21$8EKMQADVOB5NJ4KG5TBIKH79L6TRTTB4;
                wmt.c=0;
                userSegment=40-percent; walmart.csrf=5756fe2c9c347364ae459d79
                ''',

    } for branch in branches]

    def start_requests(self):
        for header in self.headers:
            yield scrapy.Request(url=self.start_urls[0], callback=self.parse, meta={'branch': header['Cookie'].split('=')[1], 'header': header}, headers=header)

    def parse(self, response):
        # All articles with div class shelf-thumbs pnoDone
        extraction = response.css(
            "input#breadcrumb-dimensions::attr(value), div.shelf-thumbs article a::attr(href)").getall()

        print('RESULTSSSS')

        category = json.loads(extraction[0])["name"]
        branch = response.meta.get('branch')
        header = response.meta.get('header')

        productUrls = extraction[1:]

        print('PRODUCTSURLSSSS')
        print(productUrls)

        newCookie = {
            'Cookie': '''_gat=1;s_gnr=1607536764423-Repeat;
            s_sq=wmicanadaprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DBrowse%25253A%252520Grocery%25253A%252520Fruits%252520%252526%252520Vegetables%25253A%252520Fruits%2526link%253DDel%252520Monte%252520Gold%252520Pineapple%252520Chunks%252520284%252520g%2525200%252520Reviews%252520Price%2525243.97%2526region%253Dthumb-6000198792590%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DBrowse%25253A%252520Grocery%25253A%252520Fruits%252520%252526%252520Vegetables%25253A%252520Fruits%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.walmart.ca%25252Fen%25252Fip%25252Fdel-monte-gold-pineapple-chunks%25252F6000198792589%2526ot%253DA;
            dtPC=-21$135379097_69h27vJLTSWKJXQTEXLFVPCTJUQXOIVPXWWVPH-0; dtSa=false%7CC%7C27%7C6000201058943%7Cx%7C1607536764361%7C135379097_69%7Chttps%3A%2F%2Fwww.walmart.ca%2Fen%2Fgrocery%2Ffruits-vegetables%2Ffruits%2FN-3852%2Fpage-2%7C%7C1607535422429%7C%7C;
            rxVisitor=1607463165268S5SUMOTNT37D10IR5Q0PJ4TNBQQMIURG;
            rxvt=1607538564636|1607535379120;
            _pxde=f83fcb6324dd1b639db1ea1f87a671fe9465c178f7ed9459fd1e5d604b943b15:eyJ0aW1lc3RhbXAiOjE2MDc1MzY2NDc0NjQsImZfa2IiOjAsImlwY19pZCI6W119;
            ENV=ak-scus-t1-prod;
            TS01170c9f=01538efd7c6f2e03b9161978f3dc1e473e6763887776617ec126625bbef88338d8a11aed2a1d323c0baafc3e6255f14db5a0a15f46;
            TS017d5bf6=01538efd7c6f2e03b9161978f3dc1e473e6763887776617ec126625bbef88338d8a11aed2a1d323c0baafc3e6255f14db5a0a15f46;
            bstc=VOg2E1R2cJS2df86IPPAo8;
            exp-ck=6V3flk7Xi3l1AN-0L3DwTRU1GpBCe1HbOxV1Jeavw1MZ9tt1NCuxi1Oqgc14X92ox4YJsua5a4vv41dykD11fHfTr2fJumS3lZnE76rwaVg4sGGbM4wx8xe1yI7_k1;
            seqnum=45;
            vtc=Uc-JTxE6pVGBW2hnCjcs5c;
            xpa=2lwWQ|63K3S|6V3fl|7Xi3l|AN-0L|DViIf|DwTRU|GpBCe|HbOxV|Jeavw|LVSOt|MBc1l|MZ9tt|NCuxi|NOaJP|Oqgc1|Q0IHr|X92ox|YJsua|_vY-K|a4vv4|dykD1|fHfTr|fJumS|hcz5Y|jeBOs|lZnE7|mOlOu|rwaVg|sGGbM|sw6qx|wx8xe|yI7_k;
            xpm=1%2B1607533878%2BUc-JTxE6pVGBW2hnCjcs5c~%2B0;
            TS0196c61b=01538efd7cd89e4757c46548b15a03e6fb5f3bd1b0eceec8a9cc713cae53b2008d5271d3288687652d7dd5da298b323b88774b4cc5;
            akavpau_ca_prod_akamai_vp=1607536864~id=7d5345f705bb2bf14704b35747eb2a65;
            cto_bundle=Kkah1V9zRW0lMkJ6Tk01U3d0WjhJJTJCU3dtRW8xWWt1TWQ3RnVGaFhnZXozbFZlSFloVnEwaSUyQlc2VEV1ajFsUFoxSThOcmZKJTJGVWVqVWRqRXZqbXYzVExrY1hQbUJ0dXZRNiUyQnQyUjhCZXpSaUxla3QyQjYwb2JQMHdOc2ZNZ2RRZzF2WCUyRjkwTw;
            __gads=ID=bfd93a399836fb58-2226ab447ab80028:T=1607463171:RT=1607536534:S=ALNI_MYHS0pD0Db6IpslZy-FR_pkg8mBhw;
            s_ecid=MCMID%7C67974126428989854003572490284746605627;
            s_vi=[CS]v1|2FE7F8818515EEBA-400007B7A3D1B3DD[CE];
            s_visit=1; _fbp=fb.1.1607463168492.673750476;
            _gcl_au=1.1.1429677599.1607463169;
            _ga=GA1.2.630256747.1607463167;
            _gid=GA1.2.833863016.1607463167;
            s_cc=true; NEXT_GEN.ENABLED=1;
            WM.USER_STATE=GUEST|Guest;
            authDuration={"lat":"1607536532040000","lt":"1607536532040000"};
            cartId=d34a3641-d1c9-4dda-9bcd-e9c5f5eb8526;
            headerType=grocery;
            _px3=4abab83ed159a3e7156902a46640c350c0693684b451b9e1549d68c1a43b6184:w5CDybzTn7pdmQc2Zl0K0BYG1jdi1B7wZ9UoqI6M43sqgpzF9y3WuWGjZEjyqouQGZ0XUoYgKxl4kd589wLriA==:1000:FpGVwKtpI8+sJKW+yltOdtihLEyCv1Yq6N08iMOcLlx/Dn1UO+bXedFKPlMSfhW+vb+GEqzcRNChuDqeMna0DUlxY283Q9nb0gzFurmhY9MprjFqLenFXaBsIj4RZgouLnkNAxHJUvfYPxw5ot8BPHtLngGzJxiGbLPZzbE6Byw=;
            AMCV_C4C6370453309C960A490D44%40AdobeOrg=359503849%7CMCIDTS%7C18605%7CMCMID%7C67974126428989854003572490284746605627%7CMCAID%7C2FE7F8818515EEBA-400007B7A3D1B3DD%7CMCOPTOUT-1607542707s%7CNONE%7CMCAAMLH-1608140307%7C4%7CMCAAMB-1608140307%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18612%7CvVersion%7C5.0.1;
            _pin_unauth=dWlkPVkyRTNZVEpoTVRNdFlqQTJPUzAwWldSakxXSmtNell0WkRWbU1EbGpZamxqWVdVeQ;
            og_autoship=0;
            _uetsid=eeebf9a0399c11eba6d24d6e8ef1bbd8;
            _uetvid=eeec28e0399c11eb8eaa6d619d095b32;
            _4c_mc_=74ed1c9c-373d-4520-97f5-40501e3ff0cc;
            walmart.locale=en;
            dtLatC=60;
            previousBreakpoint=desktop;
            usrState=1;
            wmt.breakpoint=d;
            TS011fb5f6=0130aff232e0124c807e45d28963bb987f3a7223834733392143aad7dc9744a8f575f4d39f129dd6b8a248121ff60f6f962929d83a;
            TS0175e29f=0130aff232e0124c807e45d28963bb987f3a7223834733392143aad7dc9744a8f575f4d39f129dd6b8a248121ff60f6f962929d83a;
            TS01f4281b=0130aff232e0124c807e45d28963bb987f3a7223834733392143aad7dc9744a8f575f4d39f129dd6b8a248121ff60f6f962929d83a;
            defaultNearestStoreId=3124;
            deliveryCatchment=3124;
            localStoreInfo=eyJwb3N0YWxDb2RlIjoiUDdCM1o3IiwibG9jYWxTdG9yZUlkIjoiMzEyNCIsInNlbGVjdGVkU3RvcmVJZCI6IjMxMjQiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IlRodW5kZXIgQmF5IFN1cGVyY2VudHJlIiwiZnVsZmlsbG1lbnRTdG9yZUlkIjoiMzEyNCIsImZ1bGZpbGxtZW50VHlwZSI6IklOU1RPUkVfUElDS1VQIn0=;
            walmart.nearestPostalCode=P7B3Z7;
            walmart.preferredstore=3124;
            walmart.shippingPostalCode=P7B3Z7;
            walmart.nearestLatLng="43.60822, -79.69387";
            DYN_USER_ID.ro=5ca84ad4-f199-49b4-8a0c-543a44b7e789;
            BVBRANDID=6610c764-83d6-4a95-bf86-0d86832372f5;
            BVImplmain_site=2036;
            cookiePolicy=false;
            DYN_USER_ID=5ca84ad4-f199-49b4-8a0c-543a44b7e789;
            LT=1607483357377;
            WM_SEC.AUTH_TOKEN=MTAyOTYyMDE419VE21z901+eCBke6kAqFXaY5fgs11z1RrSzrHVw1KEFF+PPZEJ7X2N/yA6v1jPI6xqG4HfJAxmTO9ZC0baNpdFRAJDRiib/NilyxQEdflRc2oCqyXD+Rlub3NXn8otUj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj1Yy1xK8u1ktSlILSxYB5RydR0oSicd8E7RJYYL+Y11PH0io5FWN2P7mWjfETzP0z7b/SoGFgAYL9DGZ8K45WCXb/Ew67/GsLtdlJHpe1JgED7ACF7QTzL/qgSxzrYRB5K7C5ZAKn0VBvKN+J/mYo2Pm64seCgGZHEY1XiZIHfr7CI2ljQKnXXrPQbGONUGGWF/IIE/FkoQBiqMngyju62UUMfDjQelA2l8kWU2EKohBg==
            _scid=02b83c2f-5f3c-4c53-91b9-a4bf0b01154b;
            _pxvid=ef4ab4ff-399c-11eb-a3c0-0242ac120019;
            og_session_id=af0a84f8847311e3b233bc764e1107f2.630922.1607463175;
            og_session_id_conf=af0a84f8847311e3b233bc764e1107f2.630922.1607463175;
            AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1;
            TBV=13;
            walmart.id=d22f36f3-8625-4f0b-f0bc-ef7901310c6f;
            dtCookie=-21$8EKMQADVOB5NJ4KG5TBIKH79L6TRTTB4;
            wmt.c=0;
            userSegment=40-percent;
            walmart.csrf=5756fe2c9c347364ae459d79'''
        }
        for url in productUrls:
            newHeader = header
            newHeader['Cookie'] = newCookie
            yield scrapy.Request(url=self.baseUrl+url, callback=self.parseProductDetail,
                                 meta={'branch': branch, 'category': category}, headers=newHeader)
            break

        # send as cookie:
    def parseProductDetail(self, response):
        print('QUIIIIIII')
        print(response.text)

        # store = scrapy.Field() x
        # barcodes = scrapy.Field() x
        # sku = scrapy.Field() x
        # brand = scrapy.Field() x
        # name = scrapy.Field() x
        # description = scrapy.Field() x
        # package = scrapy.Field()x
        # image_url = scrapy.Field() x
        # category = scrapy.Field() ok
        # url = scrapy.Field() ok
        # branch = scrapy.Field() ok
        # stock = scrapy.Field()
        # price = scrapy.Field() x
