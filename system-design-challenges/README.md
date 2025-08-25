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

### 🔗 **Infrastructure & Core Services**

#### URL Shortener
- **[URL Shortener Design](./url-shortener-design.md)**
  - **Difficulty**: Easy
  - **Key Concepts**: Hash generation, database design, caching
  - **Technologies**: Redis, PostgreSQL, CDN

#### Web Crawler
- **[Web Crawler Design](./web-crawler-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Distributed crawling, politeness, deduplication
  - **Technologies**: Queue systems, distributed storage, rate limiting

#### Load Balancer
- **[Load Balancer Design](./load-balancer-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Load distribution algorithms, health checks, session affinity
  - **Technologies**: NGINX, HAProxy, cloud load balancers

#### Rate Limiter
- **[Rate Limiter Design](./rate-limiter-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Token bucket, sliding window, distributed rate limiting
  - **Technologies**: Redis, in-memory counters, distributed coordination

### 💬 **Communication & Social**

#### Chat System
- **[Chat System Design](./chat-system-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Real-time messaging, message ordering, presence
  - **Technologies**: WebSockets, message queues, real-time databases

#### Instagram
- **[Instagram Design](./instagram-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Feed generation, media storage, social graph
  - **Technologies**: CDN, graph databases, recommendation systems

#### Facebook Feed
- **[Facebook Feed Design](./facebook-feed-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: News feed algorithm, social ranking, real-time updates
  - **Technologies**: Graph databases, recommendation engines, caching

#### Gmail
- **[Gmail Design](./gmail-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Email protocols, search, spam filtering
  - **Technologies**: IMAP/SMTP, search engines, ML for spam detection

### 🎵 **Media & Entertainment**

#### Netflix
- **[Netflix Design](./netflix-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Video streaming, content delivery, recommendation
  - **Technologies**: CDN, adaptive bitrate streaming, recommendation systems

#### Spotify
- **[Spotify Design](./spotify-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Audio streaming, playlist management, recommendation
  - **Technologies**: Audio compression, streaming protocols, ML recommendations

#### Apple Music
- **[Apple Music Design](./apple-music-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Music streaming, library sync, cross-platform
  - **Technologies**: iCloud integration, audio streaming, device sync

### 🚗 **Transportation & Services**

#### Uber
- **[Uber Design](./uber-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Real-time location, ride matching, payment processing
  - **Technologies**: GPS, real-time databases, payment gateways

#### Google Maps
- **[Google Maps Design](./google-maps-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Geospatial data, routing algorithms, real-time traffic
  - **Technologies**: Spatial databases, graph algorithms, real-time data

### 🛒 **E-commerce & Storage**

#### Amazon S3
- **[AWS S3 Design](./aws-s3-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Object storage, consistency, durability
  - **Technologies**: Distributed storage, replication, CDN

#### Google Cloud Storage
- **[GCS Design](./gcs-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Multi-region storage, versioning, lifecycle management
  - **Technologies**: Distributed file systems, version control, automated policies

### 🔍 **Search & Analytics**

#### Google Search
- **[Google Search Design](./google-search-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Web crawling, indexing, ranking algorithms
  - **Technologies**: Search engines, distributed indexing, ML ranking

#### BigQuery
- **[BigQuery Design](./bigquery-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Data warehousing, SQL processing, columnar storage
  - **Technologies**: Columnar databases, distributed query processing, data lakes

#### Data Warehouse
- **[Data Warehouse Design](./data-warehouse-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: ETL processes, dimensional modeling, OLAP
  - **Technologies**: Star/snowflake schemas, data pipelines, analytics engines

### 🤖 **AI & Machine Learning**

#### ChatGPT
- **[ChatGPT Design](./chatgpt-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Large language models, inference optimization, conversation management
  - **Technologies**: GPU clusters, model serving, conversation databases

#### Recommendation System
- **[Recommendation System Design](./recommendation-system-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Collaborative filtering, content-based filtering, hybrid approaches
  - **Technologies**: ML pipelines, feature stores, A/B testing

### 💳 **Finance & Payments**

#### Payment System
- **[Payment System Design](./payment-system-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Payment processing, fraud detection, compliance
  - **Technologies**: Payment gateways, fraud detection ML, compliance systems

### 🏥 **Healthcare & Services**

#### Telemedicine
- **[Telemedicine Design](./telemedicine-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Video conferencing, HIPAA compliance, appointment scheduling
  - **Technologies**: WebRTC, secure video, compliance frameworks

### 🎮 **Gaming & Entertainment**

#### Online Gaming
- **[Online Gaming Design](./online-gaming-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Real-time gaming, matchmaking, anti-cheat
  - **Technologies**: Game servers, real-time networking, cheat detection

#### Leaderboard
- **[Leaderboard Design](./leaderboard-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Real-time ranking, high-frequency updates, global vs local
  - **Technologies**: Sorted sets, real-time updates, caching

### 🏗️ **Infrastructure & Tools**

#### CDN
- **[CDN Design](./cdn-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Content distribution, edge caching, origin servers
  - **Technologies**: Edge servers, cache invalidation, geographic distribution

#### Distributed Cache
- **[Distributed Cache Design](./distributed-cache-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Cache consistency, partitioning, failover
  - **Technologies**: Redis Cluster, Memcached, cache invalidation

#### Monitoring & Alerting
- **[Monitoring & Alerting Design](./monitoring-alerting-design.md)**
  - **Difficulty**: Medium
  - **Key Concepts**: Metrics collection, alerting rules, incident management
  - **Technologies**: Time-series databases, alerting systems, incident response

#### Email System
- **[Email System Design](./email-system-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Email protocols, spam filtering, delivery optimization
  - **Technologies**: SMTP/IMAP, spam detection, email routing

#### Video Conferencing
- **[Video Conferencing Design](./video-conferencing-design.md)**
  - **Difficulty**: Hard
  - **Key Concepts**: Real-time video, audio processing, room management
  - **Technologies**: WebRTC, media servers, real-time communication

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
