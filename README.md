Social Authority SDK
====================

Followerwonk moved. The canonical version of this project is at [followerwonk/Social-Authority-SDK](https://github.com/followerwonk/Social-Authority-SDK).

Social Authority helps you find, optimize, and engage your Twitter audience. It's a 1 to 100 point scale that measures a user's influential content on Twitter.
More than just another self-focused metric, Social Authority helps you discover other influential tweeters with high engagement. You can read more about it at [https://followerwonk.com/social-authority](https://followerwonk.com/social-authority)

* [Code Examples](https://github.com/seomoz/Social-Authority-SDK/tree/master/code-examples)
* [Language Libraries](https://github.com/seomoz/Social-Authority-SDK/tree/master/client-libraries)

## Getting Started with the Social Authority API

The Social Authority API gives access to a select piece of the Followerwonk infrastructure. It uses standard HTTP Verbs and Hypermedia documents to make exploring and learning as easy as possible. This guide will use curl for all our examples, you're welcome to translate them into whatever language you prefer.

### A Quick Note about the Response Data Format

By default, the Social Authority API uses [Hypertext Application Language](http://stateless.co/hal_specification.html) for the JSON serialization format. This means we can (and do!) embed Hypermedia Controls into the documents. Every response from the API has a key (`_links`) pointing to more information. Simply generate requests for those URLs to obtain the additional information. This is useful when you exceed the limits for scores returned in a single request. The server will automatically generate the URLs needed for subsequent requests to obtain the remaining data.

### Setting up Access Controls

The Social Authority API uses an access control system. To gain access the first step is to fetch your Social Authority API AccessID and SecretKey.

You can do this by logging into Followerwonk and following the directions from the [Social Authority](https://followerwonk.com/social-authority) page there.

The current default freemium request limits are 250 SAs per day & 7500 SAs per month:

        25 IDs per request
         5 Requests Per Second (ie concurrently)
        10 requests per hour
        10 requests per day

Please contact us (help@moz.com) for paid subscription access for larger volumes.

### Querying the Social Authority API

Once you have an AccessID you can make a call to the Social Authority resource. The Social Authority resource takes a list of screen names or user ids and returns Social Authority scores for all of the accounts it can find. Currently we limit the number of screen names and user ids in a single request to 25 combined.

You will need to perform a signed request as described in [Anatomy of a Social Authority Call](https://github.com/seomoz/Social-Authority-SDK/blob/master/docs/Anatomy-of-a-Social-Authority-API-Call.md).

    curl -v https://api.followerwonk.com/social-authority?screen_name=randfish;AccessID=ACCESS_ID;Timestamp=TIMESTAMP;Signature=SIGNATURE_HMAC

You'll get back a JSON packet with the Social Authority score and some metrics.

        {
           "_embedded" : [
              {
                 "_links" : {
                    "self" : {
                       "href" : "/?user_id=6527972"
                    }
                 },
                 "user_id" : "6527972",
                 "social-authority" : "54.90157176971435",
                 "screen_name" : "randfish"
              }
           ],
           "_links" : {
              "search" : [
                 {
                    "templated" : "yes",
                    "href" : "/{?screen_name}",
                    "name" : "screen_name"
                 },
                 {
                    "templated" : "yes",
                    "href" : "/{?user_id}",
                    "name" : "user_id"
                 }
              ],
              "self" : {
                 "href" : "/social-authority?screen_name=randfish"
              }
           }
        }

## Attribution and Licensing

By using the Social Authority API, you agree to our [General Terms of Use](http://www.seomoz.org/users/terms), our [Privacy Policy](http://www.seomoz.org/pages/privacy) and the restrictions contained on this page. You do not have to be a paying member to use our API. Access to the Social Authority API may be suspended or terminated at any time and for any reason, with or without cause. If your access to the API is cancelled, you are not to be entitled to a refund of any kind. SEOmoz may discontinue providing service at any time and for any reason. We simply ask that if you re-use our data you give us attribution and follow our branding guidelines.

## Help

Problems? Concerns? Questions? [Contact us!](http://www.seomoz.org/help)

