---
title: Notification System Design - System Design Challenge
description: Comprehensive solution for notification system design system design challenge
layout: default
parent: Notification System Design
grand_parent: System Design Challenges
---

# Design a Notification System - System Design Challenge

*Comprehensive solution for designing a scalable push notification service, covering delivery mechanisms, user preferences, and global scale.*

## 🎯 **Challenge Overview**

Design a scalable push notification system that can deliver millions of notifications per second across multiple platforms (mobile, web, email) with high reliability and personalization.

### **Key Requirements**
- **Scale**: 10M+ notifications/second across multiple platforms
- **Reliability**: 99.9% delivery success rate
- **Latency**: <5 seconds for critical notifications
- **Personalization**: User preference management
- **Multi-platform**: iOS, Android, Web, Email support

## 🏗️ **RESHADED Framework Solution**

### **Step 1: Requirements & Constraints**

#### **Functional Requirements**
- **Notification Delivery**: Send to multiple platforms
- **User Preferences**: Manage notification settings
- **Templates**: Reusable notification templates
- **Scheduling**: Delayed and recurring notifications
- **Analytics**: Delivery tracking and engagement metrics

#### **Non-Functional Requirements**
- **Scalability**: Handle millions of notifications per second
- **Reliability**: High delivery success rate
- **Performance**: Low latency delivery
- **Availability**: 99.99% uptime
- **Personalization**: User-specific content and timing

#### **Constraints**
- **Platform Limitations**: Different APIs and rate limits
- **User Privacy**: Respect user preferences and regulations
- **Network Reliability**: Handle mobile network issues
- **Cost**: Minimize delivery costs across platforms

### **Step 2: Estimation & Scale**

#### **Capacity Planning**
```
Daily Active Users: 100M
Notifications per User: 10/day average
Total Daily Notifications: 100M × 10 = 1B/day
Peak Hour Notifications: 1B × 0.15 = 150M/hour
Peak Minute Notifications: 150M ÷ 60 = 2.5M/minute
Peak Second Notifications: 2.5M ÷ 60 = 42K/second

Platform Distribution:
- iOS: 40% = 16.8K/second
- Android: 35% = 14.7K/second
- Web: 15% = 6.3K/second
- Email: 10% = 4.2K/second

Storage Requirements:
- User Preferences: 100M × 2KB = 200GB
- Notification History: 1B × 1KB = 1TB/day
- Templates: 10K × 10KB = 100MB
```

#### **Peak Load Estimation**
```
Peak Factor: 5x normal load
Peak Notifications: 210K/second
Peak Storage: 5TB/day

Geographic Distribution:
- North America: 40%
- Europe: 30%
- Asia: 20%
- Others: 10%
```

### **Step 3: System Interface Design**

#### **API Design**
```python
# Core Operations
send_notification(user_id, template_id, data) -> notification_id
send_bulk_notifications(user_ids[], template_id, data) -> [notification_id]
schedule_notification(user_id, template_id, data, schedule_time) -> notification_id

# User Preferences
update_preferences(user_id, preferences) -> success
get_preferences(user_id) -> preferences
subscribe_topic(user_id, topic) -> success
unsubscribe_topic(user_id, topic) -> success

# Analytics
get_delivery_status(notification_id) -> status
get_user_engagement(user_id) -> metrics
get_template_performance(template_id) -> analytics
```

#### **Data Models**
```json
{
  "notification": {
    "id": "notif_123456",
    "user_id": "user_789",
    "template_id": "welcome_email",
    "platform": "ios",
    "title": "Welcome to our app!",
    "body": "Thank you for joining us.",
    "data": {
      "deep_link": "app://welcome",
      "image_url": "https://example.com/welcome.jpg"
    },
    "scheduled_at": "2024-01-01T10:00:00Z",
    "status": "pending"
  },
  "user_preferences": {
    "user_id": "user_789",
    "platforms": {
      "ios": {
        "enabled": true,
        "quiet_hours": {
          "start": "22:00",
          "end": "08:00"
        },
        "categories": {
          "marketing": false,
          "transactional": true,
          "promotional": false
        }
      }
    },
    "topics": ["news", "updates", "offers"]
  }
}
```

### **Step 4: High-Level Architecture**

```
┌─────────────────────────────────────────────────────────┐
│                Client Applications                      │
├─────────────────────────────────────────────────────────┤
│                    Load Balancer                        │
├─────────────────────────────────────────────────────────┤
│              API Gateway / Notification Service          │
├─────────────────────────────────────────────────────────┤
│              Notification Processing Pipeline            │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   iOS       │  │  Android    │  │    Web      │     │
│  │  Service    │  │  Service    │  │   Service   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Email     │  │  SMS        │  │  In-App     │     │
│  │  Service    │  │  Service    │  │  Service    │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│              User Preferences & Analytics               │
├─────────────────────────────────────────────────────────┤
│              Storage Layer (Notifications, Preferences) │
└─────────────────────────────────────────────────────────┘
```

### **Step 5: Application Layer Design**

#### **Notification Processing Pipeline**
```python
class NotificationPipeline:
    def __init__(self):
        self.preference_checker = UserPreferenceChecker()
        self.template_engine = TemplateEngine()
        self.platform_router = PlatformRouter()
        self.analytics_tracker = AnalyticsTracker()
    
    def process_notification(self, notification_request):
        # 1. Validate request
        self._validate_request(notification_request)
        
        # 2. Check user preferences
        if not self.preference_checker.should_send(notification_request):
            return {"status": "skipped", "reason": "user_preference"}
        
        # 3. Render template
        rendered_content = self.template_engine.render(
            notification_request.template_id,
            notification_request.data
        )
        
        # 4. Route to appropriate platform
        platform_service = self.platform_router.get_service(
            notification_request.platform
        )
        
        # 5. Send notification
        delivery_result = platform_service.send(rendered_content)
        
        # 6. Track analytics
        self.analytics_tracker.track_delivery(delivery_result)
        
        return delivery_result
```

#### **Platform-Specific Services**
```python
class IOSNotificationService:
    def __init__(self):
        self.apns_client = APNSClient()
        self.rate_limiter = RateLimiter(limit=1000, window=60)
    
    def send(self, notification):
        # Check rate limits
        if not self.rate_limiter.allow_request():
            raise RateLimitExceeded()
        
        # Format for APNS
        apns_payload = self._format_for_apns(notification)
        
        # Send via APNS
        response = self.apns_client.send(apns_payload)
        
        return {
            "status": "delivered" if response.success else "failed",
            "message_id": response.message_id,
            "error": response.error
        }
    
    def _format_for_apns(self, notification):
        return {
            "aps": {
                "alert": {
                    "title": notification.title,
                    "body": notification.body
                },
                "badge": 1,
                "sound": "default",
                "data": notification.data
            }
        }

class AndroidNotificationService:
    def __init__(self):
        self.fcm_client = FCMClient()
        self.retry_policy = RetryPolicy(max_retries=3)
    
    def send(self, notification):
        # Format for FCM
        fcm_payload = self._format_for_fcm(notification)
        
        # Send with retry policy
        response = self.retry_policy.execute(
            lambda: self.fcm_client.send(fcm_payload)
        )
        
        return {
            "status": "delivered" if response.success else "failed",
            "message_id": response.message_id,
            "error": response.error
        }
```

#### **User Preference Management**
```python
class UserPreferenceChecker:
    def __init__(self):
        self.preference_cache = LRUCache(max_size=1000000)
        self.preference_db = PreferenceDatabase()
    
    def should_send(self, notification_request):
        # Get user preferences
        preferences = self._get_user_preferences(notification_request.user_id)
        
        # Check if notifications are enabled
        if not preferences.platforms[notification_request.platform].enabled:
            return False
        
        # Check quiet hours
        if self._is_in_quiet_hours(preferences, notification_request.platform):
            return False
        
        # Check category preferences
        if not preferences.categories[notification_request.category]:
            return False
        
        # Check topic subscriptions
        if not self._is_topic_subscribed(preferences, notification_request.topic):
            return False
        
        return True
    
    def _get_user_preferences(self, user_id):
        # Check cache first
        if user_id in self.preference_cache:
            return self.preference_cache[user_id]
        
        # Get from database
        preferences = self.preference_db.get_preferences(user_id)
        
        # Cache for future use
        self.preference_cache[user_id] = preferences
        
        return preferences
```

### **Step 6: Data Layer Design**

#### **Notification Storage**
```python
class NotificationStorage:
    def __init__(self):
        self.notification_db = NotificationDatabase()
        self.template_db = TemplateDatabase()
        self.analytics_db = AnalyticsDatabase()
    
    def store_notification(self, notification):
        # Store notification record
        notification_id = self.notification_db.insert(notification)
        
        # Store analytics data
        self.analytics_db.track_notification_created(notification)
        
        return notification_id
    
    def update_delivery_status(self, notification_id, status):
        # Update notification status
        self.notification_db.update_status(notification_id, status)
        
        # Track delivery analytics
        self.analytics_db.track_delivery_status(notification_id, status)
    
    def get_user_notifications(self, user_id, limit=50):
        return self.notification_db.get_by_user(user_id, limit)
```

#### **Template Engine**
```python
class TemplateEngine:
    def __init__(self):
        self.template_cache = LRUCache(max_size=10000)
        self.template_db = TemplateDatabase()
    
    def render(self, template_id, data):
        # Get template from cache or database
        template = self._get_template(template_id)
        
        # Render template with data
        rendered_content = self._render_template(template, data)
        
        return rendered_content
    
    def _get_template(self, template_id):
        if template_id in self.template_cache:
            return self.template_cache[template_id]
        
        template = self.template_db.get_template(template_id)
        self.template_cache[template_id] = template
        
        return template
    
    def _render_template(self, template, data):
        # Simple template rendering
        rendered = template.content
        
        for key, value in data.items():
            placeholder = "{{" + key + "}}"
            rendered = rendered.replace(placeholder, str(value))
        
        return rendered
```

### **Step 7: Error Handling & Edge Cases**

#### **Delivery Failure Handling**
```python
class DeliveryFailureHandler:
    def __init__(self):
        self.retry_queue = RetryQueue()
        self.dead_letter_queue = DeadLetterQueue()
        self.max_retries = 3
    
    def handle_delivery_failure(self, notification, error):
        # Check if we should retry
        if notification.retry_count < self.max_retries:
            # Schedule retry with exponential backoff
            retry_delay = 2 ** notification.retry_count  # 1s, 2s, 4s
            self.retry_queue.schedule_retry(notification, retry_delay)
        else:
            # Move to dead letter queue
            self.dead_letter_queue.add(notification, error)
    
    def process_retry_queue(self):
        while True:
            notification = self.retry_queue.get_next_retry()
            if notification:
                # Attempt to send again
                result = self._send_notification(notification)
                if not result.success:
                    self.handle_delivery_failure(notification, result.error)
            else:
                time.sleep(1)  # Wait before checking again
```

#### **Rate Limiting and Throttling**
```python
class RateLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.requests = []
    
    def allow_request(self):
        current_time = time.time()
        
        # Remove old requests outside the window
        self.requests = [req for req in self.requests 
                        if current_time - req < self.window]
        
        # Check if we're under the limit
        if len(self.requests) < self.limit:
            self.requests.append(current_time)
            return True
        
        return False

class ThrottlingManager:
    def __init__(self):
        self.user_throttles = {}
        self.global_throttle = RateLimiter(limit=10000, window=60)
    
    def should_throttle(self, user_id, notification_type):
        # Check global throttle
        if not self.global_throttle.allow_request():
            return True
        
        # Check user-specific throttle
        user_key = f"{user_id}:{notification_type}"
        if user_key not in self.user_throttles:
            self.user_throttles[user_key] = RateLimiter(limit=10, window=60)
        
        return not self.user_throttles[user_key].allow_request()
```

### **Step 8: Deployment & Monitoring**

#### **Deployment Architecture**
```yaml
# Kubernetes Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: notification-service
spec:
  replicas: 10
  selector:
    matchLabels:
      app: notification-service
  template:
    metadata:
      labels:
        app: notification-service
    spec:
      containers:
      - name: notification-service
        image: notification-service:latest
        ports:
        - containerPort: 8080
        env:
        - name: REDIS_URL
          value: "redis://redis:6379"
        - name: DATABASE_URL
          value: "postgresql://user:pass@db:5432/notifications"
        resources:
          requests:
            memory: "1Gi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "1000m"
```

#### **Monitoring & Observability**
```python
class NotificationMonitoring:
    def __init__(self):
        self.metrics = {
            'notifications_sent': Counter(),
            'delivery_success_rate': Gauge(),
            'delivery_latency': Histogram(),
            'platform_errors': Counter(),
            'user_engagement': Counter()
        }
    
    def track_notification_sent(self, platform, notification_type):
        self.metrics['notifications_sent'].inc()
    
    def track_delivery_result(self, platform, success, latency):
        if success:
            self.metrics['delivery_success_rate'].set(1.0)
        else:
            self.metrics['delivery_success_rate'].set(0.0)
        
        self.metrics['delivery_latency'].observe(latency)
    
    def track_platform_error(self, platform, error_type):
        self.metrics['platform_errors'].inc()
    
    def track_user_engagement(self, user_id, action):
        self.metrics['user_engagement'].inc()
```

## 📊 **Summary**

### **Building Blocks Used**
1. **Data Storage**: Notification history, user preferences, templates
2. **Compute & Processing**: Template rendering, notification processing
3. **Message Queuing & Streaming**: Notification queues, retry mechanisms
4. **Networking & Communication**: Platform-specific APIs (APNS, FCM)
5. **Caching & Performance**: User preference caching, template caching
6. **Monitoring & Observability**: Delivery tracking, analytics

### **Key Trade-offs**
- **Reliability vs Latency**: Higher reliability requires more retries and delays
- **Personalization vs Performance**: More personalization requires more data processing
- **Platform Support vs Complexity**: Supporting more platforms increases system complexity
- **Analytics vs Privacy**: More detailed analytics may impact user privacy

### **Scalability Considerations**
- **Horizontal Scaling**: Add more notification processing nodes
- **Geographic Distribution**: Place services closer to users for lower latency
- **Platform-Specific Optimization**: Optimize for each platform's requirements
- **Queue Management**: Use message queues for reliable delivery

This design provides a robust, scalable notification system that can handle millions of notifications per second while maintaining high delivery success rates and respecting user preferences.
