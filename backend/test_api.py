#!/usr/bin/env python
"""
Test script for Django Blog API
"""
import os
import sys
import django
import requests
import json

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

def test_api_endpoints():
    """Test the API endpoints."""
    base_url = 'http://localhost:8000/api'
    
    print("Testing Django Blog API endpoints...")
    print("=" * 50)
    
    # Test 1: Get all blogs
    print("\n1. Testing GET /api/blogs/")
    try:
        response = requests.get(f'{base_url}/blogs/')
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            print(f"Number of blogs: {len(data.get('results', []))}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 2: Get categories
    print("\n2. Testing GET /api/blogs/categories/")
    try:
        response = requests.get(f'{base_url}/blogs/categories/')
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 3: Get tags
    print("\n3. Testing GET /api/blogs/tags/")
    try:
        response = requests.get(f'{base_url}/blogs/tags/')
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 4: Get featured blogs
    print("\n4. Testing GET /api/blogs/featured/")
    try:
        response = requests.get(f'{base_url}/blogs/featured/')
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 50)
    print("API testing completed!")

if __name__ == '__main__':
    test_api_endpoints() 