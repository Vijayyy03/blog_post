// Comprehensive Test Script for Omnify Blog Application
// Run this in browser console (F12 -> Console tab)

console.log('=== COMPREHENSIVE TEST ===');

// Test 1: Check if user is authenticated
async function testAuthentication() {
  console.log('\n1. Testing Authentication...');
  const token = localStorage.getItem('token');
  console.log('Token exists:', !!token);
  
  if (token) {
    try {
      const response = await fetch('http://localhost:8000/api/auth/me/', {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });
      
      if (response.ok) {
        const user = await response.json();
        console.log('✅ User authenticated:', user.name);
        return true;
      } else {
        console.log('❌ User not authenticated');
        return false;
      }
    } catch (error) {
      console.log('❌ Auth test failed:', error);
      return false;
    }
  } else {
    console.log('❌ No token found');
    return false;
  }
}

// Test 2: Test blog listing
async function testBlogListing() {
  console.log('\n2. Testing Blog Listing...');
  try {
    const response = await fetch('http://localhost:8000/api/blogs/');
    if (response.ok) {
      const data = await response.json();
      console.log('✅ Blog listing works:', data.count, 'blogs found');
      return true;
    } else {
      console.log('❌ Blog listing failed');
      return false;
    }
  } catch (error) {
    console.log('❌ Blog listing test failed:', error);
    return false;
  }
}

// Test 3: Test blog creation (if authenticated)
async function testBlogCreation() {
  console.log('\n3. Testing Blog Creation...');
  const token = localStorage.getItem('token');
  
  if (!token) {
    console.log('⚠️ Skipping blog creation test - not authenticated');
    return false;
  }
  
  try {
    const blogData = {
      title: 'Test Blog from Frontend',
      content: 'This is a test blog created from the frontend.',
      excerpt: 'Test blog excerpt'
    };
    
    const response = await fetch('http://localhost:8000/api/blogs/create/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(blogData)
    });
    
    if (response.ok) {
      const blog = await response.json();
      console.log('✅ Blog creation works:', blog.title);
      return blog.slug;
    } else {
      const error = await response.json();
      console.log('❌ Blog creation failed:', error);
      return false;
    }
  } catch (error) {
    console.log('❌ Blog creation test failed:', error);
    return false;
  }
}

// Test 4: Test blog detail view
async function testBlogDetail(slug) {
  console.log('\n4. Testing Blog Detail View...');
  if (!slug) {
    console.log('⚠️ Skipping blog detail test - no blog slug');
    return false;
  }
  
  try {
    const response = await fetch(`http://localhost:8000/api/blogs/${slug}/`);
    if (response.ok) {
      const blog = await response.json();
      console.log('✅ Blog detail works:', blog.title);
      return true;
    } else {
      console.log('❌ Blog detail failed');
      return false;
    }
  } catch (error) {
    console.log('❌ Blog detail test failed:', error);
    return false;
  }
}

// Test 5: Test categories and tags
async function testCategoriesAndTags() {
  console.log('\n5. Testing Categories and Tags...');
  
  try {
    // Test categories
    const categoriesResponse = await fetch('http://localhost:8000/api/blogs/categories/');
    if (categoriesResponse.ok) {
      const categories = await categoriesResponse.json();
      console.log('✅ Categories work:', categories.count, 'categories');
    } else {
      console.log('❌ Categories failed');
    }
    
    // Test tags
    const tagsResponse = await fetch('http://localhost:8000/api/blogs/tags/');
    if (tagsResponse.ok) {
      const tags = await tagsResponse.json();
      console.log('✅ Tags work:', tags.count, 'tags');
    } else {
      console.log('❌ Tags failed');
    }
    
    return true;
  } catch (error) {
    console.log('❌ Categories/Tags test failed:', error);
    return false;
  }
}

// Test 6: Test featured blogs
async function testFeaturedBlogs() {
  console.log('\n6. Testing Featured Blogs...');
  
  try {
    const response = await fetch('http://localhost:8000/api/blogs/featured/');
    if (response.ok) {
      const blogs = await response.json();
      console.log('✅ Featured blogs work:', blogs.length, 'featured blogs');
      return true;
    } else {
      console.log('❌ Featured blogs failed');
      return false;
    }
  } catch (error) {
    console.log('❌ Featured blogs test failed:', error);
    return false;
  }
}

// Test 7: Test user registration
async function testUserRegistration() {
  console.log('\n7. Testing User Registration...');
  
  try {
    const userData = {
      name: 'Test User Frontend',
      email: `test${Date.now()}@example.com`,
      password: 'testpass123',
      password2: 'testpass123'
    };
    
    const response = await fetch('http://localhost:8000/api/auth/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(userData)
    });
    
    if (response.ok) {
      const result = await response.json();
      console.log('✅ User registration works:', result.user.name);
      return result.tokens.access;
    } else {
      const error = await response.json();
      console.log('❌ User registration failed:', error);
      return false;
    }
  } catch (error) {
    console.log('❌ User registration test failed:', error);
    return false;
  }
}

// Test 8: Test user login
async function testUserLogin() {
  console.log('\n8. Testing User Login...');
  
  try {
    const loginData = {
      email: 'test@example.com',
      password: 'testpass123'
    };
    
    const response = await fetch('http://localhost:8000/api/auth/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(loginData)
    });
    
    if (response.ok) {
      const result = await response.json();
      console.log('✅ User login works:', result.user.name);
      return result.tokens.access;
    } else {
      const error = await response.json();
      console.log('❌ User login failed:', error);
      return false;
    }
  } catch (error) {
    console.log('❌ User login test failed:', error);
    return false;
  }
}

// Run all tests
async function runAllTests() {
  console.log('Starting comprehensive test...\n');
  
  const results = {
    auth: await testAuthentication(),
    listing: await testBlogListing(),
    categories: await testCategoriesAndTags(),
    featured: await testFeaturedBlogs(),
    registration: await testUserRegistration(),
    login: await testUserLogin()
  };
  
  // Test blog creation and detail if authenticated
  if (results.auth) {
    const blogSlug = await testBlogCreation();
    if (blogSlug) {
      results.creation = true;
      results.detail = await testBlogDetail(blogSlug);
    } else {
      results.creation = false;
      results.detail = false;
    }
  } else {
    results.creation = false;
    results.detail = false;
  }
  
  // Summary
  console.log('\n=== TEST SUMMARY ===');
  console.log('Authentication:', results.auth ? '✅ PASS' : '❌ FAIL');
  console.log('Blog Listing:', results.listing ? '✅ PASS' : '❌ FAIL');
  console.log('Blog Creation:', results.creation ? '✅ PASS' : '❌ FAIL');
  console.log('Blog Detail:', results.detail ? '✅ PASS' : '❌ FAIL');
  console.log('Categories/Tags:', results.categories ? '✅ PASS' : '❌ FAIL');
  console.log('Featured Blogs:', results.featured ? '✅ PASS' : '❌ FAIL');
  console.log('User Registration:', results.registration ? '✅ PASS' : '❌ FAIL');
  console.log('User Login:', results.login ? '✅ PASS' : '❌ FAIL');
  
  const passed = Object.values(results).filter(Boolean).length;
  const total = Object.keys(results).length;
  
  console.log(`\nOverall: ${passed}/${total} tests passed`);
  
  if (passed === total) {
    console.log('🎉 All tests passed! The application is working correctly.');
  } else {
    console.log('⚠️ Some tests failed. Check the details above.');
  }
}

// Run the tests
runAllTests();

console.log('\n=== END COMPREHENSIVE TEST ==='); 