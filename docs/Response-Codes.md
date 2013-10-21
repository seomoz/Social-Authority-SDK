# API Response Codes

## 200 OK

Your request completed successfully. The Request body contains the data you searched for.

## 201 CREATED

The resource was successfully created. A Location header points to the newly created Resource.

## 401 AUTHORIZATION REQUIRED

Supply authentication credentials. See the [Anatomy of a Social Authority API Call](/Anatomy-of-a-Social-Authority-API-Call) for more information on how to make a valid request.

## 403 FORBIDDEN

The authentication credentials you supplied are invalid. Check that you are using the right credentials and try again.

## 404 NOT FOUND

The server cannot find the data you were looking for. It may have been removed, either by Twitter or by another request.

## 420 CALM DOWN

You have made too many requests and triggered throttle controls. Please slow down your requests to fall within throttle limits.

## 429 LIMITS EXCEEDED

You have made too many requests for the current time period (hour or day). Please wait until the current period ends and your throttle limits reset.
