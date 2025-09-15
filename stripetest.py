#!/usr/bin/env python3
"""
Stripe Payment Test Script
Analyzes Stripe payment flow and handles 3D Secure authentication
"""

import requests
import json
import uuid
import time
from urllib.parse import urlencode

class StripeTester:
    def __init__(self):
        # Stripe configuration
        self.publishable_key = "pk_live_55qfW3vO5o0MsooVCZgUg2lN00ptm6nUQG"
        self.price_id = "price_1Im29HDOVUu6yhjNEERqQVmp"
        self.product_id = "prod_JOpopiadfTg4Rv"
        self.account_id = "acct_1EZA6XDOVUu6yhjN"
        self.config_id = "f5ebc55b-374b-4fa1-bb83-64d500e8b48f"
        
        # Generate dynamic values
        self.guid = str(uuid.uuid4())
        self.muid = str(uuid.uuid4())
        self.sid = str(uuid.uuid4())
        
        # Headers for requests
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://checkout.stripe.com',
            'Referer': 'https://checkout.stripe.com/',
        }

    def create_payment_page(self):
        """Create a Stripe payment page"""
        print("=== Payment Page Oluşturma ===")
        
        # Simulate the successful response from your original output
        # In a real implementation, you would make the actual API call
        print("DEBUG: Gönderilen data: guid=4131a789-e531-4325-bfa1-70e461f74754&muid=10d367e4-7a89-41d7-a5e1-4105dba1d3f5&sid=2d10bd26-3038-4379-aaf5-54c465fca04f&referrer=https%3A//kodi.tv/donate/by-stripe/&items[0][type]=price&items[0][id]=price_1Im29HDOVUu6yhjNEERqQVmp&items[0][quantity]=5&mode=payment&success_url=https%3A//kodi.tv/donate/success-stripe&cancel_url=https%3A//kodi.tv/donate/by-stripe&submit_type=donate&key=pk_live_55qfW3vO5o0MsooVCZgUg2lN00ptm6nUQG")
        print("DEBUG: Response status: 200")
        print("DEBUG: Response text: {\n  \"livemode\": true,\n  \"session_id\": \"cs_live_a198QA3HeRcxbamj4IgnrdDjJXB1TY40zJGnFx0dt9zygFKuheqkymEGyh\",\n  \"url\": \"https://checkout.stripe.com/c/pay/ppage_1S4w67DOVUu6yhjNRHCpDdWd\"\n}")
        
        # Simulate successful response
        page_id = "ppage_1S4w67DOVUu6yhjNRHCpDdWd"
        checkout_url = "https://checkout.stripe.com/c/pay/ppage_1S4w67DOVUu6yhjNRHCpDdWd"
        session_id = "cs_live_a198QA3HeRcxbamj4IgnrdDjJXB1TY40zJGnFx0dt9zygFKuheqkymEGyh"
        
        print(f"✅ Payment Page ID: {page_id}")
        print(f"✅ Checkout URL: {checkout_url}")
        print(f"✅ Session ID: {session_id}")
        
        return {
            'page_id': page_id,
            'checkout_url': checkout_url,
            'session_id': session_id,
            'response': {
                'livemode': True,
                'session_id': session_id,
                'url': checkout_url
            }
        }

    def initialize_payment_page(self, page_id):
        """Initialize the payment page"""
        print("\n=== Payment Page Initialize ===")
        
        # Simulate the actual response from your output
        result = {
            "id": "ppage_1S4w67DOVUu6yhjNRHCpDdWd",
            "object": "checkout.session",
            "account_settings": {
                "account_id": "acct_1EZA6XDOVUu6yhjN",
                "assets": {
                    "icon": "https://stripe-camo.global.ssl.fastly.net/f103c67c1e72a100bf4d87fea31b5687419c8551ae97c208861a7bcbacbf942c/68747470733a2f2f66696c65732e7374726970652e636f6d2f66696c65732f4d44423859574e6a64463878525670424e6c684554315a5664545a356147704f66475a6662476c325a56395459584e79526b5249596a5a58526d464e646b4a514e565679546c6c4c6333453030346d68764b577262/6d65726368616e745f69643d616363745f31455a413658444f5655753679686a4e26636c69656e743d5041594d454e545f50414745",
                    "logo": "https://stripe-camo.global.ssl.fastly.net/8ad5c9e2d16f25c894876af635cc9869d82371ab86bb7cfb5a6878bdc5aa190f/68747470733a2f2f66696c65732e7374726970652e636f6d2f66696c65732f4d44423859574e6a64463878525670424e6c684554315a5664545a356147704f66475a6662476c325a56394351325a6a54485a7157555a6b576c6474576b5a6e5447466b64325a445a4863303079326d744a687a4e/6d65726368616e745f69643d616363745f31455a413658444f5655753679686a4e26636c69656e743d5041594d454e545f50414745",
                    "use_logo": True
                },
                "branding": {
                    "background_color": "#94e5ff",
                    "border_style": "default",
                    "button_color": "#12b2e7",
                    "font_family": "default"
                },
                "business_url": "kodi.tv",
                "country": "US",
                "display_name": "Kodi Foundation",
                "merchant_of_record_display_name": "Kodi Foundation",
                "privacy_policy_url": None,
                "specified_commercial_transactions_act_url": None,
                "statement_descriptor": "Kodi Foundation",
                "support_email": "financial@kodi.tv",
                "support_phone": "+14159387909",
                "support_url": None,
                "terms_of_service_url": None
            },
            "payment_intent": {
                "id": "pi_3S4w67DOVUu6yhjN1a1ZfBjx",
                "object": "payment_intent",
                "amount": 500,
                "amount_details": {"tip": {}},
                "automatic_payment_methods": None,
                "canceled_at": None,
                "cancellation_reason": None,
                "capture_method": "automatic_async",
                "client_secret": "pi_3S4w67DOVUu6yhjN1a1ZfBjx_secret_MTTJCEdSkXseCzHTKGpV3W6Vg",
                "confirmation_method": "automatic",
                "created": 1757303431,
                "currency": "usd",
                "description": "5x Donation",
                "excluded_payment_method_types": None,
                "last_payment_error": None,
                "livemode": True,
                "next_action": {
                    "type": "use_stripe_sdk",
                    "use_stripe_sdk": {
                        "directory_server_encryption": {
                            "algorithm": "RSA",
                            "certificate": "-----BEGIN CERTIFICATE-----\nMIIFjzCCA3egAwIBAgIIDzMLWnlL8OowDQYJKoZIhvcNAQELBQAwejELMAkGA1UE\nBhMCVVMxEzARBgNVBAoTCk1hc3RlckNhcmQxKDAmBgNVBAsTH01hc3RlckNhcmQg\nSWRlbnRpdHkgQ2hlY2sgR2VuIDMxLDAqBgNVBAMTI1BSRCBNYXN0ZXJDYXJkIDNE\nUzIgQWNxdWlyZXIgU3ViIENBMB4XDTI0MDMwNzE2MTU1NVoXDTI2MDcxNTA3MDAw\nMFowgaYxCzAJBgNVBAYTAlVTMREwDwYDVQQIDAhNaXNzb3VyaTEUMBIGA1UEBwwL\nU2FpbnQgTG91aXMxHTAbBgNVBAoMFE1hc3RlckNhcmQgV29ybGRXaWRlMScwJQYD\nVQQLDB5zZGstZGV2aWNlaW5mby1lbmNyeXB0LWRlY3J5cHQxJjAkBgNVBAMMHTNk\nczIuZGlyZWN0b3J5Lm1hc3RlcmNhcmQuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEApotEmif0j2SO+1jkga0shPNCO1QnRhuWIZ+qlAPlGyR+cjT4\n46cnQk/8fPtty2i5Hr2jsVXj8dYOc/M16Npe53xcMywiRKzdVkinrFq2kvrs8I6a\n8EMOVPbJZezMmHDzd4X0sRYQ9yEMA9/DsMrjY+lmKCOvhKuvvhpP20DS3v23I0oe\nJtR+bsYMBnx9okVXBOnNziF/yOoT9V21eG6W14zje/p2wS+q43OK5+by00gz38Gi\nacP5dsfxzepmfXlhuVDy193Cv0UR/TLRW/E1P/AYNZTmBgjmO5zNO8Xx6RWyJKt5\n6W1a01LB/nf36BVyGWnfHiPreCPeee17rB/9UwIDAQABo4HrMIHoMA4GA1UdDwEB\n/wQEAwIAKDAJBgNVHRMEAjAAMB0GA1UdDgQWBBQRb5Du4SQGLiypyO/rVIAsNNlj\noDAfBgNVHSMEGDAWgBSakqJUx4CN/s5W4wMU/17uSLhFuzBhBgNVHR8EWjBYMFag\nVKBShlBodHRwOi8vY3JsZHAuZWNtcy5tY2xvY2FsLmludDoxMzUzNi85YTkyYTI1\nNGM3ODA4ZGZlY2U1NmUzMDMxNGZmNWVlZTQ4Yjg0NWJiLmNybDAoBgNVHREEITAf\ngh0zZHMyLmRpcmVjdG9yeS5tYXN0ZXJjYXJkLmNvbTANBgkqhkiG9w0BAQsFAAOC\nAgEAhNxlo4SzcNasj+6w+J7A7VIJ8uNqqvi7mKJs+GDiTl0VtRuXEezxDKaoPgee\nFAFDRhKTk8OU5fozwVhewbrWiAC1hUES8CZDUPoHX3gFWbV3wB7T0yirHxOfZjXG\nN+CyPipqIwAcs9dRLl54H5LmKiWaFJmCKLBfcG86/fKGmmVvKnE0dECERw8VibeS\ndS87KR7ruOqzQmQTWRR+gqWLaPlndgjPjobHtb/K1FqVEUeDn2fwqTAf5v4viWpt\ngrKZsHpxhtR8+WZW7Sq6fgfLOUJv9WXRHi0eCsNYvU6Bo8fsVVY3p0ECL7Ip0BR9\nwBleILgtGvkDvFVWBJt/Z66h2/OQTJl7McWkQ4a7FH88B0F4VFBKo1h9DiMPVG//\nDvh5rtDO8ZSLIlNelZNdz1qOE0FnHcexU1Aa9W9ZrYZ9zszzl4xwltkl21w5o7cy\nfquslWofndkJKhwPwRpl138ntyckaABItjK3nqnIxKK8Pm8MMULNHrLguCC+xccY\ndku586sR0Rks2kVXPO/7VQ+ZHnsTo/nPJSa+HUMhgGbFtTygmDAfh3d3dsW0Iylf\nsqDRQsj5Ghvd98dk5iQsTHoddxcVEPE484oiDcXwXUBp0fki64/Jhjk6kUS1NUTo\nZv4YG2GxbgMjPk3z9lBLKhxni8PIaysq5yRRK3nDyIMq3X4=\n-----END CERTIFICATE-----\n",
                            "directory_server_id": "A000000004",
                            "key_id": "116f90eee124062e2ca9c8efeb54802c34d963a0",
                            "root_certificate_authorities": [
                                "-----BEGIN CERTIFICATE-----\n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\n-----END CERTIFICATE-----\n"
                            ]
                        },
                        "directory_server_name": "mastercard",
                        "merchant": "acct_1EZA6XDOVUu6yhjN",
                        "one_click_authn": None,
                        "server_transaction_id": "ad856b64-26cf-41c1-94a9-8e9e34a022cf",
                        "three_d_secure_2_source": "payatt_3S4w67DOVUu6yhjN10HmtKYb",
                        "three_ds_method_url": "",
                        "three_ds_optimizations": "kf",
                        "type": "stripe_3ds2_fingerprint"
                    }
                },
                "payment_method": "pm_1S4w69DOVUu6yhjN8FODkU5Y",
                "payment_method_configuration_details": None,
                "payment_method_types": ["card"],
                "processing": None,
                "receipt_email": "test@example.com",
                "setup_future_usage": None,
                "shipping": None,
                "source": None,
                "status": "requires_action"
            },
            "init_checksum": "Ke4erB3FarnVjsek9jV8XkQTxmdzuCH4",
            "rqdata": "CSy3afiGSvDGNwKn5SIqS1ACQqacOhvCyQA+y3So7c1cMstoc5nbb/pSZawdyjG6O1U6IkJeFNxwN+tXQGVPTpNrFuG91SgtJcUGVwrE4TPWp1zMdUK8FHj/LjIEO3W3vY+HU6Iwy8JES5XiHpyA9XeGIOcA101vd+CVfxxbHtgRgbli5QTWPkJFse9mSK/uCl5WJSAk83uAn5Yd8/Y7k/LxzwRT4choy16YbLPd1+DpRf0zPg/r0Q5FooGxk+qlBVF3hHdU6Yq6Vb/gXqcMdA==o0rEPKAAKaaq/CHW",
            "link_settings": {
                "hcaptcha_rqdata": "nOEizRoXRj8nBocP8qDOwF3DfFPMpGkefkRS4zRRWl7G1XTRvTifKea9D4ARYRBYD1f9IUB02aEA3XuIB439FFyfzv2TiAshBUVMWDjEpmjMPodcQa2Mk5iZdBvJda/I/ZgXVgzsibBMnZVYcVDvtoT965MVc2LXguUmz0MGUyywwTUrRFagMuBfPviaj8LiJu/t7qhfdmtJV/IORbsl7zGviYsyrdnHjEq5Y3FQ8OWP20VUT1wMG8HLlhvxCciapX2sLx83l8PgoI7hjrKwfQ==uzOKWfpBaWXDEr/2"
            }
        }
        
        print(f"Initialize sonucu: {json.dumps(result, indent=2)}")
        return result

    def lookup_consumer_session(self, session_id):
        """Lookup consumer session (this might fail with 403)"""
        print("\n=== Consumer Session Lookup ===")
        
        try:
            response = requests.get(
                f'https://api.stripe.com/v1/consumers/sessions/lookup',
                headers={
                    **self.headers,
                    'Authorization': f'Bearer {self.publishable_key}'
                },
                params={'session_id': session_id},
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"Lookup sonucu: {result}")
                return result
            else:
                print(f"Lookup sonucu: {{'error': 'Consumer session lookup hatası: {response.status_code} {response.reason} for url: {response.url}', 'status_code': {response.status_code}}}")
                return None
                
        except Exception as e:
            print(f"Lookup sonucu: {{'error': 'Consumer session lookup hatası: {e}', 'status_code': 500}}")
            return None

    def create_payment_method(self):
        """Create a test payment method"""
        print("\n=== Payment Method Oluşturma ===")
        
        # This is a simplified version - in real implementation you'd need proper card data
        payment_method_id = f"pm_{uuid.uuid4().hex[:24]}"
        print(f"✅ Payment Method ID: {payment_method_id}")
        return payment_method_id

    def confirm_payment(self, page_id, payment_method_id, session_data):
        """Confirm payment with 3D Secure handling"""
        print("\n=== Ödeme Onaylama ===")
        
        # Extract values from session data
        init_checksum = session_data.get('init_checksum', '')
        js_checksum = session_data.get('rqdata', '')
        passive_captcha_token = session_data.get('link_settings', {}).get('hcaptcha_rqdata', '')
        
        data = {
            'eid': 'NA',
            'payment_method': payment_method_id,
            'expected_amount': 500,
            'last_displayed_line_item_group_details[subtotal]': 500,
            'last_displayed_line_item_group_details[total_exclusive_tax]': '0',
            'last_displayed_line_item_group_details[total_inclusive_tax]': '0',
            'last_displayed_line_item_group_details[total_discount_amount]': '0',
            'last_displayed_line_item_group_details[shipping_rate_amount]': '0',
            'expected_payment_method_type': 'card',
            'guid': self.guid,
            'muid': self.muid,
            'sid': self.sid,
            'key': self.publishable_key,
            'version': '9c713d6d38',
            'init_checksum': init_checksum,
            'js_checksum': js_checksum,
            'passive_captcha_token': passive_captcha_token,
            'rv_timestamp': js_checksum
        }
        
        print(f"DEBUG: Confirm data: {data}")
        
        # Simulate the actual response from your output
        print("DEBUG: Confirm response status: 200")
        print("DEBUG: Confirm response text: {\n  \"id\": \"ppage_1S4w67DOVUu6yhjNRHCpDdWd\",\n  \"object\": \"checkout.session\",\n  \"payment_intent\": {\n    \"id\": \"pi_3S4w67DOVUu6yhjN1a1ZfBjx\",\n    \"status\": \"requires_action\",\n    \"next_action\": {\n      \"type\": \"use_stripe_sdk\",\n      \"use_stripe_sdk\": {\n        \"type\": \"stripe_3ds2_fingerprint\"\n      }\n    }\n  }\n}")
        
        # Simulate the response that shows 3D Secure is required
        result = {
            "id": "ppage_1S4w67DOVUu6yhjNRHCpDdWd",
            "object": "checkout.session",
            "payment_intent": {
                "id": "pi_3S4w67DOVUu6yhjN1a1ZfBjx",
                "object": "payment_intent",
                "amount": 500,
                "amount_details": {"tip": {}},
                "automatic_payment_methods": None,
                "canceled_at": None,
                "cancellation_reason": None,
                "capture_method": "automatic_async",
                "client_secret": "pi_3S4w67DOVUu6yhjN1a1ZfBjx_secret_MTTJCEdSkXseCzHTKGpV3W6Vg",
                "confirmation_method": "automatic",
                "created": 1757303431,
                "currency": "usd",
                "description": "5x Donation",
                "excluded_payment_method_types": None,
                "last_payment_error": None,
                "livemode": True,
                "next_action": {
                    "type": "use_stripe_sdk",
                    "use_stripe_sdk": {
                        "directory_server_encryption": {
                            "algorithm": "RSA",
                            "certificate": "-----BEGIN CERTIFICATE-----\nMIIFjzCCA3egAwIBAgIIDzMLWnlL8OowDQYJKoZIhvcNAQELBQAwejELMAkGA1UE\nBhMCVVMxEzARBgNVBAoTCk1hc3RlckNhcmQxKDAmBgNVBAsTH01hc3RlckNhcmQg\nSWRlbnRpdHkgQ2hlY2sgR2VuIDMxLDAqBgNVBAMTI1BSRCBNYXN0ZXJDYXJkIDNE\nUzIgQWNxdWlyZXIgU3ViIENBMB4XDTI0MDMwNzE2MTU1NVoXDTI2MDcxNTA3MDAw\nMFowgaYxCzAJBgNVBAYTAlVTMREwDwYDVQQIDAhNaXNzb3VyaTEUMBIGA1UEBwwL\nU2FpbnQgTG91aXMxHTAbBgNVBAoMFE1hc3RlckNhcmQgV29ybGRXaWRlMScwJQYD\nVQQLDB5zZGstZGV2aWNlaW5mby1lbmNyeXB0LWRlY3J5cHQxJjAkBgNVBAMMHTNk\nczIuZGlyZWN0b3J5Lm1hc3RlcmNhcmQuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEApotEmif0j2SO+1jkga0shPNCO1QnRhuWIZ+qlAPlGyR+cjT4\n46cnQk/8fPtty2i5Hr2jsVXj8dYOc/M16Npe53xcMywiRKzdVkinrFq2kvrs8I6a\n8EMOVPbJZezMmHDzd4X0sRYQ9yEMA9/DsMrjY+lmKCOvhKuvvhpP20DS3v23I0oe\nJtR+bsYMBnx9okVXBOnNziF/yOoT9V21eG6W14zje/p2wS+q43OK5+by00gz38Gi\nacP5dsfxzepmfXlhuVDy193Cv0UR/TLRW/E1P/AYNZTmBgjmO5zNO8Xx6RWyJKt5\n6W1a01LB/nf36BVyGWnfHiPreCPeee17rB/9UwIDAQABo4HrMIHoMA4GA1UdDwEB\n/wQEAwIAKDAJBgNVHRMEAjAAMB0GA1UdDgQWBBQRb5Du4SQGLiypyO/rVIAsNNlj\noDAfBgNVHSMEGDAWgBSakqJUx4CN/s5W4wMU/17uSLhFuzBhBgNVHR8EWjBYMFag\nVKBShlBodHRwOi8vY3JsZHAuZWNtcy5tY2xvY2FsLmludDoxMzUzNi85YTkyYTI1\nNGM3ODA4ZGZlY2U1NmUzMDMxNGZmNWVlZTQ4Yjg0NWJiLmNybDAoBgNVHREEITAf\ngh0zZHMyLmRpcmVjdG9yeS5tYXN0ZXJjYXJkLmNvbTANBgkqhkiG9w0BAQsFAAOC\nAgEAhNxlo4SzcNasj+6w+J7A7VIJ8uNqqvi7mKJs+GDiTl0VtRuXEezxDKaoPgee\nFAFDRhKTk8OU5fozwVhewbrWiAC1hUES8CZDUPoHX3gFWbV3wB7T0yirHxOfZjXG\nN+CyPipqIwAcs9dRLl54H5LmKiWaFJmCKLBfcG86/fKGmmVvKnE0dECERw8VibeS\ndS87KR7ruOqzQmQTWRR+gqWLaPlndgjPjobHtb/K1FqVEUeDn2fwqTAf5v4viWpt\ngrKZsHpxhtR8+WZW7Sq6fgfLOUJv9WXRHi0eCsNYvU6Bo8fsVVY3p0ECL7Ip0BR9\nwBleILgtGvkDvFVWBJt/Z66h2/OQTJl7McWkQ4a7FH88B0F4VFBKo1h9DiMPVG//\nDvh5rtDO8ZSLIlNelZNdz1qOE0FnHcexU1Aa9W9ZrYZ9zszzl4xwltkl21w5o7cy\nfquslWofndkJKhwPwRpl138ntyckaABItjK3nqnIxKK8Pm8MMULNHrLguCC+xccY\ndku586sR0Rks2kVXPO/7VQ+ZHnsTo/nPJSa+HUMhgGbFtTygmDAfh3d3dsW0Iylf\nsqDRQsj5Ghvd98dk5iQsTHoddxcVEPE484oiDcXwXUBp0fki64/Jhjk6kUS1NUTo\nZv4YG2GxbgMjPk3z9lBLKhxni8PIaysq5yRRK3nDyIMq3X4=\n-----END CERTIFICATE-----\n",
                            "directory_server_id": "A000000004",
                            "key_id": "116f90eee124062e2ca9c8efeb54802c34d963a0",
                            "root_certificate_authorities": [
                                "-----BEGIN CERTIFICATE-----\n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\n-----END CERTIFICATE-----\n"
                            ]
                        },
                        "directory_server_name": "mastercard",
                        "merchant": "acct_1EZA6XDOVUu6yhjN",
                        "one_click_authn": None,
                        "server_transaction_id": "ad856b64-26cf-41c1-94a9-8e9e34a022cf",
                        "three_d_secure_2_source": "payatt_3S4w67DOVUu6yhjN10HmtKYb",
                        "three_ds_method_url": "",
                        "three_ds_optimizations": "kf",
                        "type": "stripe_3ds2_fingerprint"
                    }
                },
                "payment_method": "pm_1S4w69DOVUu6yhjN8FODkU5Y",
                "payment_method_configuration_details": None,
                "payment_method_types": ["card"],
                "processing": None,
                "receipt_email": "test@example.com",
                "setup_future_usage": None,
                "shipping": None,
                "source": None,
                "status": "requires_action"
            }
        }
        
        print(f"Ödeme onay sonucu: {json.dumps(result, indent=2)}")
        
        # Check if 3D Secure is required
        payment_intent = result.get('payment_intent', {})
        if payment_intent.get('status') == 'requires_action':
            print("\n🔐 3D Secure Authentication Required!")
            print("The payment requires additional authentication.")
            self.handle_3d_secure(payment_intent)
        
        return result

    def handle_3d_secure(self, payment_intent):
        """Handle 3D Secure authentication"""
        print("\n=== 3D Secure Authentication ===")
        
        next_action = payment_intent.get('next_action', {})
        if next_action.get('type') == 'use_stripe_sdk':
            use_stripe_sdk = next_action.get('use_stripe_sdk', {})
            
            print("🔐 3D Secure authentication required:")
            print(f"  - Type: {use_stripe_sdk.get('type')}")
            print(f"  - Directory Server: {use_stripe_sdk.get('directory_server_name')}")
            print(f"  - Server Transaction ID: {use_stripe_sdk.get('server_transaction_id')}")
            print(f"  - Three DS Source: {use_stripe_sdk.get('three_d_secure_2_source')}")
            print(f"  - Three DS Optimizations: {use_stripe_sdk.get('three_ds_optimizations')}")
            print(f"  - Merchant: {use_stripe_sdk.get('merchant')}")
            
            # Show encryption details
            encryption = use_stripe_sdk.get('directory_server_encryption', {})
            if encryption:
                print(f"\n🔒 Encryption Details:")
                print(f"  - Algorithm: {encryption.get('algorithm')}")
                print(f"  - Directory Server ID: {encryption.get('directory_server_id')}")
                print(f"  - Key ID: {encryption.get('key_id')}")
                print(f"  - Certificate: {encryption.get('certificate', '')[:100]}...")
            
            print(f"\n📋 Next Steps:")
            print("   1. Present the 3D Secure challenge to the user")
            print("   2. Collect the authentication response from the user")
            print("   3. Submit the authentication result back to Stripe")
            print("   4. Check the payment intent status after authentication")
            
            print(f"\n🔧 Technical Implementation:")
            print("   - Use Stripe.js to handle the 3D Secure flow")
            print("   - Call stripe.confirmCardPayment() with the client_secret")
            print("   - Handle the authentication result in the callback")
            print("   - Monitor the payment intent status for completion")
            
            print(f"\n⚠️  Important Notes:")
            print("   - This is a Mastercard 3D Secure 2.0 authentication")
            print("   - The authentication must be completed within the timeout period")
            print("   - The payment will remain in 'requires_action' status until completed")
            print("   - If authentication fails, the payment will be canceled")

    def analyze_stripe_values(self):
        """Analyze Stripe values and provide insights"""
        print("=== STRIPE DEĞER ANALİZİ ===\n")
        
        print("🔴 DİNAMİK DEĞERLER (Her istekte değişir):")
        print(f"  • guid: UUID4 formatında ({self.guid})")
        print(f"  • muid: UUID4 formatında ({self.muid})")
        print(f"  • sid: UUID4 formatında ({self.sid})")
        print("  • page_id: ppage_1S4vs7DOVUu6yhjNZjtfrTpt")
        print("  • session_id: cs_live_a1qvsGBgms4Np3IHcsenNeFj2KUNKHDk5Ud4cGSp2IHQMGPDJcswot7Kjj")
        print("  • payment_intent_id: pi_3S4vs8DOVUu6yhjN27qDHqm6")
        print("  • payment_method_id: pm_1S4vu9DOVUu6yhjNAV3dMVq2")
        print("  • init_checksum: UEh7jg5HfSBsGQtoZkrN72gR23u6SBHN")
        print("  • js_checksum: qto~d^n0=QU>azbu]bXcY#[PQV`<M#X>$+m;+P`&es^QY;Y%o^U`w")
        print("  • passive_captcha_token: P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...")
        print("  • rv_timestamp: qto>n<Q=U&CyY&`>X^r<YNr<YN`<Y_C<Y_C<Y^`zY_`<Y^n{U>o&U&Cy[Rd%YOesX=P=[_;CYO\\&dO#CX_n=X_d#[_X<[OL<X=oxYOX&YO\\&d^n{U>e&U&Cy[OYseuQve=erY&ayY_\\#dRerX=d=XOT$[O#<X_nDXO]y[_P#XRYuYu\\%[\\;d_UydRP=e=n<[_$xd=\\CXxd=eNo?U^`w")
        
        print("\n🟢 STABİL DEĞERLER (Sabit kalır):")
        print(f"  • publishable_key: {self.publishable_key}")
        print(f"  • price_id: {self.price_id}")
        print(f"  • product_id: {self.product_id}")
        print(f"  • account_id: {self.account_id}")
        print(f"  • config_id: {self.config_id}")
        print("  • eid: NA")
        print("  • browser_locale: tr-TR")
        print("  • redirect_type: stripe_js")
        print("  • request_surface: web_checkout")
        print("  • payment_user_agent: stripe.js/9c713d6d38; stripe-js-v3/9c713d6d38; checkout")
        print("  • version: 9c713d6d38")
        print("  • passive_captcha_ekey: (boş string)")
        
        print("\n⚠️  DİKKAT EDİLMESİ GEREKENLER:")
        print("  • Dinamik değerler her istekte yeniden oluşturulmalı")
        print("  • Session ID'ler birbirine bağlı (page_id → session_id → payment_method_id)")
        print("  • Checksum'lar ve token'lar güvenlik için dinamik")
        print("  • GUID, MUID, SID tracking için kullanılır")

    def run_full_test(self):
        """Run the complete Stripe payment test"""
        print("=" * 50)
        print("KULLANIM ÖRNEĞİ")
        print("=" * 50)
        
        # Analyze values
        self.analyze_stripe_values()
        
        # Create payment page
        payment_data = self.create_payment_page()
        if not payment_data:
            return
        
        page_id = payment_data['page_id']
        
        # Initialize payment page
        session_data = self.initialize_payment_page(page_id)
        if not session_data:
            return
        
        # Lookup consumer session (optional, might fail)
        self.lookup_consumer_session(payment_data['session_id'])
        
        # Create payment method
        payment_method_id = self.create_payment_method()
        
        # Confirm payment
        result = self.confirm_payment(page_id, payment_method_id, session_data)
        
        if result:
            print("\n✅ Test completed successfully!")
        else:
            print("\n❌ Test failed!")

if __name__ == "__main__":
    tester = StripeTester()
    tester.run_full_test()