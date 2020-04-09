* Errors
  * [BadStatus](#badstatus)
  * [NotFound](#notfound)
  * [BadRequest](#badrequest)
  * [ErrorMessage](#errormessage)
***
# BadStatus

## Properties
* Inherited by Exception

## Error

If the request has failed, and has gone through NotFound, BadRequest, and ErrorMessage, this will error and give you the status code, url, and data.

# NotFound

## Properties
* Inherited by Exception

## Error

If the request's status code is 404, this will error and give you the status code, url, and data.

# BadRequest

## Properties
* Inherited by Exception

## Error

If the request's status code is 400, this will error and give you the status code, url, and data.

# ErrorMessage

## Properties
* Inherited by Exception

## Error

If the request has an existing error message, this will error and give you the error message and data.