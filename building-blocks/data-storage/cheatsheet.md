---
title: Data Storage Systems - Cheat Sheet
description: One-page quick reference for interviews
layout: default
parent: Data Storage
grand_parent: Building Blocks
---

# Data Storage Systems - Cheat Sheet
## One-Page Quick Reference for Interviews

## ❓ **PREREQUISITE QUESTIONS FOR STORAGE SELECTION**

### **Essential Questions to Ask Before Deciding**

#### **Functional Requirements**
- **What data are we storing?** (User profiles, transactions, logs, files, etc.)
- **What operations do we need?** (CRUD, complex queries, analytics, search)
- **What queries will be performed?** (Point queries, range queries, aggregations)
- **What are the access patterns?** (Read-heavy, write-heavy, mixed)
- **What data relationships exist?** (Simple key-value, complex joins, hierarchical)

#### **Non-Functional Requirements**
- **Performance Requirements:**
  - What's the expected latency? (sub-ms, ms, seconds)
  - What's the expected throughput? (ops/sec, GB/sec)
  - How many concurrent users/connections?
  - What's the peak vs average load?

- **Scalability Requirements:**
  - What's the current data volume?
  - What's the expected growth rate?
  - What's the target scale? (users, data size, transactions)
  - How quickly do we need to scale?

- **Consistency Requirements:**
  - Do we need ACID transactions?
  - Can we tolerate eventual consistency?
  - What's the consistency vs availability trade-off?
  - Do we need strong consistency for specific operations?

- **Availability Requirements:**
  - What's the required uptime? (99.9%, 99.99%, 99.999%)
  - What's the acceptable downtime?
  - Do we need geographic distribution?
  - What's the disaster recovery requirement?

#### **Operational Requirements**

##### **Team Expertise**
- What's the team's experience with different storage types?
- What's the learning curve for new technologies?
- Do we have operational expertise?

##### **Infrastructure Constraints**
- Are we cloud-native or on-premise?
- What are the cost constraints?
- What are the compliance requirements?
- What's the integration complexity?

- **Timeline & Complexity:**
  - What's the development timeline?
  - What's the acceptable operational complexity?
  - Do we need rapid prototyping or production-ready?
  - What's the migration strategy?

#### **Data-Specific Questions**
- **Data Structure:**
  - Is the schema fixed or evolving?
  - Do we need schema flexibility?
  - What's the data complexity? (simple, nested, hierarchical)
  - Do we have structured, semi-structured, or unstructured data?

- **Data Lifecycle:**
  - How long do we need to retain data?
  - Do we need data archival?
  - What's the data access pattern over time?
  - Do we need data versioning?

- **Data Relationships:**
  - Do we need complex joins?
  - Are there foreign key relationships?
  - Do we need referential integrity?
  - Are there hierarchical relationships?

#### **Query-Specific Questions**
- **Query Types:**
  - Point queries vs range queries?
  - Complex aggregations vs simple lookups?
  - Full-text search requirements?
  - Time-series queries?
  - Geospatial queries?

- **Query Performance:**
  - What's the acceptable query latency?
  - Do we need real-time vs batch processing?
  - What's the query complexity?
  - Do we need ad-hoc querying?

### **Decision Validation Checklist**
- [ ] **Functional requirements clearly defined?**
- [ ] **Performance requirements quantified?**
- [ ] **Scalability requirements projected?**
- [ ] **Consistency requirements understood?**
- [ ] **Availability requirements specified?**
- [ ] **Team expertise assessed?**
- [ ] **Infrastructure constraints identified?**
- [ ] **Data structure requirements clear?**
- [ ] **Query patterns analyzed?**
- [ ] **Operational complexity acceptable?**

## 🎯 **SYSTEMATIC DECISION FRAMEWORK**

### **Step 1: Primary Decision Tree**
```
ACID Transactions Required? 
├─ YES → RDBMS (MySQL, PostgreSQL, Oracle)
└─ NO → Continue to Step 2

Step 2: Data Access Pattern?
├─ Simple Key-Value Lookups → Key-Value Store (Redis, DynamoDB)
├─ Complex Queries & Analytics → Continue to Step 3
├─ Full-Text Search → Text Search Engine (Elasticsearch, Solr)
├─ Time-Series Data → Time Series DB (InfluxDB, TimescaleDB)
├─ Large Binary Files → Object Store (S3, GCS, Azure Blob)
└─ Flexible Schema → Continue to Step 3

Step 3: Query Complexity?
├─ Complex Joins & Transactions → RDBMS
├─ Document-Based Queries → Document Store (MongoDB, CouchDB)
└─ Column-Based Analytics → Wide Column Store (Cassandra, HBase)
```

### **Step 2: Common Scenario Decision Matrix**

| Scenario | Primary Choice | Alternative | Decision Factors |
|----------|----------------|-------------|------------------|
| **File Metadata Storage** | Document Store | RDBMS | Schema flexibility vs ACID |
| **User Session Data** | Key-Value Store | Document Store | Performance vs query flexibility |
| **E-commerce Product Catalog** | Document Store | RDBMS | Schema evolution vs transactions |
| **Financial Transactions** | RDBMS | Document Store | ACID vs flexibility |
| **Real-time Analytics** | Time Series DB | Wide Column Store | Time queries vs general analytics |
| **Search Functionality** | Text Search Engine | Document Store | Search quality vs general purpose |
| **Configuration Management** | Key-Value Store | Document Store | Simple access vs structured data |
| **Log Storage** | Time Series DB | Object Store | Time queries vs cost |
| **User Profiles** | Document Store | RDBMS | Schema flexibility vs relationships |
| **Caching Layer** | Key-Value Store | In-Memory DB | Performance vs persistence |

### **Decision Framework Dimensions**

| Dimension | Weight | Description | Critical For |
|-----------|--------|-------------|--------------|
| **Consistency Requirements** | 25% | ACID vs eventual consistency | Financial, user data |
| **Performance Requirements** | 20% | Latency & throughput needs | Real-time systems |
| **Scalability Needs** | 20% | Horizontal vs vertical scaling | High-growth systems |
| **Query Complexity** | 15% | Simple lookups vs complex queries | Analytics, reporting |
| **Schema Flexibility** | 10% | Fixed vs evolving schemas | Rapid development |
| **Operational Complexity** | 10% | Team expertise & maintenance | Production systems |

### **Storage Type Comparison**

| Storage Type | Consistency | Performance | Scalability | Query Flexibility | Schema Flexibility | Operational Complexity | Best For |
|--------------|-------------|-------------|-------------|-------------------|-------------------|------------------------|----------|
| **RDBMS** | ✅ Linearizable | ⚠️ 1-10ms | ❌ Vertical Only | ✅ Complex SQL | ❌ Schema Migration | ⚠️ Moderate | ACID Transactions |
| **Key-Value** | ⚠️ Eventual | ✅ 0.1-1ms | ✅ Horizontal | ❌ Simple Only | ✅ No Schema | ✅ Simple | High-Performance Lookups |
| **Wide Column** | ❌ Eventual | ✅ 1-10ms | ✅ Horizontal | ⚠️ Limited | ⚠️ Column Families | ⚠️ Moderate | Analytics/OLAP |
| **Document** | ❌ Eventual | ✅ 1-10ms | ✅ Horizontal | ✅ Rich Queries | ✅ Flexible | ⚠️ Moderate | Flexible Data Models |
| **Time Series** | ❌ Eventual | ✅ 1-10ms | ✅ Horizontal | ⚠️ Time-Based | ⚠️ Time Schema | ⚠️ Moderate | Time-Ordered Data |
| **Text Search** | ❌ Eventual | ⚠️ 10-100ms | ✅ Horizontal | ✅ Search Queries | ⚠️ Index Schema | ❌ Complex | Full-Text Search |
| **Object Store** | ❌ Eventual | ❌ 100ms-1s | ✅ Horizontal | ❌ Metadata Only | ✅ No Schema | ✅ Simple | Large Binary Files |

### **Storage Type Data Structures**

| Storage Type | Primary Data Structure | Secondary Structures | Transformations | Time Complexity |
|--------------|------------------------|--------------------|-----------------|-----------------|
| **RDBMS** | B+ Tree Indexes | Hash Tables (Buffer Pool), LRU Lists, WAL | Buffer Pool → WAL → B+ Tree → Disk | O(log n) search, O(1) buffer access |
| **Key-Value** | Hash Tables + LSM Trees | Skiplist (MemTable), Bloom Filters, SSTables | Skiplist → SSTable → LSM Tree | O(1) hash lookup, O(log n) skiplist |
| **Wide Column** | Column-Oriented Storage | B-Tree Indexes, Compression Algorithms | Raw Data → Column Groups → Compressed | O(log n) index, O(n) compression |
| **Document** | B-Tree Indexes | JSON/BSON Parser, Field Mappers | JSON → BSON → Index Entries | O(log n) index, O(n) parsing |
| **Time Series** | Time Buckets | Columnar Storage, Compression | Timestamp → Bucket → Column → Compressed | O(1) bucketing, O(n) compression |
| **Text Search** | Inverted Indexes | Skip Lists, Hash Tables, Compression | Text → Tokens → Inverted Index | O(n) tokenization, O(log n) search |
| **Object Store** | Hash-based Distribution | Metadata Indexes, Compression | File → Chunks → Distributed → Compressed | O(1) hash, O(n) compression |

### **Data Structure Performance Comparison**

| Data Structure | Lookup | Insert/Delete | Range Queries | Memory Usage | Best For |
|----------------|--------|---------------|---------------|--------------|----------|
| **Hash Tables** | O(1) | O(1) | ❌ | O(n) | Exact lookups |
| **B-Trees** | O(log n) | O(log n) | ✅ | O(n) | Ordered data |
| **Skip Lists** | O(log n) | O(log n) | ✅ | O(n) | Concurrent access |
| **LSM Trees** | O(log n) | O(1) | ✅ | O(n) | Write-heavy workloads |
| **Inverted Indexes** | O(log n) | O(log n) | ✅ | O(n) | Text search |
| **Columnar Storage** | O(log n) | O(n) | ✅ | O(n) | Analytics |

### **Use Case Scenarios**

| Primary Storage | Secondary Storage | Key Decision Factors |
|----------------|-------------------|---------------------|
| **User Authentication** | RDBMS | Key-Value Cache | ACID + performance |
| **Session Management** | Key-Value Store | RDBMS | Performance + persistence |

### **Product Catalog**

| Component | Primary Storage | Secondary Storage | Key Decision Factors |
|-----------|----------------|-------------------|---------------------|
| **Product Catalog** | Document Store | Text Search | Flexibility + search |
| **Order Management** | RDBMS | Message Queue | ACID + event sourcing |
| **User Profiles** | Document Store | RDBMS | Flexibility vs relationships |
| **File Storage** | Object Store | Document Store | Large files + metadata |

### **Analytics Dashboard**

| Component | Primary Storage | Secondary Storage | Key Decision Factors |
|-----------|----------------|-------------------|---------------------|
| **Analytics Dashboard** | Time Series DB | Wide Column Store | Time queries + analytics |
| **Configuration** | Key-Value Store | Document Store | Simple access + complexity |
| **Log Storage** | Time Series DB | Object Store | Time queries + cost |
| **Search Engine** | Text Search Engine | Document Store | Search quality + content |

### **Real-time Chat**

| Component | Primary Storage | Secondary Storage | Key Decision Factors |
|-----------|----------------|-------------------|---------------------|
| **Real-time Chat** | Document Store | Message Queue | Flexibility + real-time |
| **Gaming Leaderboard** | Key-Value Store | Time Series DB | Performance + historical |
| **IoT Data** | Time Series DB | Object Store | Time queries + large volumes |
| **Content Management** | Document Store | Object Store | Content + metadata |

### **Financial Transactions**

| Component | Primary Storage | Secondary Storage | Key Decision Factors |
|-----------|----------------|-------------------|---------------------|
| **Financial Transactions** | RDBMS | Event Store | ACID + audit trail |
| **Audit Trail** | Event Store | RDBMS | Immutable history |
| **Reporting** | Data Warehouse | RDBMS | Analytics + compliance |

### **Data Pattern Selection Guide**

| Data Pattern | Storage Choice | Reasoning | Trade-offs |
|--------------|----------------|-----------|------------|
| **Simple Key-Value** | Key-Value Store | Fast lookups | Limited query flexibility |
| **Complex Documents** | Document Store | Schema flexibility | Eventual consistency |
| **Time-Series Data** | Time Series DB | Time-optimized queries | Limited general use |
| **Relational Data** | RDBMS | ACID + joins | Scaling complexity |
| **Large Binary Files** | Object Store | Cost-effective storage | Limited metadata queries |
| **Searchable Content** | Text Search Engine | Rich search capabilities | Storage overhead |
| **Analytical Data** | Wide Column Store | Column-oriented queries | Complex modeling |

### **Scaling Strategies**

| Strategy | Scale Factor | Implementation | Use Case |
|----------|--------------|----------------|----------|
| **Vertical Scaling** | 2-10x | Hardware upgrade | Single instance performance |
| **Read Replicas** | 10-50x | Master-slave replication | Read-heavy workloads |
| **Sharding** | 100-1000x | Hash/range partitioning | Write-heavy workloads |
| **Connection Pooling** | 10-100x | Connection management | Connection limits |
| **Caching** | 10-100x | Application cache | Frequently accessed data |
| **Horizontal Scaling** | 100-1000x | Consistent hashing | Even distribution |
| **Replication** | 10-100x | Master-slave | High availability |
| **Partitioning** | 100-1000x | Hash partitioning | Data distribution |
| **Auto-scaling** | 10-100x | Dynamic scaling | Variable workloads |
| **Caching Layers** | 10-100x | Multi-level cache | Performance optimization |
| **Indexing** | 10-100x | B-tree indexes | Query performance |
| **Aggregation** | 10-100x | Pre-computed results | Analytics performance |

### **Scaling Strategy**

| Strategy | Scale Factor | Implementation | Use Case |
|----------|--------------|----------------|----------|
| **Horizontal Scaling** | 100-1000x | Consistent hashing | Data distribution |
| **Replication** | 10-100x | Master-slave | High availability |

### **Compression**

| Strategy | Compression Ratio | Method | Use Case |
|----------|------------------|--------|----------|
| **Columnar Compression** | 2-10x | Columnar compression | Storage optimization |
| **Batch Operations** | 10-100x | Bulk operations | High throughput |
| **Caching** | 10-100x | Row/key cache | Performance optimization |

### **Advanced Scaling**

| Strategy | Scale Factor | Method | Use Case |
|----------|--------------|--------|----------|
| **Horizontal Scaling** | 100-1000x | Time-based sharding | Data distribution |
| **Compression** | 5-20x | Columnar compression | Storage optimization |
| **Downsampling** | 10-100x | Data aggregation | Historical data |

### **Retention Policies**

| Strategy | Efficiency Gain | Method | Use Case |
|----------|----------------|--------|----------|
| **TTL-based Deletion** | 10-100x | TTL-based deletion | Storage management |
| **Hot Data Caching** | 10-100x | Hot data caching | Recent data access |

### **Consensus Algorithms**

| Algorithm | Use Case | Complexity | Examples |
|-----------|----------|------------|----------|
| **Paxos** | Distributed consensus | High | Google Chubby, ZooKeeper |
| **Raft** | Distributed consensus | Medium | etcd, Consul, MongoDB |
| **ZAB** | Atomic broadcast | Medium | Apache ZooKeeper |
| **Gossip** | Eventual consistency | Low | Cassandra, DynamoDB |
| **Vector Clocks** | Causal consistency | Medium | DynamoDB, Riak |
| **CRDTs** | Conflict resolution | Low | Riak, Redis CRDTs |

### **Partitioning Strategies**

| Strategy | Mechanism | Advantages | Disadvantages | Use Cases |
|----------|-----------|------------|---------------|-----------|
| **Hash-based** | Consistent hashing | Even distribution | Range queries difficult | Key-value stores |

| **Range-based** | Key ranges | Efficient range queries | Potential hotspots | Time series, analytics |
| **Directory-based** | Lookup table | Flexible, balanced | Centralized directory | Complex requirements |
| **Time-based** | Time buckets | Natural time queries | Time-based hotspots | Time series data |
| **Geographic** | Location-based | Low latency | Geographic hotspots | Global applications |

### **Storage Type Availability**

| Storage Type | Native Availability | Max with Scaling | Failure Recovery |
|--------------|-------------------|------------------|------------------|
| **RDBMS** | 99.9% | 99.99% | Automatic failover |
| **Key-Value** | 99.9% | 99.99% | Automatic failover |
| **Document** | 99.9% | 99.99% | Automatic failover |
| **Wide Column** | 99.99% | 99.999% | Geographic failover |
| **Time Series** | 99.9% | 99.99% | Automatic failover |
| **Object Store** | 99.9% | 99.99% | Geographic failover |

### **Storage Type Consistency**

| Storage Type | Default | Configurable | Trade-offs |
|--------------|----------|--------------|------------|
| **RDBMS** | Linearizable | Read committed, repeatable read | Performance vs consistency |
| **Key-Value** | Eventual | Strong consistency | Consistency vs latency |
| **Document** | Eventual | Read concern levels | Consistency vs performance |
| **Wide Column** | Eventual | Quorum reads/writes | Consistency vs latency |
| **Time Series** | Eventual | Time-based consistency | Consistency vs performance |

### **Backup and Recovery**

| Storage Type | Method | Recovery Time | Frequency | Special Considerations |
|--------------|--------|---------------|-----------|------------------------|
| **RDBMS** | Full + incremental | Hours | Daily | Point-in-time recovery |
| **Key-Value** | Snapshot + WAL | Minutes | Daily | Memory state + disk state |
| **Document** | Oplog replay | Minutes | Daily | Replica set consistency |
| **Wide Column** | SSTable backup | Hours | Daily | Consistency across nodes |
| **Time Series** | Time-based backup | Minutes | Daily | Retention policy alignment |
| **Object Store** | Cross-region copy | Hours | Daily | Geographic distribution |

### **Storage Tiers**

| Tier | Access Pattern | Latency | Cost | Migration Trigger |
|------|----------------|---------|------|-------------------|
| **Hot Storage** | Frequent access | < 10ms | High | Active data |
| **Warm Storage** | Occasional access | 10-100ms | Medium | Recent data |
| **Cold Storage** | Rare access | 100ms-1s | Low | Historical data |
| **Archive Storage** | Compliance only | 1s-1min | Very Low | Long-term retention |

### **Data Lifecycle Phases**

| Phase | Duration | Storage Type | Access Pattern | Cost Optimization |
|-------|----------|--------------|----------------|-------------------|
| **Active** | 0-30 days | Hot storage | Frequent | Performance optimization |
| **Recent** | 30-90 days | Warm storage | Occasional | Balanced cost/performance |
| **Historical** | 90 days-1 year | Cold storage | Rare | Storage optimization |
| **Archive** | 1+ years | Archive storage | Compliance | Cost optimization |

### **Storage Capacity**

| Storage Type | Single Instance | Clustered | Total Capacity | Scaling Factor |
|--------------|----------------|-----------|----------------|----------------|
| **RDBMS** | 1-10TB | 100TB-1PB | 1PB+ | 100-1000x |
| **Key-Value** | 100GB-1TB | 10TB-100TB | 100TB+ | 100-1000x |
| **Document** | 1-10TB | 100TB-1PB | 1PB+ | 100-1000x |
| **Wide Column** | 10-100TB | 1PB-10PB | 10PB+ | 100-1000x |
| **Time Series** | 1-10TB | 100TB-1PB | 1PB+ | 100-1000x |
| **Object Store** | 1-10TB | 1PB-100PB | 100PB+ | 1000-10000x |

### **Storage Performance**

| Storage Type | Read Throughput | Write Throughput | Concurrent Connections | Query Complexity |
|--------------|----------------|------------------|----------------------|------------------|
| **RDBMS** | 10K-100K ops/sec | 1K-10K ops/sec | 10K-100K | Complex SQL |
| **Key-Value** | 100K-1M ops/sec | 100K-1M ops/sec | 100K-1M | Simple lookups |
| **Document** | 10K-100K ops/sec | 10K-100K ops/sec | 10K-100K | Rich queries |
| **Wide Column** | 10K-100K ops/sec | 100K-1M ops/sec | 10K-100K | Analytics |
| **Time Series** | 10K-100K ops/sec | 100K-1M ops/sec | 10K-100K | Time queries |
| **Object Store** | 100-1K ops/sec | 100-1K ops/sec | 1K-10K | Large files |

### **Partitioning Strategies**

| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Range Partitioning** | Partition by value ranges | Time-series data, ordered data | Efficient range queries | Potential hotspots |
| **Hash Partitioning** | Partition by hash function | Even distribution | Balanced load | Range queries inefficient |
| **List Partitioning** | Partition by specific values | Categorical data | Direct partition access | Limited flexibility |
| **Composite Partitioning** | Multiple partitioning methods | Complex requirements | Flexibility | Increased complexity |

### **Sharding Strategies**

| Strategy | Mechanism | Implementation | Use Case | Complexity |
|----------|-----------|----------------|----------|------------|
| **Hash-based Sharding** | Consistent hashing | User ID, UUID | Even distribution | Medium |
| **Range-based Sharding** | Key ranges | Time-series, ordered data | Efficient range queries | High |
| **Directory-based Sharding** | Lookup table | Complex requirements | Flexibility | High |
| **Composite Sharding** | Multiple strategies | Complex data | Optimal distribution | Very High |

### **Sharding Challenges**

| Problem | Solution | Implementation |
|---------|----------|----------------|
| **Cross-shard Queries** | Denormalization, application-level joins | Query routing, data duplication |
| **Transaction Management** | Distributed transactions, saga pattern | Two-phase commit, compensation logic |
| **Data Distribution** | Uneven shard load | Rebalancing, dynamic sharding |
| **Schema Changes** | Coordinated schema updates | Blue-green deployment, versioning |

### **Redis Sharding Strategies**

| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Hash Slots** | 16384 hash slots | Even distribution | Automatic rebalancing | Limited flexibility |
| **Key Tags** | Custom hash tags | Related data | Co-location | Manual management |
| **Hash Functions** | CRC16, MD5 | Custom distribution | Flexibility | Implementation complexity |

### **DynamoDB Partitioning Strategies**

| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Hash Partition Key** | Single partition key | Simple access patterns | Even distribution | Limited query flexibility |
| **Composite Key** | Partition + Sort key | Range queries | Efficient range queries | Design complexity |
| **GSI Partitioning** | Global secondary indexes | Multiple access patterns | Query flexibility | Additional cost |

### **MongoDB Sharding Strategies**

| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Hash-based Sharding** | Hash of shard key | Even distribution | Balanced load | Range queries inefficient |
| **Range-based Sharding** | Shard key ranges | Range queries | Efficient range queries | Potential hotspots |
| **Zoned Sharding** | Geographic zones | Multi-region | Geographic distribution | Complexity |

### **MongoDB Sharding Criteria**

| Considerations | Best Practices | Examples |
|---------------|----------------|----------|
| **Cardinality** | High cardinality | user_id, order_id |
| **Write Distribution** | Avoid low-cardinality keys | Even distribution across shards |
| **Query Patterns** | Support common queries | Include query fields in shard key |
| **Chunk Size** | Optimal chunk size | 64MB-128MB chunks |

### **MongoDB Partitioning Strategies**

| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Hash Partitioning** | Consistent hashing | Even distribution | Balanced load | Range queries difficult |
| **Composite Partitioning** | Multiple partition keys | Complex requirements | Flexibility | Design complexity |
| **Time-based Partitioning** | Time buckets | Time-series data | Time-based queries | Time-based hotspots |

### **MongoDB Best Practices**

| Description | Implementation | Benefits |
|-------------|----------------|----------|
| **High Cardinality** | UUID, hash-based keys | Even distribution |
| **Avoid Hotspots** | Unique partition keys | Balanced load |
| **Query Optimization** | Design for query patterns | Performance |
| **Compaction Strategy** | Size-tiered, leveled compaction | Storage efficiency |

### **InfluxDB Partitioning Strategies**

| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Time-based Partitioning** | Time buckets | Time-series data | Efficient time queries | Time-based hotspots |
| **Tag-based Partitioning** | Tag values | Multi-dimensional data | Flexible queries | Cardinality explosion |
| **Measurement Partitioning** | Different measurements | Logical separation | Clear organization | Cross-measurement queries |

### **InfluxDB Sharding Strategies**

| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Time-based Sharding** | Time ranges per shard | Historical data | Efficient time queries | Time-based hotspots |
| **Metric-based Sharding** | Different metrics per shard | Diverse metrics | Logical separation | Cross-metric queries |
| **Hybrid Sharding** | Time + metric combination | Complex requirements | Flexibility | Complexity |

### **Elasticsearch Sharding Strategies**

| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Document-based Sharding** | Hash of document ID | Even distribution | Balanced load | Cross-document queries |
| **Routing-based Sharding** | Custom routing | Related documents | Co-location | Manual management |
| **Time-based Sharding** | Time indices | Time-series data | Time-based queries | Time-based hotspots |

### **Elasticsearch Best Practices**

| Description | Implementation | Benefits |
|-------------|----------------|----------|
| **Index Aliases** | Alias → Multiple indices | Zero-downtime reindexing |
| **Index Lifecycle** | Logical index names | Management flexibility |
| **Shard Allocation** | Custom allocation | Performance optimization |
| **Replica Management** | Replica allocation, recovery | Fault tolerance |

### **S3 Partitioning Strategies**

| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Hash-based Partitioning** | Hash of object key | Even distribution | Balanced load | No logical grouping |
| **Prefix-based Partitioning** | Key prefixes | Logical organization | Efficient listing | Potential hotspots |
| **Time-based Partitioning** | Time in key | Time-series objects | Time-based access | Time-based hotspots |

### **S3 Sharding Strategies**

| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Bucket-based Sharding** | Different buckets | Logical separation | Clear organization | Cross-bucket operations |
| **Region-based Sharding** | Geographic regions | Global distribution | Low latency | Cross-region costs |
| **Storage-tier Sharding** | Different storage classes | Cost optimization | Cost efficiency | Access pattern changes |

### **Common Pitfalls and Mitigation**

| Pitfall | Description | Impact | Mitigation |
|---------|-------------|--------|------------|
| **N+1 Query Problem** | Multiple queries instead of joins | Performance degradation | Use eager loading, batch queries |
| **Missing Indexes** | No indexes on queried fields | Slow queries | Create appropriate indexes |
| **Connection Pool Exhaustion** | Too many database connections | Application failures | Configure connection pooling |
| **Long-Running Transactions** | Transactions holding locks too long | Deadlocks, poor performance | Keep transactions short |
| **Schema Lock Contention** | DDL operations blocking queries | Application downtime | Use online DDL, maintenance windows |
| **Memory Exhaustion** | Running out of memory | Service failures | Configure eviction policies |
| **Hot Keys** | Uneven key distribution | Performance bottlenecks | Use key distribution strategies |
| **Cache Stampede** | Multiple requests for same expired key | Performance degradation | Use cache warming, background refresh |
| **TTL Management** | Inconsistent expiration handling | Memory leaks | Implement proper TTL cleanup |
| **Large Documents** | Documents exceeding 16MB | Performance degradation | Normalize large documents |
| **Schema Drift** | Inconsistent document structures | Query complexity | Design schema upfront |
| **Write Concern Issues** | Insufficient write acknowledgment | Data loss | Configure appropriate write concerns |
| **Wide Rows** | Too many columns per row | Performance degradation | Normalize wide rows |
| **Read Repair Overhead** | Frequent consistency repairs | Performance degradation | Tune read repair frequency |
| **Compaction Pressure** | Insufficient compaction resources | Performance degradation | Monitor and tune compaction |

### **Time Series Database Pitfalls**

| Description | Impact | Mitigation |
|-------------|--------|------------|
| **Cardinality Explosion** | Too many unique time series | Memory usage | Limit cardinality, use tags wisely |
| **Retention Policy Issues** | Very large time ranges | Performance degradation | Use appropriate time windows |
| **Downsampling Configuration** | Incorrect aggregation intervals | Data loss | Configure downsampling carefully |
| **Write Buffer Issues** | Insufficient write buffering | Performance degradation | Tune write buffer size |

### **Storage Type Scoring Matrix**

| Storage Type | Consistency | Performance | Scalability | Query Flexibility | Schema Flexibility | Operational Complexity | Cost | Use Case Fit |
|--------------|-------------|-------------|-------------|-------------------|-------------------|------------------------|------|--------------|
| **RDBMS** | ✅ 10 | ⚠️ 6 | ❌ 3 | ✅ 10 | ❌ 2 | ⚠️ 6 | ⚠️ 6 | ACID Transactions |
| **Key-Value** | ⚠️ 4 | ✅ 10 | ✅ 9 | ❌ 2 | ✅ 10 | ✅ 8 | ✅ 8 | Simple Lookups |
| **Wide Column** | ❌ 3 | ✅ 8 | ⚠️ 6 | ⚠️ 6 | ⚠️ 6 | ⚠️ 5 | ✅ 7 | Analytics |
| **Document** | ❌ 3 | ✅ 7 | ✅ 7 | ✅ 8 | ✅ 10 | ⚠️ 6 | ⚠️ 6 | Flexible Data |
| **Time Series** | ❌ 3 | ✅ 9 | ✅ 7 | ⚠️ 5 | ⚠️ 6 | ⚠️ 5 | ✅ 7 | Time Data |
| **Text Search** | ❌ 3 | ⚠️ 6 | ⚠️ 5 | ✅ 8 | ⚠️ 5 | ❌ 4 | ⚠️ 6 | Full-Text Search |
| **Object Store** | ❌ 2 | ⚠️ 4 | ❌ 3 | ❌ 1 | ✅ 10 | ✅ 9 | ✅ 9 | Large Files |

### **Scoring Methodology**

| Score Range | Rating | Description |
|-------------|--------|-------------|
| **✅ 9-10** | Excellent | Excellent fit for the requirement |
| **⚠️ 5-8** | Good | Good fit with some trade-offs |
| **❌ 1-4** | Poor | Poor fit, significant compromises needed |

### **Decision Validation Process**

```
Step 1: Proof of Concept
├─ Technical feasibility validation
├─ Performance testing
├─ Scalability testing
└─ Integration testing

Step 2: Risk Assessment
├─ Single point of failure analysis
├─ Data loss scenarios
├─ Performance degradation risks
└─ Operational complexity assessment

Step 3: Cost Analysis
├─ Infrastructure costs
├─ Operational costs
├─ Development costs
└─ Migration costs

Step 4: Final Decision
├─ Document decision rationale
├─ Identify trade-offs and compromises
├─ Plan implementation strategy
└─ Define success metrics
```

### **Common Decision Patterns**

#### **Pattern 1: ACID Requirements**
```
If ACID transactions required:
├─ Primary: RDBMS
├─ Consider: Event sourcing for audit trails
├─ Alternative: Distributed transactions (complex)
└─ Trade-off: Scaling complexity vs data integrity
```

#### **Pattern 2: High Performance Requirements**
```
If sub-millisecond latency required:
├─ Primary: Key-Value Store
├─ Consider: In-memory databases
├─ Alternative: Caching layer + persistent storage
└─ Trade-off: Performance vs data persistence
```

#### **Pattern 3: Schema Flexibility Requirements**
```
If schema evolution expected:
├─ Primary: Document Store
├─ Consider: Schema migration strategies
├─ Alternative: Versioned schemas
└─ Trade-off: Flexibility vs query performance
```

#### **Pattern 4: Analytics Requirements**
```
If complex analytics needed:
├─ Primary: Wide Column Store
├─ Consider: Data warehouse integration
├─ Alternative: Analytics-specific databases
└─ Trade-off: Query complexity vs performance
```

---

*Use this cheatsheet for quick reference during interviews. Remember: choose storage based on requirements, not just familiarity.*
