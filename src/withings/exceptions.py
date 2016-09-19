# -*- coding: utf-8 -*-


class WithingsError(Exception):
    STATUS_CODES = {
        # Response status codes as defined in documentation
        # http://oauth.withings.com/api/doc
        0: "Operation was successful",
        247: "The userid provided is absent, or incorrect",
        250: "The provided userid and/or Oauth credentials do not match",
        286: "No such subscription was found",
        293: "The callback URL is either absent or incorrect",
        294: "No such subscription could be deleted",
        304: "The comment is either absent or incorrect",
        305: "Too many notifications are already set",
        342: "The signature (using Oauth) is invalid",
        343: "Wrong Notification Callback Url don't exist",
        601: "Too Many Request",
        2554: "Wrong action or wrong webservice",
        2555: "An unknown error occurred",
        2556: "Service is not defined",
    }

    def __init__(self, status):
        exc = '{0}: {1}'.format(status, self.STATUS_CODES[status])
        super(WithingsError, self).__init__(exc)
        self.status = status
