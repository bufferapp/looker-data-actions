# Looker Data Actions

Set of [Looker Data Actions](https://discourse.looker.com/t/data-actions/3573)
to perform tasks in other tools from directly within Looker.

#### What are Data Actions?
Data Actions allow users to perform tasks in other tools from directly within
Looker using API calls. The action is set up in LookML on a particular field
and can trigger an API call.

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

### Prerequisites

To run this Looker Data Actions service you'll need Docker and this variables in
your environment:

- `LOOKER_DATA_ACTIONS_TOKEN`: Token to perform authentication from Looker.
  This value will be placed in the LookML
- `SENDGRID_API_KEY`: Value for the [API key](https://app.sendgrid.com/settings/api_keys) you want to use for Sendgrid

### Running Looker Data Actions Service

Ensure that Docker is running locally and place the environment variables under
an `.env` file. You can now run `make build && make` to create the server in
port 5000.

Once the service is up you can test it with this snippet (_remember to replace
the token with the one you placed in the env file_):

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
