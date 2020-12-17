import facebook
from Frases_Bot import frase

token = 'EAAJMRMT1VI4BAKgGwh7ttjmMQRJRsbXdsvbHTsr9JhIY3HAMKDCxgW8oZAoGh8HjOZCwfZBWtBlFwz5vfS7HFaEkh9hB6ZAAfr8nc8E3ghuTUxZBh0093VK0Lz0CSUqCdNUkF2FlDFITW0ZBfPiymXAICTjy5ZC8DFIxSmplsYj2gZDZD'
fb = facebook.GraphAPI(access_token=token)
fb.put_object(parent_object='me', connection_name='feed',message=frase())
