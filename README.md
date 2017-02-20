# Looker Data Actions

Set of Looker Data Actions to perform tasks in other tools from directly within
Looker.

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes. See deployment for notes on
how to deploy the project on a live system.

### Prerequisites

To run this Looker Data Actions service you'll need to add some variables to
your environment:

- `LOOKER_DATA_ACTIONS_TOKEN`: Token to perform authentication from Looker.
  This value will be placed in the LookML
- `SENDGRID_API_KEY`: Value for the [API key](https://app.sendgrid.com/settings/api_keys) you want to use for Sendgrid

### Running Looker Data Actions Service

If you're running Docker locally, place the environment variables under an
`.env` file and run `make build && make`. This will create the server in
port 5000.

You can go ahead and test it with this snippet (_remember to replace the token
with the one you placed in the env file_):

```bash
curl -X POST \
    -d '{"data": {"auth": "LOOKER_DATA_ACTIONS_TOKEN"}}' \
    -H "Content-type: application/json" \
    http://0.0.0.0:5000/ping
```

#### Email

To send emails from Looker you need to place the next snippet under an email
dimension:

```
dimension: user_email {
  action: {
    label: "Send Email"
    url: "https://urlofyourserver.com/email/{{value}}"
    param: {
      name: "auth"
      value: "LOOKER_DATA_ACTIONS_TOKEN"
    }
    form_param: {
      name: "subject"
      required: yes
    }
    form_param: {
      name: "body"
      type: textarea
      required: yes
    }
  }
  type: string
  sql: ${TABLE}.email ;;
}
```

## License

MIT © Buffer
