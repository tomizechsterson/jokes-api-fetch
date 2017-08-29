# Chuck Norris Joke Fetch Script

This should be called with version 3+ of Python

## Examples

### Show Id
If you want to show the joke id with the output. Useful for providing feedback

`python3 callJokesApi.py -id`

Sample output: `Fool me once, shame on you. Fool Chuck Norris once and he will roundhouse kick you in the face. (Joke Id: 35)`

### Change First Name
If you want to change the first name of the returned person from 'Chuck'

`python3 callJokesApi.py -f Example`

Sample output: `Example Norris never has to wax his skis because they're always slick with blood.`

### Change Last Name
To change the last name of the returned person from 'Norris'

`python3 callJokesApi.py -l Example`

Sample output: `Chuck Example doesn't daydream. He's too busy giving other people nightmares.`

### Change Full Name
You can also change both at the same time

`python3 callJokesApi.py -f Nicholas -l Cage`

Sample output: `Nicholas Cage is the reason why Waldo is hiding.`

### Include Categories
You can choose between 'nerdy' and 'explicit' to include. Currently, these are the only two categories that I'm aware of. 

`python3 callJokesApi.py -i nerdy`

or you can specify both by using the same parameter twice

`python3 callJokesApi.py -i nerdy -i explicit`

Sample output: `Chuck Norris's database has only one table, 'Kick', which he DROPs frequently.`

### Exclude Categories
You can also exclude categories in exactly the same way as with including, except you need to use the `-e` parameter

`python3 callJokesApi.py -e nerdy`

or

`python3 callJokesApi.py -e nerdy -e explicit`

Sample output: `Chuck Norris did not "lose" his virginity, he stalked it and then destroyed it with extreme prejudice.`