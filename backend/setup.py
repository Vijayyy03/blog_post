#!/usr/bin/env python
"""
Setup script for Django Blog Application
"""
import os
import sys
import django
from django.core.management import execute_from_command_line
from django.contrib.auth import get_user_model

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

User = get_user_model()


def create_superuser():
    """Create a superuser if none exists."""
    if not User.objects.filter(is_superuser=True).exists():
        print("Creating superuser...")
        try:
            user = User.objects.create_superuser(
                email='admin@omnify.com',
                name='Admin User',
                password='admin123'
            )
            print(f"Superuser created: {user.email}")
        except Exception as e:
            print(f"Error creating superuser: {e}")
    else:
        print("Superuser already exists.")


def create_sample_data():
    """Create sample categories, tags, and blog posts."""
    from blogs.models import Category, Tag, Blog
    from django.utils import timezone
    
    # Create sample categories
    categories = [
        {'name': 'Technology', 'description': 'Technology related posts'},
        {'name': 'Programming', 'description': 'Programming and development posts'},
        {'name': 'Web Development', 'description': 'Web development posts'},
        {'name': 'Design', 'description': 'Design and UI/UX posts'},
        {'name': 'Business', 'description': 'Business and entrepreneurship posts'},
    ]
    
    created_categories = {}
    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        created_categories[cat_data['name']] = category
        if created:
            print(f"Created category: {category.name}")
    
    # Create sample tags
    tags = [
        'Python', 'Django', 'React', 'JavaScript', 'CSS', 'HTML',
        'API', 'Database', 'PostgreSQL', 'Docker', 'AWS', 'Git',
        'Frontend', 'Backend', 'Full-stack', 'Mobile', 'Web'
    ]
    
    created_tags = {}
    for tag_name in tags:
        tag, created = Tag.objects.get_or_create(name=tag_name)
        created_tags[tag_name] = tag
        if created:
            print(f"Created tag: {tag.name}")
    
    # Create sample blog posts
    sample_blogs = [
        {
            'title': 'Getting Started with Django REST Framework',
            'content': '''# Getting Started with Django REST Framework

Django REST Framework (DRF) is a powerful toolkit for building Web APIs. It provides a set of tools and utilities that make it easy to build RESTful APIs with Django.

## Why Django REST Framework?

DRF offers several advantages:
- **Serialization**: Easy conversion of Django models to JSON
- **Authentication**: Built-in support for various authentication methods
- **Permissions**: Flexible permission system
- **Views**: Class-based views for common API patterns
- **Testing**: Comprehensive testing utilities

## Basic Setup

First, install DRF:
```bash
pip install djangorestframework
```

Add it to your INSTALLED_APPS:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Creating Your First API

Let's create a simple API for a blog:

```python
from rest_framework import serializers
from rest_framework import generics
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
```

## Authentication

DRF supports various authentication methods:
- Token Authentication
- Session Authentication
- JWT Authentication
- OAuth2

## Conclusion

Django REST Framework makes building APIs with Django straightforward and efficient. Its comprehensive feature set and excellent documentation make it a top choice for API development.
''',
            'excerpt': 'Learn how to build powerful APIs with Django REST Framework, including authentication, serialization, and best practices.',
            'category': created_categories['Programming'],
            'tags': [created_tags['Python'], created_tags['Django'], created_tags['API']],
            'is_featured': True
        },
        {
            'title': 'Building Modern UIs with React and Tailwind CSS',
            'content': '''# Building Modern UIs with React and Tailwind CSS

React and Tailwind CSS are a powerful combination for building modern, responsive user interfaces. This guide will show you how to create beautiful, functional UIs efficiently.

## Why React + Tailwind?

**React** provides:
- Component-based architecture
- Virtual DOM for performance
- Rich ecosystem of libraries
- Excellent developer experience

**Tailwind CSS** offers:
- Utility-first approach
- Rapid prototyping
- Consistent design system
- Small bundle size in production

## Setting Up the Project

Create a new React project:
```bash
npx create-react-app my-app
cd my-app
```

Install Tailwind CSS:
```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

## Configuration

Update your `tailwind.config.js`:
```javascript
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## Building Components

Here's an example of a modern card component:

```jsx
function BlogCard({ title, excerpt, author, date }) {
  return (
    <div className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
      <div className="p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-2">
          {title}
        </h3>
        <p className="text-gray-600 mb-4">
          {excerpt}
        </p>
        <div className="flex items-center justify-between">
          <span className="text-sm text-gray-500">{author}</span>
          <span className="text-sm text-gray-500">{date}</span>
        </div>
      </div>
    </div>
  )
}
```

## Responsive Design

Tailwind makes responsive design easy:
```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  {/* Cards will stack on mobile, 2 columns on tablet, 3 on desktop */}
</div>
```

## Best Practices

1. **Component Composition**: Break down complex UIs into reusable components
2. **Utility Classes**: Use Tailwind's utility classes for consistent styling
3. **Responsive Design**: Always consider mobile-first design
4. **Performance**: Use React.memo for expensive components
5. **Accessibility**: Include proper ARIA labels and semantic HTML

## Conclusion

React and Tailwind CSS together provide a powerful, efficient way to build modern web applications. The combination of React's component system and Tailwind's utility-first approach results in maintainable, scalable code.
''',
            'excerpt': 'Learn how to create beautiful, responsive user interfaces using React and Tailwind CSS with practical examples and best practices.',
            'category': created_categories['Web Development'],
            'tags': [created_tags['React'], created_tags['JavaScript'], created_tags['CSS'], created_tags['Frontend']],
            'is_featured': True
        },
        {
            'title': 'PostgreSQL vs MongoDB: Choosing the Right Database',
            'content': '''# PostgreSQL vs MongoDB: Choosing the Right Database

When building modern applications, choosing the right database is crucial. PostgreSQL and MongoDB are two popular options, each with their own strengths and use cases.

## PostgreSQL: The Relational Powerhouse

PostgreSQL is a powerful, open-source relational database that excels in:

### Strengths
- **ACID Compliance**: Full ACID transactions ensure data integrity
- **Complex Queries**: Advanced SQL features for complex data relationships
- **Data Types**: Rich set of data types including JSON, arrays, and custom types
- **Extensions**: Extensive ecosystem of extensions
- **Maturity**: Battle-tested in production environments

### Use Cases
- Financial applications requiring strict data consistency
- Applications with complex relationships between data
- Reporting and analytics systems
- Applications requiring advanced SQL features

## MongoDB: The Document Store

MongoDB is a NoSQL document database that offers:

### Strengths
- **Flexibility**: Schema-less design allows rapid iteration
- **Scalability**: Horizontal scaling with sharding
- **JSON-like Documents**: Natural fit for JavaScript applications
- **Performance**: Fast read/write operations for document-based data
- **Developer Experience**: Intuitive for developers familiar with JSON

### Use Cases
- Content management systems
- Real-time applications
- Applications with rapidly changing schemas
- Prototyping and rapid development

## Performance Comparison

| Aspect | PostgreSQL | MongoDB |
|--------|------------|---------|
| Complex Queries | Excellent | Good |
| Simple CRUD | Good | Excellent |
| Schema Changes | Requires migration | Flexible |
| ACID Compliance | Full | Limited |

## Code Examples

### PostgreSQL with Django
```python
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['author', 'created_at']),
        ]
```

### MongoDB with Python
```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.blog_db
posts = db.posts

# Insert a document
post = {
    'title': 'My Blog Post',
    'content': 'This is the content...',
    'author': 'John Doe',
    'created_at': datetime.now()
}
posts.insert_one(post)
```

## Making the Choice

### Choose PostgreSQL when:
- You need complex relationships between data
- Data consistency is critical
- You're building financial or enterprise applications
- You need advanced SQL features

### Choose MongoDB when:
- You're building content-heavy applications
- Your schema changes frequently
- You need horizontal scaling
- You're prototyping rapidly

## Conclusion

Both PostgreSQL and MongoDB are excellent databases, but they serve different purposes. PostgreSQL excels in structured, relational data with complex relationships, while MongoDB shines in flexible, document-based applications. The choice depends on your specific use case, data structure, and application requirements.
''',
            'excerpt': 'Compare PostgreSQL and MongoDB to understand their strengths, use cases, and when to choose each database for your application.',
            'category': created_categories['Technology'],
            'tags': [created_tags['Database'], created_tags['PostgreSQL'], created_tags['API']],
            'is_featured': False
        },
        {
            'title': 'The Future of Web Development: Trends to Watch',
            'content': '''# The Future of Web Development: Trends to Watch

Web development is constantly evolving, with new technologies and methodologies emerging regularly. Let's explore the key trends that will shape the future of web development.

## 1. Serverless Architecture

Serverless computing is revolutionizing how we build and deploy applications.

### Benefits
- **Scalability**: Automatic scaling based on demand
- **Cost Efficiency**: Pay only for actual usage
- **Reduced Complexity**: No server management required
- **Faster Development**: Focus on business logic, not infrastructure

### Popular Platforms
- AWS Lambda
- Vercel Functions
- Netlify Functions
- Google Cloud Functions

## 2. Jamstack Architecture

Jamstack (JavaScript, APIs, and Markup) is gaining popularity for its performance and developer experience.

### Core Principles
- **Decoupling**: Separate frontend and backend
- **Pre-rendering**: Static site generation for better performance
- **CDN Delivery**: Global content delivery
- **API-first**: Backend as a service

### Benefits
- **Performance**: Fast loading times
- **Security**: Reduced attack surface
- **Scalability**: Easy to scale
- **Developer Experience**: Modern development workflow

## 3. Web Components

Web Components are becoming the standard for building reusable UI elements.

### Features
- **Custom Elements**: Create new HTML elements
- **Shadow DOM**: Encapsulated styling
- **HTML Templates**: Reusable markup

### Example
```javascript
class BlogCard extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }
  
  connectedCallback() {
    this.shadowRoot.innerHTML = `
      <style>
        .card { padding: 1rem; border: 1px solid #ccc; }
      </style>
      <div class="card">
        <slot></slot>
      </div>
    `;
  }
}

customElements.define('blog-card', BlogCard);
```

## 4. Progressive Web Apps (PWAs)

PWAs combine the best of web and mobile applications.

### Features
- **Offline Functionality**: Service workers for offline access
- **App-like Experience**: Native app feel
- **Push Notifications**: Engage users effectively
- **Installable**: Add to home screen

## 5. AI and Machine Learning Integration

AI is becoming increasingly important in web development.

### Applications
- **Content Generation**: AI-powered content creation
- **Personalization**: Dynamic content based on user behavior
- **Chatbots**: Intelligent customer service
- **Image Recognition**: Automated image processing

## 6. WebAssembly (WASM)

WebAssembly allows running high-performance code in the browser.

### Use Cases
- **Performance-critical Applications**: Games, video editing
- **Legacy Code Integration**: Running existing C++/Rust code
- **Cross-platform Development**: Share code between web and native

## 7. Micro Frontends

Micro frontends extend microservices architecture to the frontend.

### Benefits
- **Team Autonomy**: Independent development teams
- **Technology Diversity**: Use different frameworks
- **Scalability**: Scale teams and applications independently
- **Maintainability**: Easier to maintain large applications

## 8. GraphQL

GraphQL is becoming the preferred API query language.

### Advantages
- **Flexible Queries**: Get exactly the data you need
- **Single Endpoint**: One endpoint for all data
- **Strong Typing**: Type-safe API development
- **Real-time Updates**: Subscriptions for live data

## 9. Containerization and Kubernetes

Containerization is essential for modern deployment strategies.

### Benefits
- **Consistency**: Same environment across development and production
- **Scalability**: Easy horizontal scaling
- **Portability**: Run anywhere
- **Isolation**: Secure application boundaries

## 10. Low-Code/No-Code Platforms

Low-code platforms are democratizing web development.

### Features
- **Visual Development**: Drag-and-drop interfaces
- **Pre-built Components**: Ready-to-use UI elements
- **Rapid Prototyping**: Quick application development
- **Business User Empowerment**: Non-developers can build applications

## Conclusion

The future of web development is exciting and dynamic. These trends are shaping how we build, deploy, and maintain web applications. Staying current with these technologies will be crucial for developers who want to remain competitive in the industry.

The key is to understand which trends align with your project requirements and to adopt them strategically rather than following every new technology blindly.
''',
            'excerpt': 'Explore the latest trends in web development, from serverless architecture to AI integration, and understand how they will shape the future of the industry.',
            'category': created_categories['Technology'],
            'tags': [created_tags['Web'], created_tags['Frontend'], created_tags['Backend']],
            'is_featured': False
        },
        {
            'title': 'Design Principles for Modern Web Applications',
            'content': '''# Design Principles for Modern Web Applications

Good design is crucial for creating successful web applications. This guide covers essential design principles that will help you create user-friendly, accessible, and beautiful web applications.

## 1. User-Centered Design

Always put your users first when designing web applications.

### Key Principles
- **User Research**: Understand your target audience
- **User Testing**: Regular testing with real users
- **Feedback Loops**: Collect and act on user feedback
- **Accessibility**: Design for all users, including those with disabilities

### Implementation
```css
/* Ensure sufficient color contrast */
.text-primary {
  color: #1a202c; /* Dark text on light background */
}

/* Provide focus indicators */
.button:focus {
  outline: 2px solid #3182ce;
  outline-offset: 2px;
}
```

## 2. Visual Hierarchy

Create clear visual hierarchy to guide users through your interface.

### Elements of Hierarchy
- **Typography**: Use different font sizes and weights
- **Color**: Use color to create emphasis
- **Spacing**: Use whitespace effectively
- **Layout**: Organize content logically

### Example
```html
<div class="blog-post">
  <h1 class="text-4xl font-bold mb-4">Main Title</h1>
  <h2 class="text-2xl font-semibold mb-3">Section Title</h2>
  <p class="text-lg mb-2">Body text with good readability</p>
  <small class="text-sm text-gray-600">Supporting text</small>
</div>
```

## 3. Consistency

Maintain consistency across your application for better user experience.

### Areas of Consistency
- **Color Palette**: Use a consistent color scheme
- **Typography**: Stick to a limited set of fonts
- **Spacing**: Use consistent spacing values
- **Components**: Reuse design patterns

### Design System
```css
:root {
  /* Color palette */
  --primary: #3182ce;
  --secondary: #718096;
  --success: #38a169;
  --error: #e53e3e;
  
  /* Spacing scale */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
}
```

## 4. Responsive Design

Ensure your application works well on all devices.

### Mobile-First Approach
```css
/* Start with mobile styles */
.container {
  padding: 1rem;
  max-width: 100%;
}

/* Tablet styles */
@media (min-width: 768px) {
  .container {
    padding: 2rem;
    max-width: 768px;
  }
}

/* Desktop styles */
@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
  }
}
```

## 5. Performance and Loading States

Design for performance and provide good loading experiences.

### Loading States
```jsx
function BlogList() {
  const [loading, setLoading] = useState(true);
  const [blogs, setBlogs] = useState([]);
  
  if (loading) {
    return (
      <div className="space-y-4">
        {[1, 2, 3].map(i => (
          <div key={i} className="animate-pulse">
            <div className="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
            <div className="h-3 bg-gray-200 rounded w-1/2"></div>
          </div>
        ))}
      </div>
    );
  }
  
  return (
    <div className="space-y-4">
      {blogs.map(blog => (
        <BlogCard key={blog.id} blog={blog} />
      ))}
    </div>
  );
}
```

## 6. Accessibility (A11y)

Make your applications accessible to all users.

### WCAG Guidelines
- **Perceivable**: Information must be presentable to users
- **Operable**: Interface components must be operable
- **Understandable**: Information and operation must be understandable
- **Robust**: Content must be robust enough for assistive technologies

### Implementation
```html
<!-- Proper semantic HTML -->
<main role="main">
  <h1>Page Title</h1>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</main>

<!-- ARIA labels for complex components -->
<button aria-label="Close dialog" aria-describedby="dialog-description">
  ×
</button>
```

## 7. Micro-interactions

Add subtle animations and interactions to enhance user experience.

### Examples
```css
/* Hover effects */
.button {
  transition: all 0.2s ease;
}

.button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Loading animations */
.spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

## 8. Error Handling

Design for error states and provide helpful feedback.

### Error States
```jsx
function ErrorBoundary({ children }) {
  const [hasError, setHasError] = useState(false);
  
  if (hasError) {
    return (
      <div className="text-center py-8">
        <h2 className="text-xl font-semibold text-red-600 mb-2">
          Something went wrong
        </h2>
        <p className="text-gray-600 mb-4">
          We're working to fix the problem. Please try again later.
        </p>
        <button 
          onClick={() => window.location.reload()}
          className="px-4 py-2 bg-blue-600 text-white rounded"
        >
          Reload Page
        </button>
      </div>
    );
  }
  
  return children;
}
```

## 9. Data Visualization

Present data in clear, understandable ways.

### Principles
- **Simplicity**: Keep visualizations simple and clear
- **Accuracy**: Ensure data is represented accurately
- **Context**: Provide necessary context for data
- **Interactivity**: Allow users to explore data

## 10. Testing and Iteration

Continuously test and improve your designs.

### Testing Methods
- **Usability Testing**: Test with real users
- **A/B Testing**: Compare different design approaches
- **Analytics**: Use data to inform design decisions
- **Accessibility Testing**: Ensure compliance with standards

## Conclusion

Good design is not just about aesthetics—it's about creating functional, accessible, and user-friendly applications. By following these principles, you can create web applications that provide excellent user experiences and achieve your business goals.

Remember that design is an iterative process. Continuously gather feedback, test with users, and refine your designs based on real-world usage.
''',
            'excerpt': 'Learn essential design principles for creating modern, user-friendly web applications with practical examples and best practices.',
            'category': created_categories['Design'],
            'tags': [created_tags['Frontend'], created_tags['CSS'], created_tags['Web']],
            'is_featured': False
        }
    ]
    
    # Get or create a test user for the blog posts
    test_user, created = User.objects.get_or_create(
        email='demo@omnify.com',
        defaults={
            'name': 'Demo User',
            'password': 'demo123'
        }
    )
    if created:
        test_user.set_password('demo123')
        test_user.save()
        print(f"Created demo user: {test_user.email}")
    
    # Create blog posts
    for blog_data in sample_blogs:
        blog, created = Blog.objects.get_or_create(
            title=blog_data['title'],
            defaults={
                'content': blog_data['content'],
                'excerpt': blog_data['excerpt'],
                'author': test_user,
                'category': blog_data['category'],
                'is_featured': blog_data['is_featured'],
                'status': 'published',
                'published_at': timezone.now()
            }
        )
        if created:
            # Add tags to the blog
            blog.tags.set(blog_data['tags'])
            print(f"Created blog: {blog.title}")
        else:
            print(f"Blog already exists: {blog.title}")


def main():
    """Main setup function."""
    print("Setting up Django Blog Application...")
    
    # Run migrations
    print("Running migrations...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create superuser
    create_superuser()
    
    # Create sample data
    print("Creating sample data...")
    create_sample_data()
    
    print("Setup completed successfully!")
    print("\nYou can now:")
    print("1. Start the server: python manage.py runserver")
    print("2. Access admin panel: http://localhost:8000/admin")
    print("3. API endpoints: http://localhost:8000/api/")


if __name__ == '__main__':
    main() 