#!/usr/bin/env python3
"""
Stripe 3D Secure Backend Implementation
Handles payment intent creation and status checking for 3D Secure authentication
"""

import os
import json
from flask import Flask, request, jsonify
import stripe

# Initialize Flask app
app = Flask(__name__)

# Configure Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY', 'sk_live_your_secret_key_here')
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', 'pk_live_55qfW3vO5o0MsooVCZgUg2lN00ptm6nUQG')

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """Create a payment intent for 3D Secure authentication"""
    try:
        data = request.get_json()
        amount = int(data.get('amount', 500))  # Default to $5.00
        currency = data.get('currency', 'usd')
        email = data.get('email', '')
        name = data.get('name', '')
        
        # Create payment intent with 3D Secure enabled
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            metadata={
                'email': email,
                'name': name,
            },
            # Enable 3D Secure authentication
            payment_method_types=['card'],
            confirmation_method='manual',
            # Don't confirm immediately - let frontend handle 3D Secure
            confirm=False,
            # Optional: Set up automatic payment methods
            automatic_payment_methods={
                'enabled': True,
            },
        )
        
        return jsonify({
            'client_secret': payment_intent.client_secret,
            'payment_intent_id': payment_intent.id,
            'status': payment_intent.status
        })
        
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f"Error creating payment intent: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/confirm-payment-intent', methods=['POST'])
def confirm_payment_intent():
    """Confirm a payment intent after 3D Secure authentication"""
    try:
        data = request.get_json()
        payment_intent_id = data.get('payment_intent_id')
        
        if not payment_intent_id:
            return jsonify({'error': 'Payment intent ID is required'}), 400
        
        # Retrieve the payment intent
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        
        # Confirm the payment intent
        confirmed_intent = stripe.PaymentIntent.confirm(payment_intent_id)
        
        return jsonify({
            'status': confirmed_intent.status,
            'payment_intent_id': confirmed_intent.id,
            'amount': confirmed_intent.amount,
            'currency': confirmed_intent.currency,
        })
        
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f"Error confirming payment intent: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/payment-intent-status/<payment_intent_id>', methods=['GET'])
def get_payment_intent_status(payment_intent_id):
    """Get the current status of a payment intent"""
    try:
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        
        return jsonify({
            'status': payment_intent.status,
            'amount': payment_intent.amount,
            'currency': payment_intent.currency,
            'created': payment_intent.created,
            'last_payment_error': payment_intent.last_payment_error,
        })
        
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f"Error retrieving payment intent: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle Stripe webhooks for payment status updates"""
    payload = request.get_data()
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET', 'whsec_your_webhook_secret_here')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        print(f"Invalid payload: {e}")
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError as e:
        print(f"Invalid signature: {e}")
        return jsonify({'error': 'Invalid signature'}), 400
    
    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        print(f"Payment succeeded: {payment_intent['id']}")
        # Handle successful payment
        handle_payment_success(payment_intent)
        
    elif event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        print(f"Payment failed: {payment_intent['id']}")
        # Handle failed payment
        handle_payment_failure(payment_intent)
        
    elif event['type'] == 'payment_intent.requires_action':
        payment_intent = event['data']['object']
        print(f"Payment requires action: {payment_intent['id']}")
        # Handle 3D Secure requirement
        handle_payment_requires_action(payment_intent)
    
    return jsonify({'status': 'success'})

def handle_payment_success(payment_intent):
    """Handle successful payment"""
    print(f"Payment succeeded for {payment_intent['amount']} {payment_intent['currency']}")
    # Add your business logic here:
    # - Send confirmation email
    # - Update database
    # - Trigger fulfillment process
    pass

def handle_payment_failure(payment_intent):
    """Handle failed payment"""
    print(f"Payment failed: {payment_intent.get('last_payment_error', {}).get('message', 'Unknown error')}")
    # Add your business logic here:
    # - Send failure notification
    # - Log the failure
    # - Update order status
    pass

def handle_payment_requires_action(payment_intent):
    """Handle payment requiring 3D Secure authentication"""
    print(f"Payment requires 3D Secure authentication: {payment_intent['id']}")
    # Add your business logic here:
    # - Notify user about authentication requirement
    # - Update order status to pending
    pass

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'stripe-3ds-backend'})

if __name__ == '__main__':
    # Set up environment variables
    if not os.getenv('STRIPE_SECRET_KEY'):
        print("Warning: STRIPE_SECRET_KEY not set. Using placeholder.")
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)