

def ParseHtml(self, html):
        soup = BeautifulSoup(html)
        links = soup.findAll('a', attrs={'class': 'ulink'})
        #print len(links)
        if len(links) == 0:  # the js return
            # tmp_js = soup.find(name='script', attrs={'language': 'javascript'})
            js_str = soup.script.string  # two ways to get the <script></script>
            new_url = js_str[16:-1]  # get the new url
            new_url = eval(new_url)  # eval:??????????
            self.ParseHtml(self.LoadPage(new_url))
        else:
            # print type(links)
            for link in links:
                # print type(link)
                # print type(link.string)
                # print unicode(link.string)
                # unicode(link.string))
                titles = re.findall(r'?(.+?)?', str(link.string))
                if len(titles) <> 0:
                    print titles[0]
                # print 'url is %s, title is %s.' %(link['href'], titles[0])
