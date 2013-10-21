Social Authority API
====================

Social Authority helps you find, optimize, and engage your Twitter audience. It's a 1 to 100 point scale that measures a user's influential content on Twitter.

More than just another self-focused metric, Social Authority helps you discover other influential tweeters with high engagement. Read more about it on the [Moz Social Authority site](https://followerwonk.com/social-authority).

* [Code samples](https://github.com/seomoz/Social-Authority-SDK/tree/master/code-examples) can help you get started with the Social Authority API.
* [Client libraries](https://github.com/seomoz/Social-Authority-SDK/tree/master/client-libraries) can help you develop your own applications.

This guide uses `curl` for examples; you're welcome to use the tools and languages of your choice.

The Social Authority API uses [standard HTTP methods](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html) and hypermedia documents to make exploring and learning as easy as possible.

## Getting Started with the Social Authority API

### Get Your Access Credentials

To access the Social Authority API:

1. Log into your Twitter account.
2. Log into Followerwonk.
3. Go to the [Social Authority](https://followerwonk.com/social-authority) page and click on "get access credentials".

Follow the instructions on the web page to receive an Access ID and a Secret Key.

### A Quick Note about the Response Data Format

The Social Authority API uses [Hypertext Application Language](http://stateless.co/hal_specification.html) for its JSON serialization format. This means we can (and do!) embed Hypermedia Controls in documents the Social Authority API returns. 

When you exceed the limits for scores returned in a single request, the server automatically generates URLs (`_links`) for subsequent requests to obtain the remaining data.

### Querying the Social Authority API

[Anatomy of a Social Authority Call](/docs/Anatomy-of-a-Social-Authority-API-Call.md) describes how to make Social Authority API requests.

Here is an example of an API request:

    curl -v https://api.followerwonk.com/social-authority?screen_name=randfish;AccessID=member-MDczMjM1NGUtN2Y3Ny01OGI0LThkOGUtYzhlYWVlYjcxMTZk;Timestamp=1225138898;Signature=LmXYcPqc%2BkapNKzHzYz2BI4SXfC%3D

The Social Authority API returns Social Authority scores and metrics in a JSON-formatted packet. For example:
 
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

### Request Limits

The default request limits are:

        25 IDs per request
         5 Requests Per Second (ie concurrently)
      5000 requests per hour
    20,000 requests per day

The Social Authority API counts both screen names and user IDs toward the limit of 25 IDs per request.

## Attribution and Licensing

By using the Social Authority API, you agree to our [Terms of Use and Privacy Policy](http://moz.com/terms-privacy) as well as the restrictions contained on this page. You do not have to be a paying PRO member to use the Social Authority API. Access to the Social Authority API may be suspended or terminated at any time and for any reason, with or without cause. If your access is cancelled, you are not entitled to a refund of any kind. Moz may discontinue providing service at any time and for any reason. Data must follow all attribution and branding requirements.

## Help 

Problems? Concerns? Questions? Join the [Moz Support Forums](https://seomoz.zendesk.com/categories/6328-SEOmoz-APIs-and-Extras)! You can ask questions and get answers, interact with the support team and other API users, and request features for future releases.

