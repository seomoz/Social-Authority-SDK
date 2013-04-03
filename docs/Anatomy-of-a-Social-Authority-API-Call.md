---
title: Anatomy of a Social Authority API Call
layout: default
---
# Anatomy of a Social Authority API Call

Every request to the Social Authority API follows the same basic format: 

http://api.followerwonk.com/social-authority?{screen_name};{user_id};{AccessID};{Expires};{Signature}

Here’s what each of these parts of this request do:

* `http://api.followerwonk.com`	
Access the API by calling the hostname of the service `api.followerwonk.com` and the Resource you’re making the request to `/social-authority`.

* {screen_name} & {user_id}
These are query parameters for which accounts you want to look up Social Authority scores for. You can provide either a Twitter screen name, `screen_name=peterbray` or a Twitter user id, `user_id=24496399` or both. You can provide multiple of either by separating the IDs with commas, `screen_name=peterbray,randfish,aplusk`.

* {AccessID}, {Expires} & {Signature}
These are query parameters that provide your credentials. For example:
AccessID=NKzHzYz2BI4SXf&Expires=1225138898&Signature=LmXYcPqc%2BkapNKzHzYz2BI4SXfC%3D
For more on how to authenticate your API requests, see [Signed Authentication](http://apiwiki.seomoz.org/signed-authentication).

## ? and ;

These little characters are important, so don’t miss them. The ? separates the main URL from the query parameters, and the ; goes between multiple parameters. You’ll see the ; used in the example for authentication, which is just 3 parameters required by the service.
All of these elements together give you a valid request:

`http://api.followerwonk.com/social-authority?screen_name=randfish;AccessID=NKzHzYz2BI4SXf;Expires=1225138898;Signature=LmXYcPqc%2BkapNKzHzYz2BI4SXfC%3D`

## Creating Valid Requests in Code
While you can enter a valid request in your browser for quick queries, if you’re doing a lot of work with the service, you’ll want to create a program that generates the requests for you. To get started, see our [sample code] and applications.
