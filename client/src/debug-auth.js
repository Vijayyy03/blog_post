// Debug script to check authentication status
// Run this in browser console (F12 -> Console tab)

console.log('=== AUTH DEBUG ===');

// Check if token exists
const token = localStorage.getItem('token');
console.log('Token exists:', !!token);
if (token) {
  console.log('Token length:', token.length);
  console.log('Token preview:', token.substring(0, 50) + '...');
}

// Test current user endpoint
async function testAuth() {
  try {
    const response = await fetch('http://localhost:8000/api/auth/me/', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });
    
    console.log('Auth test status:', response.status);
    const data = await response.json();
    console.log('Auth test response:', data);
    
    if (response.ok) {
      console.log('✅ User is authenticated');
    } else {
      console.log('❌ User is not authenticated');
    }
  } catch (error) {
    console.log('❌ Auth test failed:', error);
  }
}

// Test blog creation
async function testBlogCreation() {
  try {
    const blogData = {
      title: 'Debug Test Blog',
      content: 'This is a test blog for debugging.',
      excerpt: 'Debug test'
    };
    
    const response = await fetch('http://localhost:8000/api/blogs/create/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(blogData)
    });
    
    console.log('Blog creation status:', response.status);
    const data = await response.json();
    console.log('Blog creation response:', data);
    
    if (response.ok) {
      console.log('✅ Blog creation successful');
    } else {
      console.log('❌ Blog creation failed');
    }
  } catch (error) {
    console.log('❌ Blog creation test failed:', error);
  }
}

// Run tests
testAuth();
testBlogCreation();

console.log('=== END DEBUG ==='); 