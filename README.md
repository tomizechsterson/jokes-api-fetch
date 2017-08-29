# jokes-api-fetch

This should be called with version 3+ of Python

## Examples

#### Show Id
If you want to show the joke id with the output. Useful for providing feedback

`python3 callJokesApi.py -id`

#### Change First Name
If you want to change the first name of the returned person from 'Chuck'

`python3 callJokesApi.py -f example`

#### Change Last Name
To change the last name of the returned person from 'Norris'

`python3 callJokesApi.py -l example`

#### Change Full Name
You can also change both at the same time

`python3 callJokesApi.py -f Nicholas -l Cage`

#### Include Certain Categories
You can choose between 'nerdy' and 'explicit' to include. Currently, these are the only two categories that I'm aware of. 

`python3 callJokesApi.py -i nerdy`

or you can specify both by using the same parameter twice

`python3 callJokesApi.py -i nerdy -i explicit`

#### Exclude Categories
You can also exclude categories in exactly the same way as with including, except you need to use the `-e` parameter

`python3 callJokesApi.py -e nerdy`

or

`python3 callJokesApi.py -e nerdy -e explicit`