from unittest import TestCase
from app import app

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class ForexConverterTest(TestCase):
    def test_home_page(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Forex Converter</h1>', html)
    
    def test_currency_submit(self):
        with app.test_client() as client:
            res = client.post('/result', data={'convert_from':'USD','convert_to':'INR', 'amount':1})
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>The result is: ₹73.63</h1>',  html)
    
    def test_currency_submit_2(self):
        with app.test_client() as client:
            res = client.post('/result', data={'convert_from':'USD','convert_to':'THB', 'amount':1})         
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>The result is: ฿31.2</h1>', html)
    
    def test_redirection_followed(self):
        with app.test_client() as client:
            res = client.get('/', follow_redirects=True)
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Forex Converter</h1>', html)
        

