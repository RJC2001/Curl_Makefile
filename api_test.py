import subprocess
import json


def send_request(url):
    result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def test_endpoint(url, expected_keys):
    response = send_request(url)
    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        return "FAILED: Invalid JSON response"

    for key in expected_keys:
        if key not in data:
            return f"FAILED: Missing key '{key}' in response"

    return "PASSED"


def main():
    base_url = "https://jsonplaceholder.typicode.com"

    tests = [
        {"url": f"{base_url}/posts/1", "expected_keys": ["userId", "id", "title", "body"]},
        {"url": f"{base_url}/users/1", "expected_keys": ["id", "name", "username", "email"]},
        {"url": f"{base_url}/comments/1", "expected_keys": ["postId", "id", "name", "email", "body"]}
    ]

    for i, test in enumerate(tests, start=1):
        result = test_endpoint(test["url"], test["expected_keys"])
        print(f"Test {i}: {result}")


if __name__ == "__main__":
    main()