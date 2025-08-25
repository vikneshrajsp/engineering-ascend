# System Design Challenges

> 40+ detailed system design challenges with comprehensive solutions following the RESHADED framework.

## 🎯 Overview

This collection contains detailed solutions to real-world system design challenges commonly asked in senior software engineer interviews at top tech companies. Each challenge follows a structured approach and includes trade-off analysis, scalability considerations, and implementation details.

## 🔧 Framework

All challenges follow the **RESHADED** framework:

- **R**equirements & Constraints - Clarify functional and non-functional requirements
- **E**stimation & Scale - Back-of-envelope calculations and capacity planning
- **S**ystem Interface Design - Define APIs and data contracts
- **H**igh-Level Architecture - Overall system design and component interaction
- **A**pplication Layer Design - Business logic and service architecture
- **D**ata Layer Design - Database design and data access patterns
- **E**rror Handling & Edge Cases - Failure scenarios and recovery mechanisms
- **D**eployment & Monitoring - Infrastructure and observability

## 📚 Challenge Categories

### 🔧 **Infrastructure & Core Services**

#### Rate Limiting
- **[Rate Limiter Design](./rate-limiting-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Token bucket, sliding window, distributed rate limiting
  - **Technologies**: Redis, distributed counters, algorithms

#### Data Storage
- **[Key-Value Store Design](./key-value-store-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Distributed storage, consistency models, replication
  - **Technologies**: LSM trees, consistent hashing, consensus protocols

#### ID Generation
- **[Unique ID Generator Design](./unique-id-generator-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Distributed ID generation, clock synchronization, collision avoidance
  - **Technologies**: Snowflake algorithm, UUID, ULID

#### URL Shortening
- **[URL Shortener Design](./url-shortener-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: URL shortening, redirect handling, analytics
  - **Technologies**: Hash functions, caching, analytics tracking

#### Web Crawling
- **[Web Crawler Design](./web-crawler-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Web crawling, politeness policies, distributed crawling
  - **Technologies**: Crawl frontier, robots.txt, content extraction

#### Notifications
- **[Notification System Design](./notification-system-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Push notifications, multi-platform delivery, user preferences
  - **Technologies**: APNS, FCM, email services, message queues

#### News Feed
- **[News Feed System Design](./facebook-feed-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Feed generation, content ranking, real-time updates
  - **Technologies**: Graph databases, ranking algorithms, real-time processing

#### Chat System
- **[Chat System Design](./chat-system-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Real-time messaging, message ordering, group chats
  - **Technologies**: WebSockets, message queues, distributed systems

#### Search Autocomplete
- **[Search Autocomplete Design](./search-autocomplete-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Real-time suggestions, query completion, personalization
  - **Technologies**: Trie data structures, caching, ranking algorithms

#### Video Streaming
- **[Video Streaming Design](./netflix-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Video streaming, content delivery, recommendation
  - **Technologies**: CDN, adaptive bitrate streaming, recommendation systems

#### Cloud Storage
- **[Cloud Storage Design](./gcs-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Multi-region storage, versioning, lifecycle management
  - **Technologies**: Distributed file systems, version control, automated policies

#### Maps Service
- **[Maps Service Design](./google-maps-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Geospatial data, routing algorithms, real-time traffic
  - **Technologies**: Spatial databases, graph algorithms, real-time data

#### Object Storage
- **[Object Storage Design](./aws-s3-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Object storage, consistency, durability
  - **Technologies**: Distributed storage, replication, CDN

#### Search Engine
- **[Search Engine Design](./google-search-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Web crawling, indexing, ranking algorithms
  - **Technologies**: Search engines, distributed indexing, ML ranking

#### Ride Sharing
- **[Ride Sharing Design](./uber-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Real-time location, ride matching, payment processing
  - **Technologies**: GPS, real-time databases, payment gateways

#### Email Service
- **[Email Service Design](./gmail-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Email storage, spam filtering, search capabilities
  - **Technologies**: Distributed databases, search indexing, ML filtering

#### Email System
- **[Email System Design](./email-system-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Email protocols, storage, delivery
  - **Technologies**: SMTP, IMAP, POP3, distributed storage

#### Video Conferencing
- **[Video Conferencing Design](./video-conferencing-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Real-time video, audio processing, screen sharing
  - **Technologies**: WebRTC, media servers, peer-to-peer networking

#### Load Balancer
- **[Load Balancer Design](./load-balancer-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Traffic distribution, health checking, failover
  - **Technologies**: Load balancing algorithms, health monitoring, SSL termination

#### Payment System
- **[Payment System Design](./payment-system-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Payment processing, fraud detection, compliance
  - **Technologies**: Payment gateways, fraud detection, PCI compliance

#### Chat System
- **[Chat System Design](./chat-system-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Real-time messaging, message ordering, group chats
  - **Technologies**: WebSockets, message queues, distributed systems

#### Recommendation System
- **[Recommendation System Design](./recommendation-system-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Collaborative filtering, content-based filtering, ML
  - **Technologies**: ML algorithms, user behavior analysis, A/B testing

#### Distributed Cache
- **[Distributed Cache Design](./distributed-cache-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Cache distribution, consistency, eviction policies
  - **Technologies**: Redis, Memcached, cache invalidation

#### Monitoring & Alerting
- **[Monitoring & Alerting Design](./monitoring-alerting-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Metrics collection, alerting, anomaly detection
  - **Technologies**: Time-series databases, alerting systems, ML

#### Data Warehouse
- **[Data Warehouse Design](./data-warehouse-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Data modeling, ETL processes, analytics
  - **Technologies**: Columnar storage, query optimization, data pipelines

#### BigQuery
- **[BigQuery Design](./bigquery-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Data warehousing, SQL processing, serverless
  - **Technologies**: Columnar storage, distributed query processing

#### CDN
- **[CDN Design](./cdn-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Content delivery, edge caching, global distribution
  - **Technologies**: Edge servers, cache management, geographic routing

#### Telemedicine
- **[Telemedicine Design](./telemedicine-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Video consultations, patient data, compliance
  - **Technologies**: HIPAA compliance, video streaming, secure storage

#### Online Gaming
- **[Online Gaming Design](./online-gaming-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Real-time multiplayer, matchmaking, anti-cheat
  - **Technologies**: Game servers, real-time networking, cheat detection

#### ChatGPT
- **[ChatGPT Design](./chatgpt-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: LLM inference, conversation management, scaling
  - **Technologies**: Transformer models, GPU clusters, conversation storage

#### Leaderboard
- **[Leaderboard Design](./leaderboard-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Real-time rankings, score updates, competition
  - **Technologies**: Sorted sets, real-time updates, caching

### 🎵 **Media & Entertainment**

#### Video Streaming
- **[Video Streaming Design](./netflix-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Video streaming, content delivery, recommendation
  - **Technologies**: CDN, adaptive bitrate streaming, recommendation systems

#### Music Streaming
- **[Music Streaming Design](./spotify-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Audio streaming, playlist management, recommendation
  - **Technologies**: Audio compression, streaming protocols, ML recommendations

#### Music Platform
- **[Music Platform Design](./apple-music-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Music streaming, library sync, cross-platform
  - **Technologies**: Cloud integration, audio streaming, device sync

### 🚗 **Transportation & Services**

#### Ride Sharing
- **[Ride Sharing Design](./uber-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Real-time location, ride matching, payment processing
  - **Technologies**: GPS, real-time databases, payment gateways

#### Maps Service
- **[Maps Service Design](./google-maps-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Geospatial data, routing algorithms, real-time traffic
  - **Technologies**: Spatial databases, graph algorithms, real-time data

### 🛒 **E-commerce & Storage**

#### Object Storage
- **[Object Storage Design](./aws-s3-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Object storage, consistency, durability
  - **Technologies**: Distributed storage, replication, CDN

#### Cloud Storage
- **[Cloud Storage Design](./gcs-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Multi-region storage, versioning, lifecycle management
  - **Technologies**: Distributed file systems, version control, automated policies

### 🔍 **Search & Analytics**

#### Search Engine
- **[Search Engine Design](./google-search-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Web crawling, indexing, ranking algorithms
  - **Technologies**: Search engines, distributed indexing, ML ranking

### 📱 **Social Media & Content**

#### Instagram
- **[Instagram Design](./instagram-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Photo sharing, social networking, content discovery
  - **Technologies**: Image processing, social graphs, recommendation systems

#### Facebook Feed
- **[Facebook Feed Design](./facebook-feed-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Feed generation, content ranking, real-time updates
  - **Technologies**: Graph databases, ranking algorithms, real-time processing

## 📊 Difficulty Levels

### 🟢 **Easy** (0-2 years experience)
- Basic system design concepts
- Single service architecture
- Simple data models
- Basic scalability considerations

### 🟡 **Medium** (2-5 years experience)
- Distributed system concepts
- Multiple service interactions
- Complex data models
- Advanced scalability patterns

### 🔴 **Hard** (5+ years experience)
- Large-scale distributed systems
- Complex system interactions
- Advanced data architectures
- Enterprise-level considerations

## 🎯 Interview Preparation

### **Before the Interview**
1. **Review Building Blocks** - Understand the 8 core components
2. **Practice Estimation** - Master back-of-envelope calculations
3. **Study Patterns** - Learn common architectural patterns
4. **Review Trade-offs** - Understand CAP theorem, consistency vs availability

### **During the Interview**
1. **Clarify Requirements** - Ask clarifying questions
2. **Estimate Scale** - Do quick calculations
3. **Start Simple** - Begin with basic architecture
4. **Iterate** - Add complexity step by step
5. **Discuss Trade-offs** - Explain your decisions

### **Common Pitfalls to Avoid**
- **Over-engineering** - Start simple, add complexity as needed
- **Ignoring Scale** - Always consider scale in your design
- **Forgetting Trade-offs** - Every decision has trade-offs
- **Not Testing** - Consider failure scenarios and edge cases

## 🔗 Related Resources

- **[Building Blocks](../building-blocks/README.md)** - Understand the core components
- **[Quantitative Metrics](../quantitative-metrics.md)** - Learn performance metrics
- **[Back of Envelope Estimation](../back-of-envelope-estimation.md)** - Master quick calculations

## 📈 Success Metrics

Track your progress with these metrics:

- **Challenges Completed**: Aim for 20+ challenges
- **Building Blocks Mastered**: Understand all 8 components
- **Estimation Accuracy**: Practice until you're within 10% of actual numbers
- **Interview Confidence**: Feel prepared for any system design question

---

**Ready to master system design?** Start with any challenge above and build your expertise! 🚀
