---
title: Search Autocomplete Design - System Design Challenge
description: Comprehensive solution for search autocomplete design system design challenge
layout: default
parent: Search Autocomplete Design
grand_parent: System Design Challenges
---

# Design a Search Autocomplete System - System Design Challenge

*Comprehensive solution for designing a search autocomplete system, covering real-time suggestions, ranking algorithms, and global scale.*

## 🎯 **Challenge Overview**

Design a search autocomplete system that provides real-time suggestions as users type, with intelligent ranking and personalization for millions of users.

### **Key Requirements**
- **Scale**: 100M+ daily searches, 10K+ suggestions/second
- **Latency**: <100ms response time for suggestions
- **Relevance**: High-quality, personalized suggestions
- **Real-time**: Suggestions update as user types
- **Multi-language**: Support for multiple languages

## 🏗️ **RESHADED Framework Solution**

### **Step 1: Requirements & Constraints**

#### **Functional Requirements**
- **Real-time Suggestions**: Show suggestions as user types
- **Query Completion**: Complete partial queries
- **Popular Queries**: Show trending and popular searches
- **Personalization**: User-specific suggestions based on history
- **Multi-language**: Support for different languages and locales

#### **Non-Functional Requirements**
- **Scalability**: Handle millions of search queries per day
- **Performance**: Low latency response times
- **Availability**: High availability across regions
- **Accuracy**: Relevant and useful suggestions
- **Freshness**: Real-time updates for trending queries

#### **Constraints**
- **Network Latency**: Minimize round-trip time for suggestions
- **Storage**: Efficient storage of query data and indexes
- **Memory**: Fast access to frequently used data
- **Cost**: Minimize infrastructure costs

### **Step 2: Estimation & Scale**

#### **Capacity Planning**
```
Daily Active Users: 50M
Searches per User: 10/day average
Total Daily Searches: 50M × 10 = 500M/day
Peak Hour Searches: 500M × 0.15 = 75M/hour
Peak Minute Searches: 75M ÷ 60 = 1.25M/minute
Peak Second Searches: 1.25M ÷ 60 = 21K/second

Suggestions per Search: 10 suggestions average
Peak Suggestions: 21K × 10 = 210K/second

Storage Requirements:
- Query History: 500M × 100 bytes = 50GB/day
- User Preferences: 50M × 2KB = 100GB
- Query Indexes: 1M unique queries × 1KB = 1GB
- Trending Data: 10K trending queries × 1KB = 10MB
```

#### **Peak Load Estimation**
```
Peak Factor: 3x normal load
Peak Searches: 63K/second
Peak Suggestions: 630K/second

Geographic Distribution:
- North America: 40%
- Europe: 30%
- Asia: 20%
- Others: 10%

Query Length Distribution:
- 1-3 characters: 20%
- 4-6 characters: 40%
- 7-10 characters: 30%
- 10+ characters: 10%
```

### **Step 3: System Interface Design**

#### **API Design**
```python
# Core Operations
get_suggestions(query, user_id=None, limit=10) -> [suggestion]
get_trending_queries(category=None, limit=20) -> [query]
get_personalized_suggestions(user_id, query, limit=10) -> [suggestion]

# User Management
update_user_preferences(user_id, preferences) -> success
get_user_search_history(user_id, limit=50) -> [query]
clear_user_history(user_id) -> success

# Analytics
track_query(query, user_id, selected_suggestion=None) -> success
get_query_analytics(query, time_range) -> analytics
```

#### **Data Models**
```json
{
  "suggestion": {
    "query": "machine learning",
    "score": 0.95,
    "type": "completion",
    "metadata": {
      "frequency": 15000,
      "click_rate": 0.12,
      "conversion_rate": 0.08,
      "last_updated": "2024-01-01T12:00:00Z"
    }
  },
  "user_preferences": {
    "user_id": "user_123",
    "language": "en",
    "region": "US",
    "interests": ["technology", "science"],
    "search_history": [
      {
        "query": "python tutorial",
        "timestamp": "2024-01-01T10:00:00Z",
        "selected_suggestion": "python tutorial for beginners"
      }
    ]
  },
  "trending_query": {
    "query": "artificial intelligence",
    "trend_score": 0.98,
    "category": "technology",
    "growth_rate": 0.25,
    "geographic_distribution": {
      "US": 0.4,
      "EU": 0.3,
      "Asia": 0.2,
      "Others": 0.1
    }
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
│              API Gateway / Autocomplete Service         │
├─────────────────────────────────────────────────────────┤
│              Suggestion Processing Pipeline              │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Query     │  │  Trending   │  │Personalized │     │
│  │ Completion  │  │  Queries    │  │ Suggestions │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│              Ranking & Scoring Engine                   │
├─────────────────────────────────────────────────────────┤
│              Cache Layer (Redis)                        │
├─────────────────────────────────────────────────────────┤
│              Search Index (Elasticsearch)               │
├─────────────────────────────────────────────────────────┤
│              Analytics & Learning Pipeline              │
└─────────────────────────────────────────────────────────┘
```

### **Step 5: Application Layer Design**

#### **Suggestion Processing Pipeline**
```python
class AutocompletePipeline:
    def __init__(self):
        self.query_completer = QueryCompleter()
        self.trending_service = TrendingService()
        self.personalization_service = PersonalizationService()
        self.ranking_engine = RankingEngine()
        self.cache_service = CacheService()
    
    def get_suggestions(self, query, user_id=None, limit=10):
        # 1. Check cache first
        cache_key = f"suggestions:{query}:{user_id}"
        cached_suggestions = self.cache_service.get(cache_key)
        if cached_suggestions:
            return cached_suggestions[:limit]
        
        # 2. Get query completions
        completions = self.query_completer.get_completions(query)
        
        # 3. Get trending queries
        trending = self.trending_service.get_trending_queries(query)
        
        # 4. Get personalized suggestions
        personalized = []
        if user_id:
            personalized = self.personalization_service.get_suggestions(user_id, query)
        
        # 5. Combine and rank suggestions
        all_suggestions = completions + trending + personalized
        ranked_suggestions = self.ranking_engine.rank_suggestions(
            all_suggestions, query, user_id
        )
        
        # 6. Cache results
        self.cache_service.set(cache_key, ranked_suggestions, ttl=300)
        
        # 7. Track analytics
        self._track_query(query, user_id)
        
        return ranked_suggestions[:limit]
```

#### **Query Completion Engine**
```python
class QueryCompleter:
    def __init__(self):
        self.trie = Trie()
        self.query_index = QueryIndex()
    
    def get_completions(self, prefix):
        # Get completions from trie
        trie_completions = self.trie.get_completions(prefix)
        
        # Get completions from search index
        index_completions = self.query_index.search_prefix(prefix)
        
        # Combine and deduplicate
        all_completions = list(set(trie_completions + index_completions))
        
        return all_completions
    
    def update_trie(self, new_queries):
        for query in new_queries:
            self.trie.insert(query)
    
    def get_popular_completions(self, prefix, limit=10):
        completions = self.get_completions(prefix)
        
        # Sort by popularity
        sorted_completions = sorted(
            completions,
            key=lambda x: x.metadata.frequency,
            reverse=True
        )
        
        return sorted_completions[:limit]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.word = word
    
    def get_completions(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        
        return self._get_all_words(node, prefix)
    
    def _get_all_words(self, node, prefix):
        words = []
        if node.is_end:
            words.append(prefix)
        
        for char, child in node.children.items():
            words.extend(self._get_all_words(child, prefix + char))
        
        return words
```

#### **Trending Queries Service**
```python
class TrendingService:
    def __init__(self):
        self.trending_cache = {}
        self.trending_analyzer = TrendingAnalyzer()
        self.update_interval = 300  # 5 minutes
    
    def get_trending_queries(self, query=None, limit=10):
        # Get trending queries from cache
        trending_queries = self._get_cached_trending()
        
        # Filter by query if provided
        if query:
            trending_queries = self._filter_by_query(trending_queries, query)
        
        # Sort by trend score
        sorted_queries = sorted(
            trending_queries,
            key=lambda x: x.trend_score,
            reverse=True
        )
        
        return sorted_queries[:limit]
    
    def update_trending_queries(self):
        # Analyze recent queries for trends
        recent_queries = self._get_recent_queries()
        trending_queries = self.trending_analyzer.analyze_trends(recent_queries)
        
        # Update cache
        self.trending_cache = trending_queries
    
    def _get_cached_trending(self):
        if not self.trending_cache:
            self.update_trending_queries()
        return self.trending_cache

class TrendingAnalyzer:
    def __init__(self):
        self.time_windows = [1, 6, 24]  # hours
    
    def analyze_trends(self, queries):
        trending_queries = []
        
        for query in queries:
            trend_score = self._calculate_trend_score(query)
            if trend_score > 0.5:  # Threshold for trending
                trending_queries.append({
                    'query': query.text,
                    'trend_score': trend_score,
                    'growth_rate': self._calculate_growth_rate(query),
                    'category': query.category
                })
        
        return trending_queries
    
    def _calculate_trend_score(self, query):
        # Calculate trend score based on frequency increase
        current_freq = query.get_frequency(1)  # Last hour
        previous_freq = query.get_frequency(6)  # Last 6 hours
        
        if previous_freq == 0:
            return 0
        
        growth_rate = (current_freq - previous_freq) / previous_freq
        return min(growth_rate, 1.0)  # Cap at 1.0
```

#### **Personalization Service**
```python
class PersonalizationService:
    def __init__(self):
        self.user_profiles = UserProfileManager()
        self.collaborative_filter = CollaborativeFilter()
        self.ml_model = MLModel()
    
    def get_suggestions(self, user_id, query, limit=10):
        # Get user profile
        user_profile = self.user_profiles.get_profile(user_id)
        
        # Get collaborative filtering suggestions
        cf_suggestions = self.collaborative_filter.get_suggestions(user_id, query)
        
        # Get ML-based suggestions
        ml_suggestions = self.ml_model.predict_suggestions(user_profile, query)
        
        # Combine and rank
        all_suggestions = cf_suggestions + ml_suggestions
        personalized_suggestions = self._rank_by_personalization(
            all_suggestions, user_profile
        )
        
        return personalized_suggestions[:limit]
    
    def _rank_by_personalization(self, suggestions, user_profile):
        for suggestion in suggestions:
            # Calculate personalization score
            personalization_score = self._calculate_personalization_score(
                suggestion, user_profile
            )
            suggestion.personalization_score = personalization_score
        
        # Sort by personalization score
        return sorted(suggestions, key=lambda x: x.personalization_score, reverse=True)
    
    def _calculate_personalization_score(self, suggestion, user_profile):
        score = 0
        
        # Interest matching
        if suggestion.category in user_profile.interests:
            score += 0.3
        
        # Historical preference
        if suggestion.query in user_profile.search_history:
            score += 0.2
        
        # Similar user behavior
        if suggestion.query in user_profile.similar_users_queries:
            score += 0.2
        
        # Recency
        if suggestion.is_recent:
            score += 0.1
        
        return min(score, 1.0)
```

### **Step 6: Data Layer Design**

#### **Search Index (Elasticsearch)**
```python
class QueryIndex:
    def __init__(self):
        self.es_client = ElasticsearchClient()
        self.index_name = "autocomplete_queries"
    
    def search_prefix(self, prefix, limit=20):
        # Search for queries starting with prefix
        query = {
            "query": {
                "prefix": {
                    "query_text": {
                        "value": prefix.lower(),
                        "boost": 1.0
                    }
                }
            },
            "sort": [
                {"frequency": {"order": "desc"}},
                {"click_rate": {"order": "desc"}}
            ],
            "size": limit
        }
        
        response = self.es_client.search(self.index_name, query)
        
        return [self._parse_hit(hit) for hit in response['hits']['hits']]
    
    def index_query(self, query_data):
        # Index new query data
        document = {
            "query_text": query_data.query.lower(),
            "frequency": query_data.frequency,
            "click_rate": query_data.click_rate,
            "conversion_rate": query_data.conversion_rate,
            "category": query_data.category,
            "last_updated": query_data.timestamp
        }
        
        self.es_client.index(self.index_name, document)
    
    def _parse_hit(self, hit):
        return {
            "query": hit["_source"]["query_text"],
            "score": hit["_score"],
            "metadata": {
                "frequency": hit["_source"]["frequency"],
                "click_rate": hit["_source"]["click_rate"]
            }
        }
```

#### **Cache Layer (Redis)**
```python
class CacheService:
    def __init__(self):
        self.redis_client = RedisClient()
        self.default_ttl = 300  # 5 minutes
    
    def get(self, key):
        try:
            value = self.redis_client.get(key)
            return json.loads(value) if value else None
        except Exception:
            return None
    
    def set(self, key, value, ttl=None):
        try:
            ttl = ttl or self.default_ttl
            serialized_value = json.dumps(value)
            self.redis_client.setex(key, ttl, serialized_value)
            return True
        except Exception:
            return False
    
    def get_suggestions_cache_key(self, query, user_id=None):
        # Create cache key for suggestions
        if user_id:
            return f"suggestions:{query}:{user_id}"
        else:
            return f"suggestions:{query}:anonymous"
    
    def invalidate_user_cache(self, user_id):
        # Invalidate all cached suggestions for a user
        pattern = f"suggestions:*:{user_id}"
        keys = self.redis_client.keys(pattern)
        if keys:
            self.redis_client.delete(*keys)
```

### **Step 7: Error Handling & Edge Cases**

#### **Query Processing Errors**
```python
class QueryErrorHandler:
    def __init__(self):
        self.fallback_service = FallbackService()
        self.error_tracker = ErrorTracker()
    
    def handle_query_error(self, query, error):
        # Log error
        self.error_tracker.track_error(query, error)
        
        # Return fallback suggestions
        fallback_suggestions = self.fallback_service.get_suggestions(query)
        
        return {
            "suggestions": fallback_suggestions,
            "error": str(error),
            "fallback_used": True
        }
    
    def handle_empty_results(self, query):
        # Return popular queries when no suggestions found
        popular_queries = self.fallback_service.get_popular_queries()
        
        return {
            "suggestions": popular_queries,
            "message": "No specific suggestions found",
            "fallback_used": True
        }

class FallbackService:
    def __init__(self):
        self.popular_queries = [
            "how to", "what is", "best", "top", "guide"
        ]
    
    def get_suggestions(self, query):
        # Return generic suggestions based on query
        if len(query) < 2:
            return self.get_popular_queries()
        
        # Return query with common suffixes
        suffixes = [" tutorial", " guide", " examples", " tips"]
        suggestions = [query + suffix for suffix in suffixes]
        
        return suggestions[:5]
    
    def get_popular_queries(self):
        return self.popular_queries
```

#### **Performance Optimization**
```python
class PerformanceOptimizer:
    def __init__(self):
        self.query_length_threshold = 2
        self.cache_hit_threshold = 0.8
    
    def should_process_query(self, query):
        # Skip very short queries
        if len(query.strip()) < self.query_length_threshold:
            return False
        
        return True
    
    def optimize_suggestions(self, suggestions, query_length):
        # Adjust number of suggestions based on query length
        if query_length <= 3:
            return suggestions[:5]  # Fewer suggestions for short queries
        elif query_length <= 6:
            return suggestions[:8]  # Medium suggestions
        else:
            return suggestions[:10]  # More suggestions for longer queries
    
    def should_cache(self, query, user_id):
        # Cache more aggressively for anonymous users
        if not user_id:
            return True
        
        # Cache based on query frequency
        query_frequency = self._get_query_frequency(query)
        return query_frequency > 100  # Cache popular queries
```

### **Step 8: Deployment & Monitoring**

#### **Deployment Architecture**
```yaml
# Kubernetes Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: autocomplete-service
spec:
  replicas: 5
  selector:
    matchLabels:
      app: autocomplete-service
  template:
    metadata:
      labels:
        app: autocomplete-service
    spec:
      containers:
      - name: autocomplete-service
        image: autocomplete-service:latest
        ports:
        - containerPort: 8080
        env:
        - name: ELASTICSEARCH_URL
          value: "http://elasticsearch:9200"
        - name: REDIS_URL
          value: "redis://redis:6379"
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
class AutocompleteMonitoring:
    def __init__(self):
        self.metrics = {
            'queries_per_second': Counter(),
            'suggestion_latency': Histogram(),
            'cache_hit_rate': Gauge(),
            'suggestion_accuracy': Gauge(),
            'error_rate': Counter()
        }
    
    def track_query(self, query, latency, cache_hit):
        self.metrics['queries_per_second'].inc()
        self.metrics['suggestion_latency'].observe(latency)
        
        if cache_hit:
            self.metrics['cache_hit_rate'].set(1.0)
        else:
            self.metrics['cache_hit_rate'].set(0.0)
    
    def track_suggestion_click(self, query, selected_suggestion):
        # Track suggestion accuracy
        accuracy = self._calculate_accuracy(query, selected_suggestion)
        self.metrics['suggestion_accuracy'].set(accuracy)
    
    def track_error(self, error_type):
        self.metrics['error_rate'].inc()
    
    def _calculate_accuracy(self, query, selected_suggestion):
        # Simple accuracy calculation
        if query.lower() in selected_suggestion.lower():
            return 1.0
        elif len(set(query.lower()) & set(selected_suggestion.lower())) > 0:
            return 0.5
        else:
            return 0.0
```

## 📊 **Summary**

### **Building Blocks Used**
1. **Data Storage**: Query indexes, user profiles, search history
2. **Compute & Processing**: Query completion, trending analysis, personalization
3. **Caching & Performance**: Redis caching, trie data structure
4. **Networking & Communication**: Real-time API responses
5. **Monitoring & Observability**: Query analytics, performance metrics

### **Key Trade-offs**
- **Accuracy vs Speed**: More accurate suggestions require more processing time
- **Personalization vs Privacy**: More personalization requires more user data
- **Cache Size vs Memory**: Larger cache improves performance but uses more memory
- **Real-time vs Freshness**: Real-time updates may impact performance

### **Scalability Considerations**
- **Horizontal Scaling**: Add more autocomplete service instances
- **Geographic Distribution**: Place services closer to users for lower latency
- **Cache Optimization**: Use distributed caching for better performance
- **Index Optimization**: Optimize search indexes for faster queries

This design provides a robust, scalable autocomplete system that can handle millions of queries per day while providing relevant, personalized suggestions in real-time.
