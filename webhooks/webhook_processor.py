# webhook_processor.py


def process_webhook(data):
    # Validate and process webhook payload
    # Example: Log the event and return a response
    print(f"Received webhook payload: {data}")
    return {"message": "Webhook processed successfully"}
