from hashlib import sha1
from time import time
import base64
import urllib2, urllib
import json
import hmac
import json

"""
author: Evan Duffield <eduffield@iacquire.com>

Thank you to iAcquire for sponsoring development of this module.
"""

follower_wonk_access_id = ""
follower_wonk_secret_key = ""

class FollowerWonk(object):
    @staticmethod
    def social_authority(username):
        uri = 'https://api.followerwonk.com/social-authority'

        datime = int(time() + 500)

        s = hmac.new(follower_wonk_secret_key, "%s\n%s" % (follower_wonk_access_id, datime), sha1).digest()
        b64  = base64.b64encode(s)
        signature = urllib.quote_plus(b64)

        auth = "AccessID=%s;Timestamp=%s;Signature=%s;" % (follower_wonk_access_id, datime, signature)

        req = urllib2.Request("%s?screen_name=%s;%s" % (uri, username, auth))
        r = urllib2.urlopen(req)

        response = json.loads( r.read());

        r.close()

        if '_embedded' not in response:
            return -1

        return response['_embedded'][0]['social_authority']

assert FollowerWonk.social_authority("randfish") > 0
assert FollowerWonk.social_authority("usernamedoesnotexist123") == -1