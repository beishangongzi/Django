from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

## login_required

`from django.contrib.auth.decorators import login_requierd`

if the user isn't logged in, redirect to settings.LOGIN_URL, passing the current 
absolute path in the query string. Example: `/accounts/login/?next=/polls/3/`

## csrf_exempt

`from django.views.decorators.csrf import csrf_exempt`

This decorator marks a view as being exempt from the protection 
ensured by the middle.

## require_POST()

`from django.views.decorators.http import require_POST`

Decorator to require that a view only accepts the POST method.

