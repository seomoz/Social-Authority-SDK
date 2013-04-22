# Anatomy of a Social Authority API Call

Every request to the Social Authority API follows the same basic format: 

    http://api.followerwonk.com/social-authority?{screen_name};{user_id};{AccessID};{Timestamp};{Signature}

Here's what each of these parts of this request do:

* `http://api.followerwonk.com`	
Access the API by calling the hostname of the service `api.followerwonk.com` and the Resource you’re making the request to `/social-authority`.

* {screen_name} & {user_id}
These are query parameters for which accounts you want to look up Social Authority scores for. You can provide either a Twitter screen name, `screen_name=peterbray` or a Twitter user id, `user_id=24496399` or both. You can provide multiple of either by separating the IDs with commas, `screen_name=peterbray,randfish,aplusk`.

* {AccessID}, {Timestamp} & {Signature}
These are query parameters that provide your credentials. For example:

    `AccessID=member-MDczMjM1NGUtN2Y3Ny01OGI0LThkOGUtYzhlYWVlYjcxMTZk;Timestamp=1225138898;Signature=LmXYcPqc%2BkapNKzHzYz2BI4SXfC%3D`

## Signed Authentication

To use signed authentication, append the following three query string parameters:

The AccessID parameter identifies the client in question. The value of this parameter must be your access ID, obtained when you generate yourAPI credentials.
The Expires parameter is a Unix timestamp that indicates for how long this request is valid. This should be a time in the future, usually no more than several minutes later than the moment your client code initiates the transfer. Values that expire excessively far in the future will not be honored by the Mozscape API. Authentication timestamps must be in UTC in order to work properly.
The Signature parameter is an HMAC-SHA1 hash of your Access ID (as it appears in the AccessID parameter), followed by a new line, followed by the Expires parameter, using your Secret Key. This hash must be base64 and URL-encoded before being placed in the request query string.
Once combined, a valid query string should look like the following:

`AccessID=member-MDczMjM1NGUtN2Y3Ny01OGI0LThkOGUtYzhlYWVlYjcxMTZk;Timestamp=1225138899;Signature=LmXYcPqc%2BkapNKzHzYz2BI4SXfC%3D`

For example, the example request above should compute the HMAC-SHA1 of the following two lines (including a single linefeed character between the AccessID and the timestamp, and ignoring any whitespace below):

`member-MDczMjM1NGUtN2Y3Ny01OGI0LThkOGUtYzhlYWVlYjcxMTZk <newline> 1225138899`

Once the HMAC-SHA1 of this string is created, the binary form must be base64 encoded. The result of the base64 encoding must be URL-encoded. This method of authentication is complicated, but you can find helpful examples in several languages in our Sample Code.

## ? and ;

These little characters are important, so don’t miss them. The ? separates the main URL from the query parameters, and the ; goes between multiple parameters. You’ll see the ; used in the example for authentication, which is just 3 parameters required by the service.
All of these elements together give you a valid request:

    http://api.followerwonk.com/social-authority?screen_name=randfish;AccessID=member-MDczMjM1NGUtN2Y3Ny01OGI0LThkOGUtYzhlYWVlYjcxMTZk;Timestamp=1225138898;Signature=LmXYcPqc%2BkapNKzHzYz2BI4SXfC%3D

## Creating Valid Requests in Code
While you can enter a valid request in your browser for quick queries, if you’re doing a lot of work with the service, you’ll want to create a program that generates the requests for you. To get started, see our sample code and applications.
