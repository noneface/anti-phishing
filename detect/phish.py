# -*- coding: utf-8 -*-

import requests
import json
import time
import base64
import hashlib


class PhishTank(object):

    """
        search url in PhishTank
        verified the url 

        self.phishes values:
                Unknown   (default)
                not phish 
                phish
    """

    def __init__(self, key):
        self.key = key

    def verified(self, url):
        # reference : https://www.phishtank.com/api_info.php

        requestURL = "http://checkurl.phishtank.com/checkurl/"
        parameter = {
            "url": url,
            "format": "json",
            "app_key": self.key
        }

        try:
            res = requests.post(requestURL, data=parameter)
            result = json.loads(res.content)
            self.result = result
        except Exception, e:
            print "Error"
            raise e

    def parse(self):
        
        """
            response will look like:
                {
                "meta":
                    {
                        "timestamp":"2016-09-13T09:50:28+00:00",
                        "serverid":"32963dad",
                        "status":"success",
                        "requestid":"146.112.225.22.57d7cbe4216703.90533009"
                    },
                "results":
                    {
                        "url":"http:\/\/www.vieabcps.com\/pe.php",
                        "in_database":true,
                        "phish_id":"4451648",
                        "phish_detail_page":"http:\/\/www.phishtank.com\/phish_detail.php?phish_id=4451648",
                        "verified":true,
                        "verified_at":"2016-09-12T22:01:32+00:00",
                        "valid":true
                    }
    
                }
        """

        result = self.result['results']
        try:
            if result['in_database'] == False:
                self.phishes = "Unknown"
            else:
                self.phishes = "phish"
        except Exception, e:
            raise e

    def test(self):
        self.verified("http://www.vieabcps.com/pe.php")
        self.parse()
        print self.phishes


class jinshan(object):

    """
        jinshan api for phish 

        self.phishes values:
                Unknown   (default)
                not phish 
                phish

    """

    def __init__(self, key, secret):

        self.appkey = key
        self.secret = secret   
        self.signatureString = "/phish/?appkey=%s&q=%s&timestamp=%s"
        self.phishes = "Unknown"

    def verified(self, url):
        requestURL = "http://open.pc120.com/phish/"

        q = base64.b64encode(url)[:-1]
        timestamp = str(time.time())

        sign = self.signatureString % (self.appkey, q, timestamp)

        m = hashlib.md5()
        m.update(sign+self.secret)
        sign = m.hexdigest()     # signature string
        # reference http://code.ijinshan.com/api/devmore4.html#md3

        parameter = {
            "q": q,
            "appkey": self.appkey,
            "timestamp": timestamp,
            "sign": sign
        }

        try:
            res = requests.get(requestURL, params=parameter)
            self.result = json.loads(res.content)
        except Exception, e:
            print "Request Error"
            raise e

    def parse(self):

        """
            respones will look like:
                1.  {"success": 1, "phish":$phish}    1 for success
                2.  {"success": 0, "errno": $errno, "msg": $msg}   0 for error
        """

        result = self.result
        try:
            if result['success'] == 0:
                self.phishes = False
            else:
                if result['phish'] == -1:   
                    self.phishes = "Unknown"
                elif result['phish'] == 0:
                    self.phishes = "not phish"
                else:
                    self.phishes = "phish"
        except Exception, e:
            print "Parse Error"
            raise e

    def test(self):

        self.verified("http://www.vieabcps.com/pe.php")
        self.parse()
        print self.phishes


class Google(object):

    """
        Google api for browser safe
        
        self.phishes values:
            Unknown   (default)
            not phish 
            phish
    """

    def __init__(self, key):
        self.key = key

    def verified(self,url):
        requestURL = "https://safebrowsing.googleapis.com/v4/threatMatches:find?key=%s"

        header = {
                "content-type": "json"
        }

        requestURL = requestURL % self.key

        data = {
            "client": {
              "clientId":      "phishing",
              "clientVersion": "1.333333"
            },
            "threatInfo": {
              "threatTypes":      ["SOCIAL_ENGINEERING"],  # for social engineering test
              "platformTypes":    ["WINDOWS"],
              "threatEntryTypes": ["URL"],
              "threatEntries": [
                {"url": url},
              ]
            }
          }

        data = json.dumps(data)

        try:
            res = requests.post(requestURL, headers=header,data=data)
            self.result = json.loads(res.content)
            print self.result
        except Exception, e:
            raise e

    def parse(self):

        """
            response will look like:
                {
                    u'matches': 
                        [
                            {
                                u'threatType': u'SOCIAL_ENGINEERING', 
                                u'threatEntryType': u'URL', 
                                u'platformType': u'WINDOWS', 
                                u'threat': {u'url': u'http://www.vieabcps.com/pe.php'}, 
                                u'cacheDuration': u'300.000s'
                            }
                        ]
                }

        """

        result = self.result

        try:
            if len(result) == 0:
                self.phishes = "Unknown"
            else:
                matches = result['matches'][0]
                if matches["threatType"] == "SOCIAL_ENGINEERING":
                    self.phishes = "phish"
                else:
                    self.phishes = "Unknown"
        except Exception, e:
            raise e

    def test(self):
        self.verified("http://www.vieabcps.com/pe.php")
        self.parse()
        print self.phishes