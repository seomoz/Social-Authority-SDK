# API Response Codes

## 200 OK

Your request has completed successfully. The Request body will contain the data you were looking for.

## 201 CREATED

Creating the resource was successful. There will be a Location header pointing to the newly created Resource.

## 401 AUTHORIZATION REQUIRED

You need to supply authentication credentials. See the [[Anatomy of a Social Authority API Call]] for more information on how to make a valid request.

## 403 FORBIDDEN

The authentication credentials you supplied weren't valid. You'll need to check that you are using the right credentials and supply the appropriate ones. 

## 404 NOT FOUND

The server couldn't find the data you were looking for. Possibly it was removed (either by twitter, or by another request).

## 420 CALM DOWN

You're requests are coming in too quickly and have triggered throttle controls. Please slow down your requests to under the throttle limits.

## 429 LIMITS EXCEEDED

You've made too many requests for the current time period (hour or day). Please wait until your throttle limits have reset (when the current period ends) and try again.
