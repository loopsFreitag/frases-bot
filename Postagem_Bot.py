import facebook
from Frases_Bot import frase

token = 'Token do Facebook'
fb = facebook.GraphAPI(access_token=token)
fb.put_object(parent_object='me', connection_name='feed',message=frase())
