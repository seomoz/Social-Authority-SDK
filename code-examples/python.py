"""
author: Evan Duffield <eduffield@iacquire.com>
Thank you to iAcquire for sponsoring development of this module.

Updated by Bryan Minor, Ph.D.
--> Now works for Python 3
Supported by envision.ai
"""

# External libraries
from hashlib import sha1
from time import time
import base64
import urllib.request
import urllib.parse
import urllib.error
import json
import hmac

#Initializations
follower_wonk_access_id_str = "your-access-id"
follower_wonk_secret_key_str = "your-secret key"

#Class for access FollowerWonk API
class FollowerWonk(object):
    @staticmethod
    def social_authority(username):
        uri = 'https://api.followerwonk.com/social-authority'

        datime = int(time() + 500)


        #Add BMM: Trying to binary format correct
        keyBin = bytes(follower_wonk_secret_key_str, 'UTF-8')
        messageStr = "%s\n%s" % (follower_wonk_access_id_str, datime)
        messageBin = bytes(messageStr, 'UTF-8')


        s = hmac.new(keyBin, messageBin, sha1).digest()
        b64 = base64.b64encode(s)
        signature = urllib.parse.quote_plus(b64)

        auth = "AccessID=%s;Timestamp=%s;Signature=%s;" % (follower_wonk_access_id_str, datime, signature)

        req = urllib.request.Request("%s?screen_name=%s;%s" % (uri, username, auth))
        r = urllib.request.urlopen(req)

        responseStr = r.read().decode("utf-8")
        #print("responseStr = ", responseStr)
        response_Json = json.loads(responseStr)

        #print("response_Json = ", response_Json)

        r.close()

        if '_embedded' not in response_Json:
            return -1

        return float(response_Json['_embedded'][0]['social_authority'])
        #return response_Json

assert FollowerWonk.social_authority("bryanminorphd") > 0
assert FollowerWonk.social_authority("UserNameDoesNotExist123") == -1

#Test cases
FollowerWonk.social_authority("bryanminorphd")

FollowerWonk.social_authority("envision_ai")

FollowerWonk.social_authority("google")


