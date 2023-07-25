from django.http import JsonResponse
import time

def short_polling_view(request):
    # Simulate some data on the server
    data = {"name": "Annu"}
    return JsonResponse(data)


def long_polling_view(request):
    # Simulate some data source (e.g., a message queue, database, or real-time data)
    # For demonstration purposes, we'll use a list as our data source.
    data_source = []

    # Get the client's timestamp (if provided)
    client_timestamp = request.GET.get('timestamp')

    # Wait for new data to become available or until a timeout is reached
    timeout = 5  # Adjust the timeout as needed
    start_time = time.time()

    while not data_source and time.time() - start_time < timeout:
        time.sleep(1)  # Adjust the sleep interval as needed

    # Prepare the response data
    response_data = {"data": data_source}

    # If the client's timestamp is provided, only return data if it's newer than the client's timestamp
    if client_timestamp:
        response_data["data"] = [data for data in data_source if data["timestamp"] > client_timestamp]

    return JsonResponse(response_data)
