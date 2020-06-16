# Okta Inline Hook Simple HTTP Endpoint Example

This example demonstrates how to setup a simple HTTP POST endpoint with Okta Took Inline Hook or similar [Inline Hook](https://developer.okta.com/docs/concepts/inline-hooks/).

## Use Cases

- Wrapping an existing internal or external endpoint/service.
- Integration with Okta Took Inline Hook. When a user authenticates using Okta, additional claims appended to the JSON Web Token either in Access Token and/or ID Token.

## Deploy

> NOTE: Serverless Framework cli needs to be [setup](https://www.serverless.com/framework/docs/).

In order to deploy the you endpoint simply run

```bash
serverless deploy
```

The expected result should be similar to:

```bash
Serverless: Packaging service...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading service .zip file to S3 (758 B)...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..........
Serverless: Stack update finished...

Service Information
service: aws-python-simple-http-endpoint
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  GET - https://f7r5srabr3.execute-api.us-east-1.amazonaws.com/dev/ping
functions:
  aws-python-simple-http-endpoint-dev-currentTime: arn:aws:lambda:us-east-1:377024778620:function:aws-python-simple-http-endpoint-dev-currentTime
```

## Okta Setup

- [Okta developer account](https://developer.okta.com/).
- Configure [Okta Inline Hook](https://developer.okta.com/docs/concepts/inline-hooks/)..
  - [Inline Hook Setup](https://developer.okta.com/docs/concepts/inline-hooks/#inline-hook-setup).
- OAuth2 / OpenID Connect application to Sign-On and demo.
  - TODO: Create custom attribute at the application level (eg. `extPatientId`)
  - TODO: Create new claim in Authorization Server.
  - TODO: Configure Access Policy to Inline Hook.

## Usage

> NOTE: Invoking via curl to validate.

```bash
curl --location --request POST 'https://swz5v5xuya.execute-api.us-east-1.amazonaws.com/dev/addclaim'
```

The expected result should be similar to:

```bash
{
  "commands": [
    {
    "type": "com.okta.identity.patch",
    "value": [
      {
          "op": "add",
          "path": "/claims/extPatientId",
          "value": "42"
      }
    ]
    }
  ],
  "debugContext": {
      "message": "hello world"
  }
}
```

## Inspiration

- [Simple HTTP Endpoint Example](https://github.com/serverless/examples/tree/master/aws-python-simple-http-endpoint)
