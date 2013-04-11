Social-Authority-SDK
====================

Social Authority helps you find, optimize, and engage your Twitter audience. It's a 1 to 100 point scale that measures a user's influential content on Twitter.
More than just another self-focused metric, Social Authority helps you discover other influential tweeters with high engagement.

* [Code Examples](https://github.com/seomoz/Social-Authority-SDK/tree/master/code-examples)
* [Language Libraries](https://github.com/seomoz/Social-Authority-SDK/tree/master/client-libraries)

## Getting Started with the Social Authority API

The Social Authority API gives access to a select piece of the Follwerwonk infrastructure. It uses standard HTTP Verbs and Hypermedia documents to make exploring and learning as easy as possible. This guide will use curl for all our examples, you're welcome to translate them into whatever language you prefer.

### A Quick Note about the Response Data Format

By default, the Social Authority API uses [Hypertext Application Language](http://stateless.co/hal_specification.html) for the JSON serialization format. This means we can (and do!) embed Hypermedia Controls into the documents. Every response from the API has a key (`_links`) pointing to more information. Simply generate requests for those URLs to obtain the additional information. This is useful when you exceed the limits for scores returned in a single request. The server will automatically generate the URLs needed for subsequent requests to obtain the remaining data.

### Setting up Access Controls

The Followerwonk Social Authority API uses the Mozscape API Access Controls system. You'll need to do to gain access but the first step is to create a Mozscape API account and fetch your AccessID and SecretKey.

You can do this by following the directions at [The Mozscape API keys page](https://www.seomoz.org/api/keys).

Once you have your API keys you will need to add them to Followerwonk's AccessControl registry. This is temporary while we're still in limited beta and hopefully when we launch this integration will be seamless.

To add them to Followerwonk's AccessControl registry simply post them. Here is an example:

    curl -v -XPOST -H'Content-Type: application/json' https://api.followerwonk.com/access-control -d '{ "AccessID":"ACCESS_ID", "SecretKey":"SECRET_KEY"}' 

A 201 CREATED response will contain a Location header giving the URI of the new AccessControl credentials you just registered. Querying that location will let you check your current access rate limits.

    curl -v https://api.followerwonk.com/access-control/ACCESS_ID

        {
             "_links" : {
                "create" : {
                   "href" : "/token"
                },
                "self" : {
                   "href" : "/access-control/ACCESS_ID"
                }
             },
             "throttle" : "1",
             "hourly" : "100",
             "daily" : "800"
        }

### Querying the Social Authority API

Now that you have an AccessID registered, to query the Social Authority API you will need to make a call to the Social Authority Resource. The Social Authority Resource takes a list of screen names or user ids and returns Social Authority scores for all of the accounts it can find. Currently we limit the number of screen names and user ids in a single request to 100 combined.

You will need to perform a signed request as described in [The Mozscape API wiki](http://apiwiki.seomoz.org/signed-authentication).

    curl -v https://api.followerwonk.com/social-authority?screen_name=randfish;AccessID=ACCESS_ID;Expires=TIMESTAMP;Signature=SIGNATURE_HMAC

You'll get back a JSON packet with the the Social Authority score and some metrics.
 
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

### Klout v1 Compatible API

There is also a Klout v1 Compatible API. You'll need to make requests using an Accept-Content header set to `application/klout+json`. This still requires a signed request as documented at [The Mozscape API wiki](http://apiwiki.seomoz.org/signed-authentication).

    curl -v 'https://api.followerwonk.com/social-authority?screen_name=randfish;AccessID=ACCESS_ID;Expires=TIMESTAMP;Signature=SIGNATURE_HMAC' -H'Accept: application/klout+json'

This will return Klout compatible JSON.

        {
           "status" : 200,
           "users" : [
              {
                 "twitter_screen_name" : "randfish",
                 "kscore" : "54.90157176971435"
              }
           ]
        }

The Klout Compatible API is provided for easy transition. It is limited in what information it can provide going forward and the native API is recommended for *new* code.
