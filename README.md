Social-Authority-SDK
====================

Social Authority helps you find, optimize, and engage your Twitter audience. It's a 1 to 100 point scale that measures a user's influential content on Twitter.
More than just another self-focused metric, Social Authority helps you discover other influential tweeters with high engagement. You can read more about it at [http://followerwonk.com/social-authority]()

* [Code Examples](https://github.com/seomoz/Social-Authority-SDK/tree/master/code-examples)
* [Language Libraries](https://github.com/seomoz/Social-Authority-SDK/tree/master/client-libraries)

## Getting Started with the Social Authority API

The Social Authority API gives access to a select piece of the Followerwonk infrastructure. It uses standard HTTP Verbs and Hypermedia documents to make exploring and learning as easy as possible. This guide will use curl for all our examples, you're welcome to translate them into whatever language you prefer.

### A Quick Note about the Response Data Format

By default, the Social Authority API uses [Hypertext Application Language](http://stateless.co/hal_specification.html) for the JSON serialization format. This means we can (and do!) embed Hypermedia Controls into the documents. Every response from the API has a key (`_links`) pointing to more information. Simply generate requests for those URLs to obtain the additional information. This is useful when you exceed the limits for scores returned in a single request. The server will automatically generate the URLs needed for subsequent requests to obtain the remaining data.

### Setting up Access Controls

The Followerwonk Social Authority API uses the an access control system. To gain access the first step is to create a fetch your Social Authority API AccessID and SecretKey.

You can do this by logging into your Followerwonk account and following the directions at [The Social Authority Page](https://followerwonk.com/social-authority).

### Querying the Social Authority API

Now that you have an AccessID registered, to query the Social Authority API you will need to make a call to the Social Authority Resource. The Social Authority Resource takes a list of screen names or user ids and returns Social Authority scores for all of the accounts it can find. Currently we limit the number of screen names and user ids in a single request to 100 combined.

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

Our Social Authority data is free to use. All we ask is that if you use it publicly, that you include an attribution to http://followerwonk.com/social-authority

## Help 

Problems? Concerns? Questions? [Contact us!](http://www.seomoz.org/help)

