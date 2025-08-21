# Data Storage Systems - Cheat Sheet
## One-Page Quick Reference for Interviews

## 🏗️ **STORAGE TYPE SELECTION**

```
Linearizability Required? → RDBMS (MySQL, PostgreSQL)
High Throughput? → Key-Value (Redis, DynamoDB)
Analytics/OLAP? → Wide Column (Cassandra, HBase)
Time Series Data? → InfluxDB, TimescaleDB
Full-Text Search? → Elasticsearch, Solr
Large Binary Files? → Object Store (S3, GCS)
Flexible Schema? → Document Store (MongoDB)
```

---

## 📊 **QUICK COMPARISON TABLE**

| Storage | Linearizability | Scaling | Query | Throughput | Use Case |
|---------|-----------------|---------|-------|------------|----------|
| **RDBMS** | ✅ | ❌ | ✅ | ⚠️ | ACID Transactions |
| **Key-Value** | ⚠️ | ✅ | ❌ | ✅ | Simple Lookups |
| **Wide Column** | ❌ | ✅ | ⚠️ | ✅ | Analytics/OLAP |
| **Document** | ❌ | ✅ | ✅ | ✅ | Flexible Data |
| **Time Series** | ❌ | ✅ | ⚠️ | ✅ | Time-Series Data |
| **Text Search** | ❌ | ✅ | ⚠️ | ✅ | Full-Text Search |
| **Object Store** | ❌ | ✅ | ❌ | ⚠️ | Large Binary Files |

---

## 🔍 **INDEXING QUICK REFERENCE**

### **In-Memory Indexes**
- **Hash Tables**: O(1) lookup, no ordering
- **B-Trees**: O(log n), ordered, range queries
- **Skip Lists**: O(log n), ordered, concurrent

### **On-Disk Indexes**
- **B-Tree**: Balanced, good read/write
- **LSM Tree**: Write-optimized, background compaction
- **Bitmap**: Boolean operations, compression

---

## 🚀 **SCALING PATTERNS**

### **Horizontal (Scale Out)**
- **Hash-based Sharding**: Even distribution, consistent hashing
- **Range-based Sharding**: Efficient range queries, potential hotspots
- **Leader-Follower Replication**: Primary for writes, replicas for reads
- **Multi-Master Replication**: Multiple write nodes, conflict resolution
- **Auto-scaling**: Automatic instance management based on load

### **Vertical (Scale Up)**
- **CPU**: Multi-core utilization, hyper-threading, CPU affinity
- **Memory**: Larger RAM, memory hierarchy optimization, NUMA awareness
- **Storage**: SSD/NVMe drives, RAID configurations, storage tiering
- **Network**: Higher bandwidth, lower latency, network optimization

---

## ⚖️ **CONSISTENCY MODELS**

### **Strong Consistency**
- **Linearizability**: All operations appear atomic with global ordering
- **Sequential Consistency**: Operations appear in some sequential order
- **Causal Consistency**: Causally related operations appear in order
- **Use**: Financial transactions, user accounts, critical data

### **Eventual Consistency**
- **Monotonic Reads**: Reads never go backwards in time
- **Monotonic Writes**: Writes appear in order for same client
- **Read-Your-Writes**: Client sees own writes immediately
- **Use**: Social media feeds, content delivery, non-critical data

---

## 📈 **PERFORMANCE OPTIMIZATION**

### **Read-Heavy Workloads**
- Read replicas, caching layers, B-tree indexing
- Performance: 1-10ms latency, 10K-100K ops/sec throughput

### **Write-Heavy Workloads**
- Write buffering, LSM trees, async processing
- Performance: 1-100ms latency, 1K-100K ops/sec throughput

### **Mixed Workloads**
- Read/write separation, caching layers, background processing
- Performance: 5-50ms latency, 5K-50K ops/sec throughput

---

## 🔧 **COMMON IMPLEMENTATIONS**

### **RDBMS**
- **MySQL**: Web apps, high availability
- **PostgreSQL**: Complex queries, ACID
- **Oracle**: Enterprise, high performance

### **NoSQL**
- **MongoDB**: Document store, flexible
- **Cassandra**: Wide column, high availability
- **Redis**: Key-value, in-memory
- **Elasticsearch**: Text search, analytics

### **Specialized**
- **InfluxDB**: Time series data
- **S3**: Object storage, cloud-native
- **DynamoDB**: Managed NoSQL, auto-scaling

---

## 🎯 **INTERVIEW QUICK TIPS**

### **When Asked About Storage:**
1. **Clarify requirements**: ACID, scale, performance
2. **Consider access patterns**: Read vs write heavy
3. **Think about consistency**: Strong vs eventual
4. **Plan for scaling**: Horizontal vs vertical
5. **Consider operational complexity**: Team expertise

### **Common Trade-offs:**
- **Consistency vs Performance**: ACID vs speed
- **Complexity vs Scalability**: Simple vs distributed
- **Cost vs Performance**: Budget vs optimization

---

## ⚠️ **RED FLAGS TO AVOID**

- Single point of failure
- No scaling plan
- Ignoring consistency requirements
- Over-engineering simple problems
- No monitoring strategy

---

## 📋 **DECISION CHECKLIST**

- [ ] Linearizability requirements clear?
- [ ] Scaling expectations defined?
- [ ] Performance requirements specified?
- [ ] Team expertise considered?
- [ ] Operational complexity evaluated?
- [ ] Cost implications understood?
- [ ] Failure scenarios planned?
- [ ] Backup and recovery procedures defined?
- [ ] Monitoring and alerting configured?
- [ ] Maintenance procedures documented?

---

## 🎯 **50 MAANG SYSTEM DESIGN INTERVIEW QUESTIONS**

### **Google-Style Questions**

#### **1. Design a URL Shortener (bit.ly)**
- **Storage Choice**: Key-Value Store (Redis) + RDBMS (PostgreSQL)
- **Trade-offs**: Redis for fast lookups, RDBMS for analytics
- **Scaling**: Hash-based sharding, read replicas

#### **2. Design a Chat System (WhatsApp)**
- **Storage Choice**: Document Store (MongoDB) + Message Queue (Kafka)
- **Trade-offs**: MongoDB for chat history, Kafka for real-time delivery
- **Scaling**: User-based sharding, geographic distribution

#### **3. Design a Social Media Feed (Instagram)**
- **Storage Choice**: Document Store (MongoDB) + Time Series DB (InfluxDB)
- **Trade-offs**: MongoDB for posts, InfluxDB for engagement metrics
- **Scaling**: User-based sharding, read replicas

#### **4. Design a Video Streaming Platform (YouTube)**
- **Storage Choice**: Object Store (S3) + RDBMS (PostgreSQL)
- **Trade-offs**: S3 for video files, RDBMS for metadata
- **Scaling**: CDN for global distribution, horizontal scaling

#### **5. Design a Ride-Sharing App (Uber)**
- **Storage Choice**: Geospatial DB (PostGIS) + Key-Value (Redis)
- **Trade-offs**: PostGIS for location queries, Redis for real-time data
- **Scaling**: Geographic partitioning, real-time updates

#### **6. Design a Search Engine (Google)**
- **Storage Choice**: Text Search (Elasticsearch) + Object Store (GCS)
- **Trade-offs**: Elasticsearch for search, GCS for web pages
- **Scaling**: Document-based sharding, distributed indexing

#### **7. Design a Payment System (Stripe)**
- **Storage Choice**: RDBMS (PostgreSQL) + Message Queue (Kafka)
- **Trade-offs**: PostgreSQL for ACID transactions, Kafka for events
- **Scaling**: Account-based sharding, read replicas

#### **8. Design a Recommendation System (Netflix)**
- **Storage Choice**: Document Store (MongoDB) + Time Series (InfluxDB)
- **Trade-offs**: MongoDB for user profiles, InfluxDB for viewing patterns
- **Scaling**: User-based sharding, ML model serving

#### **9. Design a File Storage System (Dropbox)**
- **Storage Choice**: Object Store (S3) + RDBMS (PostgreSQL)
- **Trade-offs**: S3 for files, PostgreSQL for metadata
- **Scaling**: User-based partitioning, CDN for popular files

#### **10. Design a Real-time Analytics Dashboard**
- **Storage Choice**: Time Series DB (InfluxDB) + Key-Value (Redis)
- **Trade-offs**: InfluxDB for historical data, Redis for real-time
- **Scaling**: Time-based partitioning, stream processing

### **Amazon-Style Questions**

#### **11. Design an E-commerce Platform (Amazon)**
- **Storage Choice**: RDBMS (Aurora) + Document Store (DynamoDB)
- **Trade-offs**: Aurora for orders, DynamoDB for product catalog
- **Scaling**: Product-based sharding, read replicas

#### **12. Design a Content Delivery Network (CloudFront)**
- **Storage Choice**: Object Store (S3) + Key-Value (ElastiCache)
- **Trade-offs**: S3 for origin, ElastiCache for edge caching
- **Scaling**: Geographic distribution, edge locations

#### **13. Design a Log Aggregation System**
- **Storage Choice**: Time Series DB (InfluxDB) + Object Store (S3)
- **Trade-offs**: InfluxDB for metrics, S3 for raw logs
- **Scaling**: Time-based partitioning, stream processing

#### **14. Design a Notification System**
- **Storage Choice**: Message Queue (SQS) + Key-Value (DynamoDB)
- **Trade-offs**: SQS for delivery, DynamoDB for user preferences
- **Scaling**: User-based sharding, multi-channel delivery

#### **15. Design a Gaming Leaderboard**
- **Storage Choice**: Key-Value (Redis) + Time Series (Timestream)
- **Trade-offs**: Redis for real-time, Timestream for historical
- **Scaling**: Game-based sharding, sorted sets

### **Microsoft-Style Questions**

#### **16. Design a Document Collaboration Tool (Google Docs)**
- **Storage Choice**: Document Store (Cosmos DB) + Object Store (Blob)
- **Trade-offs**: Cosmos DB for documents, Blob for attachments
- **Scaling**: Document-based sharding, operational transforms

#### **17. Design a Calendar System (Outlook)**
- **Storage Choice**: RDBMS (SQL Server) + Key-Value (Redis)
- **Trade-offs**: SQL Server for events, Redis for availability
- **Scaling**: User-based sharding, time-based queries

#### **18. Design a Video Conferencing System (Teams)**
- **Storage Choice**: Document Store (Cosmos DB) + Time Series (Azure TS)
- **Trade-offs**: Cosmos DB for meetings, TS for metrics
- **Scaling**: Geographic distribution, real-time streaming

### **Apple-Style Questions**

#### **19. Design iCloud Photo Storage**
- **Storage Choice**: Object Store (S3) + RDBMS (PostgreSQL)
- **Trade-offs**: S3 for photos, PostgreSQL for metadata
- **Scaling**: User-based partitioning, device sync

#### **20. Design Apple Music**
- **Storage Choice**: Document Store (MongoDB) + Object Store (S3)
- **Trade-offs**: MongoDB for playlists, S3 for audio files
- **Scaling**: User-based sharding, CDN for streaming

### **Netflix-Style Questions**

#### **21. Design a Movie Recommendation System**
- **Storage Choice**: Document Store (MongoDB) + Time Series (InfluxDB)
- **Trade-offs**: MongoDB for user profiles, InfluxDB for viewing data
- **Scaling**: User-based sharding, ML model serving

#### **22. Design a Video Encoding Pipeline**
- **Storage Choice**: Object Store (S3) + Message Queue (Kafka)
- **Trade-offs**: S3 for video files, Kafka for job queue
- **Scaling**: Parallel processing, multiple formats

### **Meta/Facebook-Style Questions**

#### **23. Design a Social Graph (Facebook)**
- **Storage Choice**: Graph DB (Neo4j) + Document Store (MongoDB)
- **Trade-offs**: Neo4j for relationships, MongoDB for posts
- **Scaling**: User-based sharding, graph partitioning

#### **24. Design a News Feed**
- **Storage Choice**: Document Store (MongoDB) + Time Series (InfluxDB)
- **Trade-offs**: MongoDB for posts, InfluxDB for engagement
- **Scaling**: User-based sharding, real-time aggregation

#### **25. Design a Photo Sharing App (Instagram)**
- **Storage Choice**: Object Store (S3) + Document Store (MongoDB)
- **Trade-offs**: S3 for photos, MongoDB for metadata
- **Scaling**: User-based sharding, CDN distribution

### **Additional Common Questions**

#### **26. Design a Rate Limiter**
- **Storage Choice**: Key-Value (Redis)
- **Trade-offs**: In-memory for speed, TTL for cleanup
- **Scaling**: Sliding window, distributed rate limiting

#### **27. Design a Distributed Cache**
- **Storage Choice**: Key-Value (Redis Cluster)
- **Trade-offs**: Memory vs persistence, consistency vs performance
- **Scaling**: Consistent hashing, replication

#### **28. Design a Job Scheduler**
- **Storage Choice**: RDBMS (PostgreSQL) + Message Queue (Kafka)
- **Trade-offs**: PostgreSQL for jobs, Kafka for execution
- **Scaling**: Time-based partitioning, worker pools

#### **29. Design a Distributed Lock**
- **Storage Choice**: Key-Value (Redis) + RDBMS (PostgreSQL)
- **Trade-offs**: Redis for speed, PostgreSQL for durability
- **Scaling**: Lease-based locking, leader election

#### **30. Design a Metrics Collection System**
- **Storage Choice**: Time Series DB (InfluxDB) + Object Store (S3)
- **Trade-offs**: InfluxDB for queries, S3 for long-term storage
- **Scaling**: Time-based partitioning, aggregation

#### **31. Design a Distributed Counter**
- **Storage Choice**: Key-Value (Redis) + RDBMS (PostgreSQL)
- **Trade-offs**: Redis for speed, PostgreSQL for durability
- **Scaling**: Sharded counters, eventual consistency

#### **32. Design a Distributed Queue**
- **Storage Choice**: Message Queue (Kafka) + RDBMS (PostgreSQL)
- **Trade-offs**: Kafka for throughput, PostgreSQL for persistence
- **Scaling**: Partitioning, consumer groups

#### **33. Design a Distributed Log**
- **Storage Choice**: Message Queue (Kafka) + Object Store (S3)
- **Trade-offs**: Kafka for streaming, S3 for storage
- **Scaling**: Partitioning, retention policies

#### **34. Design a Distributed Cache with Persistence**
- **Storage Choice**: Key-Value (Redis) + RDBMS (PostgreSQL)
- **Trade-offs**: Redis for speed, PostgreSQL for durability
- **Scaling**: Write-through, write-behind patterns

#### **35. Design a Distributed Session Store**
- **Storage Choice**: Key-Value (Redis Cluster)
- **Trade-offs**: Memory vs persistence, consistency vs availability
- **Scaling**: Consistent hashing, replication

#### **36. Design a Distributed Configuration Store**
- **Storage Choice**: Key-Value (etcd) + RDBMS (PostgreSQL)
- **Trade-offs**: etcd for speed, PostgreSQL for history
- **Scaling**: Consensus protocol, versioning

#### **37. Design a Distributed File System**
- **Storage Choice**: Object Store (S3) + RDBMS (PostgreSQL)
- **Trade-offs**: S3 for files, PostgreSQL for metadata
- **Scaling**: Partitioning, replication

#### **38. Design a Distributed Database**
- **Storage Choice**: RDBMS (PostgreSQL) + Message Queue (Kafka)
- **Trade-offs**: Consistency vs availability, performance vs durability
- **Scaling**: Sharding, replication, consensus

#### **39. Design a Distributed Search Engine**
- **Storage Choice**: Text Search (Elasticsearch) + Object Store (S3)
- **Trade-offs**: Elasticsearch for search, S3 for documents
- **Scaling**: Sharding, replication, indexing

#### **40. Design a Distributed Cache with Eviction**
- **Storage Choice**: Key-Value (Redis)
- **Trade-offs**: Memory vs performance, eviction policies
- **Scaling**: LRU, LFU, TTL-based eviction

#### **41. Design a Distributed Lock with Timeout**
- **Storage Choice**: Key-Value (Redis) + RDBMS (PostgreSQL)
- **Trade-offs**: Speed vs durability, timeout handling
- **Scaling**: Lease-based locking, deadlock detection

#### **42. Design a Distributed Counter with Reset**
- **Storage Choice**: Key-Value (Redis) + RDBMS (PostgreSQL)
- **Trade-offs**: Speed vs durability, reset semantics
- **Scaling**: Sharded counters, periodic persistence

#### **43. Design a Distributed Queue with Priority**
- **Storage Choice**: Message Queue (Kafka) + RDBMS (PostgreSQL)
- **Trade-offs**: Throughput vs ordering, priority handling
- **Scaling**: Partitioning, consumer groups

#### **44. Design a Distributed Log with Compression**
- **Storage Choice**: Message Queue (Kafka) + Object Store (S3)
- **Trade-offs**: Storage vs performance, compression ratios
- **Scaling**: Partitioning, retention policies

#### **45. Design a Distributed Cache with TTL**
- **Storage Choice**: Key-Value (Redis)
- **Trade-offs**: Memory vs performance, TTL accuracy
- **Scaling**: Lazy expiration, periodic cleanup

#### **46. Design a Distributed Session Store with Replication**
- **Storage Choice**: Key-Value (Redis Cluster)
- **Trade-offs**: Consistency vs availability, replication lag
- **Scaling**: Master-slave replication, failover

#### **47. Design a Distributed Configuration Store with Versioning**
- **Storage Choice**: Key-Value (etcd) + RDBMS (PostgreSQL)
- **Trade-offs**: Speed vs durability, version management
- **Scaling**: Consensus protocol, version control

#### **48. Design a Distributed File System with Deduplication**
- **Storage Choice**: Object Store (S3) + RDBMS (PostgreSQL)
- **Trade-offs**: Storage vs performance, deduplication accuracy
- **Scaling**: Content-based addressing, chunking

#### **49. Design a Distributed Database with Sharding**
- **Storage Choice**: RDBMS (PostgreSQL) + Message Queue (Kafka)
- **Trade-offs**: Consistency vs performance, sharding complexity
- **Scaling**: Hash-based sharding, cross-shard queries

#### **50. Design a Distributed Search Engine with Faceted Search**
- **Storage Choice**: Text Search (Elasticsearch) + Object Store (S3)
- **Trade-offs**: Search quality vs performance, facet accuracy
- **Scaling**: Sharding, replication, aggregation

---

## 📊 **COMPREHENSIVE DECISION FRAMEWORK**

### **Multi-Dimensional Decision Matrix**

| Storage Type | Linearizability | Throughput | Latency | Scalability | Query Flexibility | Schema Flexibility | Operational Complexity | Cost | Use Case Fit |
|--------------|-----------------|------------|---------|-------------|-------------------|-------------------|------------------------|------|--------------|
| **RDBMS** | ✅ 10 | ⚠️ 5 | ⚠️ 6 | ❌ 3 | ✅ 10 | ❌ 2 | ⚠️ 6 | ⚠️ 6 | ACID Transactions |
| **Key-Value** | ⚠️ 4 | ✅ 9 | ✅ 9 | ✅ 9 | ❌ 2 | ✅ 10 | ✅ 8 | ✅ 8 | Simple Lookups |
| **Wide Column** | ❌ 3 | ✅ 8 | ⚠️ 6 | ✅ 8 | ⚠️ 6 | ⚠️ 6 | ⚠️ 5 | ✅ 7 | Analytics |
| **Document** | ❌ 3 | ✅ 7 | ✅ 7 | ✅ 7 | ✅ 8 | ✅ 10 | ⚠️ 6 | ⚠️ 6 | Flexible Data |
| **Time Series** | ❌ 3 | ✅ 9 | ✅ 7 | ✅ 8 | ⚠️ 5 | ⚠️ 6 | ⚠️ 5 | ✅ 7 | Time Data |
| **Text Search** | ❌ 3 | ⚠️ 6 | ⚠️ 5 | ✅ 7 | ✅ 8 | ⚠️ 5 | ❌ 4 | ⚠️ 6 | Full-Text Search |
| **Object Store** | ❌ 2 | ⚠️ 4 | ❌ 3 | ✅ 9 | ❌ 1 | ✅ 10 | ✅ 9 | ✅ 9 | Large Files |
| **Geospatial** | ❌ 3 | ⚠️ 6 | ⚠️ 6 | ✅ 7 | ⚠️ 6 | ⚠️ 6 | ❌ 4 | ⚠️ 6 | Location Data |

### **Scoring Legend**
- **✅ 9-10**: Excellent fit
- **⚠️ 5-8**: Good fit with trade-offs
- **❌ 1-4**: Poor fit

### **Decision Process**
1. **Identify primary requirements** (consistency, throughput, latency)
2. **Evaluate secondary requirements** (scalability, flexibility, complexity)
3. **Consider operational constraints** (team expertise, budget, timeline)
4. **Apply decision matrix** for systematic evaluation
5. **Document trade-offs** and reasoning

---

*Use this cheatsheet for quick reference during interviews. Remember: choose storage based on requirements, not just familiarity.*
