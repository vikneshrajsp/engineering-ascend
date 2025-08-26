---
title: Data Storage Systems - Concise Summary
description: Quick revision guide for system design
layout: default
parent: Data Storage
grand_parent: Building Blocks
---

# Data Storage Systems - Concise Summary
## Quick Revision Guide for System Design

## 📋 **STORAGE SYSTEM OVERVIEW**

### **Storage Types Classification with Performance Metrics**

| Storage Type | Primary Use | Consistency Model | Scaling Pattern | Read Throughput | Write Throughput | Latency | Examples |
|--------------|-------------|-------------------|-----------------|-----------------|------------------|---------|----------|
| **RDBMS** | ACID transactions | Linearizable | Vertical + Read Replicas | 10K-50K ops/sec | 5K-20K ops/sec | 1-5ms | MySQL, PostgreSQL |
| **Key-Value** | Simple lookups | Eventual/Linearizable | Horizontal Sharding | 100K-1M ops/sec | 50K-500K ops/sec | 0.1-1ms | Redis, DynamoDB |
| **Wide Column** | Analytics | Eventual | Hash-based Partitioning | 10K-100K ops/sec | 50K-200K ops/sec | 5-20ms | Cassandra, HBase |
| **Document** | Flexible schemas | Eventual | Range-based Sharding | 10K-50K ops/sec | 5K-20K ops/sec | 1-10ms | MongoDB, CouchDB |
| **Time Series** | Time-ordered data | Eventual | Time-based Partitioning | 10K-100K ops/sec | 100K-1M ops/sec | 1-10ms | InfluxDB, TimescaleDB |
| **Text Search** | Full-text search | Eventual | Document-based Sharding | 1K-10K ops/sec | 1K-5K ops/sec | 10-100ms | Elasticsearch, Solr |
| **Object Store** | Large files | Eventual | Hash-based Distribution | 100-1K ops/sec | 100-1K ops/sec | 100ms-1s | S3, GCS, Azure Blob |
| **Geospatial** | Location data | Eventual | Geographic Partitioning | 1K-10K ops/sec | 1K-5K ops/sec | 1-10ms | PostGIS, MongoDB |

---

## 🏗️ **CORE STORAGE SYSTEMS**

### **1. Relational Database Management Systems (RDBMS)**

#### **Key Characteristics**
- ✅ Linearizable consistency (ACID properties)
- ✅ Structured schemas with relational constraints
- ✅ SQL query language with ACID transactions
- ✅ Multi-version concurrency control (MVCC)
- ❌ Limited horizontal scaling (vertical + read replicas)
- ❌ Schema rigidity and migration complexity

#### **Internal Structures**
```
B-Tree Indexes:
- Balanced tree structure
- O(log n) search complexity
- Efficient range queries
- Disk-optimized

B+ Tree Indexes:
- All data in leaf nodes
- Better sequential access
- Reduced tree height
- Linked leaf nodes

Skiplist Structures:
- Probabilistic O(log n) height
- Multiple forward pointers
- Memory efficient
- Redis sorted sets
```

#### **Data Structure Transformations**
```
Write Path: Buffer Pool → WAL → B+ Tree → Disk
- Hash Table: O(1) page lookup
- LRU List: O(1) eviction
- Sequential WAL: O(1) append
- B+ Tree: O(log n) updates

Read Path: Query → Index → Buffer Pool → Data
- Parse Tree: O(n) parsing
- B+ Tree: O(log n) search
- Buffer Pool: O(1) access
- Tuple Assembly: O(k) for k fields
```

#### **Use Cases**
- Financial transactions
- User account management
- Inventory systems
- E-commerce orders

---

### **2. Key-Value Stores**

#### **Key Characteristics**
- ✅ Simple key-value pairs with O(1) lookup
- ✅ High performance with hash table implementation
- ✅ Horizontal scaling via consistent hashing
- ✅ High write throughput with LSM trees
- ❌ Limited query capabilities (no range queries)
- ❌ Eventual consistency (configurable in some systems)

#### **Internal Mechanisms**
```
Hash Tables:
- O(1) average lookup
- Collision resolution (chaining, open addressing)
- Memory efficient
- No natural ordering

LSM Trees:
- Write-optimized (append to MemTable)
- Background compaction
- Bloom filters for existence checks
- Sequential disk writes

Skiplist MemTable:
- O(log n) insertion in memory
- Sorted by key for efficient lookups
- Hash table for duplicate detection
- Bloom filter for existence checks
```

#### **Data Structure Transformations**
```
Write Path: MemTable → SSTable → LSM Tree
- Skiplist: O(log n) in-memory insertion
- Hash Table: O(1) duplicate detection
- Sequential Write: O(n) SSTable creation
- Merge Sort: O(n log n) compaction

Read Path: MemTable → Bloom Filter → SSTable
- Skiplist: O(log n) memory search
- Bloom Filter: O(k) hash operations
- Binary Search: O(log n) SSTable lookup
- Merge Logic: Latest value selection
```

#### **Use Cases**
- Session storage
- Configuration management
- Real-time analytics
- Gaming leaderboards

---

### **3. Wide Column Stores**

#### **Key Characteristics**
- ✅ Column-oriented storage
- ✅ High compression ratios
- ✅ Sparse data handling
- ✅ Analytical queries
- ❌ Complex data modeling
- ❌ Limited ACID support

#### **Storage Structure**
```
Row-Oriented vs Column-Oriented:

Row: [User1: John, 25, NYC] [User2: Jane, 30, LA]
Col: [John, Jane] [25, 30] [NYC, LA]

Column Families:
- Basic Info: {name, email, age}
- Address: {street, city, state, zip}
- Preferences: {theme, language}
```

#### **Use Cases**
- Data warehousing
- IoT sensor data
- Log analysis
- Business intelligence

---

### **4. Document Stores**

#### **Key Characteristics**
- ✅ Schema flexibility
- ✅ Rich data types (nested objects, arrays)
- ✅ Complex queries
- ✅ Horizontal scaling
- ❌ No ACID guarantees
- ❌ Complex transactions

#### **Document Structure**
```json
{
  "user_id": "12345",
  "profile": {
    "name": "John Doe",
    "email": "john@example.com",
    "addresses": [
      {"type": "home", "city": "NYC"},
      {"type": "work", "city": "LA"}
    ]
  }
}
```

#### **Indexing Strategies**
- Single field: `{"email": 1}`
- Compound: `{"age": 1, "city": 1}`
- Array: `{"addresses.city": 1}`
- Text: `{"profile.name": "text"}`

#### **Use Cases**
- Content management
- User profiles
- Product catalogs
- API data storage

---

### **5. Time Series Databases**

#### **Key Characteristics**
- ✅ Time-ordered data
- ✅ High write throughput
- ✅ Data retention policies
- ✅ Time-based aggregations
- ❌ Limited general-purpose use
- ❌ Complex retention management

#### **Storage Architecture**
```
Time Buckets:
Hour 1: [Data Points 1-3600]
Hour 2: [Data Points 3601-7200]

Compression:
Raw: 1-minute intervals (1 day)
Hourly: Aggregates (1 month)
Daily: Summaries (1 year)
```

#### **Data Structure Transformations**
```
Write Path: Timestamp → Bucket → Column → Compressed
- Time Bucketing: O(1) bucket assignment
- Value Encoding: Delta encoding O(n)
- Compression: Run-length encoding
- Index Updates: Time-based maintenance

Read Path: Query → Buckets → Columns → Time Series
- Time Range: O(log n) bucket selection
- Column Access: Direct column reading
- Decompression: O(n) value processing
- Aggregation: Statistical operations
```

#### **Use Cases**
- IoT sensor data
- Application metrics
- Financial time series
- System monitoring

---

### **6. Text Search Engines**

#### **Key Characteristics**
- ✅ Full-text search
- ✅ Relevance scoring
- ✅ Faceted search
- ✅ Real-time indexing
- ❌ Complex indexing
- ❌ Storage overhead

#### **Inverted Index**
```
Documents:
Doc1: "The quick brown fox"
Doc2: "A quick brown dog"

Index:
"quick": [Doc1:2, Doc2:2]
"brown": [Doc1:3, Doc2:3]
"fox": [Doc1:4]
"dog": [Doc2:4]
```

#### **Data Structure Transformations**
```
Indexing Path: Text → Tokens → Inverted Index
- Tokenization: O(n) character processing
- Term Dictionary: Hash table O(1) lookups
- Posting Lists: Skip list O(log n) access
- Compression: Variable-length encoding

Search Path: Query → Terms → Posting Lists → Results
- Query Parsing: O(n) query length
- Term Lookup: O(1) dictionary access
- List Intersection: O(n) merge complexity
- Scoring: TF-IDF, BM25 algorithms
```

#### ### **Search Types**

| - Boolean: `"quick AND brown"` | - Fuzzy: `"quik" → "quick"` | - Phrase: `"quick brown fox"` |
|---|---|---|
| #### **Use Cases** | - E-commerce search | - Content discovery | - Log analysis |
- Knowledge bases

---

### **7. Write-Ahead Logs (WAL)**

#### **Key Characteristics**
- ✅ Sequential writes
- ✅ Crash recovery
- ✅ Durability guarantees
- ✅ Performance optimization
- ❌ Storage overhead
- ❌ Complex recovery

#### **WAL Structure**
```
[Header] [Record1] [Record2] [Record3] ... [Footer]

Record: [Length] [Timestamp] [Operation] [Data] [Checksum]

Operations: BEGIN_TXN, INSERT, UPDATE, DELETE, COMMIT, ROLLBACK
```

#### **Recovery Process**
1. Read WAL from checkpoint
2. Replay operations in order
3. Reconstruct state
4. Verify consistency
5. Resume operation

#### **Use Cases**
- Database transaction logs
- Message queue persistence
- Event sourcing
- Audit trails

---

### **8. Object Stores**

#### **Key Characteristics**
- ✅ Large file storage
- ✅ RESTful API access
- ✅ High durability
- ✅ Cost-effective
- ❌ High latency
- ❌ Limited query capabilities

#### **Storage Tiers**
- **Hot**: Frequently accessed, low latency
- **Warm**: Occasionally accessed, medium latency
- **Cold**: Rarely accessed, high latency
- **Archive**: Long-term storage, very high latency

#### **Use Cases**
- Media file storage
- Backup and archival
- Data lake storage
- Static asset hosting

---

## 🔍 **INDEXING STRATEGIES**

### **In-Memory Indexes**

| Index Type | Lookup | Insert/Delete | Memory | Ordering |
|------------|--------|---------------|--------|----------|
| **Hash Tables** | O(1) | O(1) | O(n) | No |
| **B-Trees** | O(log n) | O(log n) | O(n) | Yes |
| **Skip Lists** | O(log n) | O(log n) | O(n) | Yes |

### **On-Disk Indexes**

| Index Type | Write Performance | Read Performance | Space Efficiency |
|------------|-------------------|------------------|------------------|
| **B-Tree** | Good | Excellent | Good |
| **LSM Tree** | Excellent | Good | Excellent |
| **Bitmap** | Poor | Excellent | Excellent |

### **Spatial Indexes**

| Index Type | Point Query | Range Query | Nearest Neighbor | Use Case |
|------------|-------------|-------------|------------------|----------|
| **R-Tree** | O(log n) | O(log n + k) | O(log n) | Geographic data |
| **Quad-Tree** | O(log n) | O(log n + k) | O(log n) | 2D spatial data |
| **Geohash** | O(1) | O(log n) | O(log n) | Location services |

---

## 📈 **SCALING STRATEGIES**

### **Vertical Scaling Strategies**

| Strategy | Scale Factor | Implementation | Use Case |
|----------|--------------|----------------|----------|
| **Vertical Scaling** | 2-10x | Hardware upgrade | Single instance performance |
| **Read Replicas** | 10-50x | Master-slave replication | Read-heavy workloads |
| **Sharding** | 100-1000x | Hash/range partitioning | Write-heavy workloads |
| **Partitioning** | 10-100x | Table partitioning | Large tables |

### **Horizontal Scaling Strategies**

| Strategy | Scale Factor | Implementation | Use Case |
|----------|--------------|----------------|----------|
| **Sharding** | 100-1000x | Consistent hashing | Data distribution |
| **Replication** | 10-100x | Master-slave | High availability |
| **Partitioning** | 100-1000x | Hash partitioning | Data distribution |
| **Auto-scaling** | 10-100x | Dynamic scaling | Variable workloads |
| **Indexing** | 10-100x | B-tree indexes | Query performance |
| **Caching** | 10-100x | In-memory cache | Frequently accessed data |

### **Advanced Scaling Strategies**

| Strategy | Scale Factor | Implementation | Use Case |
|----------|--------------|----------------|----------|
| **Consistent Hashing** | 100-1000x | Consistent hashing | Data distribution |
| **Multi-DC Replication** | 10-100x | Multi-DC replication | Geographic distribution |
| **Compression** | 2-10x | Columnar compression | Storage optimization |
| **Batch Operations** | 10-100x | Bulk operations | High throughput |
| **Time-based Sharding** | 100-1000x | Time-based sharding | Data distribution |
| **Downsampling** | 10-100x | Time-based aggregation | Long-term storage |
| **Retention Policies** | 10-100x | TTL-based deletion | Storage management |

### **Consensus Algorithms**

| Algorithm | Use Case | Complexity | Examples |
|-----------|----------|------------|----------|
| **Paxos** | Distributed consensus | High | Google Chubby, ZooKeeper |
| **Raft** | Distributed consensus | Medium | etcd, Consul, MongoDB |
| **Gossip** | Eventual consistency | Low | Cassandra, DynamoDB |
| **Vector Clocks** | Causal consistency | Medium | DynamoDB, Riak |
| **CRDTs** | Conflict resolution | Low | Riak, Redis CRDTs |

### **Availability & Failover Characteristics**

| Storage Type | Native | Max with Scaling | Failure Recovery |
|--------------|--------|------------------|------------------|
| **RDBMS** | 99.9% | 99.99% | Automatic failover |
| **Key-Value** | 99.95% | 99.999% | Sub-second failover |
| **Document** | 99.9% | 99.99% | Automatic failover |
| **Wide Column** | 99.99% | 99.999% | Geographic failover |
| **Time Series** | 99.9% | 99.99% | Automatic failover |
| **Object Store** | 99.99% | 99.999% | Regional failover |

### **Consistency Models & Trade-offs**

| Storage Type | Default | Configurable | Trade-offs |
|--------------|---------|--------------|------------|
| **RDBMS** | Linearizable | Read committed, repeatable read | Performance vs consistency |
| **Key-Value** | Eventual | Strong, causal, session | Consistency vs availability |
| **Document** | Eventual | Read concern levels | Consistency vs performance |
| **Wide Column** | Eventual | Quorum reads/writes | Consistency vs latency |
| **Time Series** | Eventual | Time-based consistency | Consistency vs performance |

### **Backup & Recovery Methods**

| Storage Type | Method | Recovery Time | Frequency |
|--------------|--------|---------------|-----------|
| **RDBMS** | Full + incremental | Hours | Daily |
| **Key-Value** | Snapshot + WAL | Minutes | Daily |
| **Document** | Oplog replay | Minutes | Daily |
| **Wide Column** | SSTable backup | Hours | Daily |
| **Time Series** | Time-based backup | Minutes | Daily |
| **Object Store** | Cross-region copy | Hours | Daily |

### **Storage Tiering Strategy**

| Tier | Access Pattern | Latency | Cost | Migration Trigger |
|------|----------------|---------|------|-------------------|
| **Hot** | Frequent | < 10ms | High | Active data |
| **Warm** | Occasional | 10-100ms | Medium | Recent data |
| **Cold** | Rare | 100ms-1s | Low | Historical data |
| **Archive** | Compliance | 1s-1min | Very Low | Long-term retention |

### **Storage Capacity Scaling**

| Storage Type | Single Instance | Clustered | Total Capacity |
|--------------|----------------|-----------|----------------|
| **RDBMS** | 1-10TB | 100TB-1PB | 1PB+ |
| **Key-Value** | 100GB-1TB | 10TB-100TB | 100TB+ |
| **Document** | 1-10TB | 100TB-1PB | 1PB+ |
| **Wide Column** | 10-100TB | 1PB-10PB | 10PB+ |
| **Time Series** | 1-10TB | 100TB-1PB | 1PB+ |
| **Object Store** | 1-10TB | 1PB-100PB | 100PB+ |

### **Performance Characteristics**

| Storage Type | Read Throughput | Write Throughput | Concurrent Connections |
|--------------|----------------|------------------|----------------------|
| **RDBMS** | 10K-100K ops/sec | 1K-10K ops/sec | 10K-100K |
| **Key-Value** | 100K-1M ops/sec | 100K-1M ops/sec | 100K-1M |
| **Document** | 10K-100K ops/sec | 10K-100K ops/sec | 10K-100K |
| **Wide Column** | 10K-100K ops/sec | 100K-1M ops/sec | 10K-100K |
| **Time Series** | 10K-100K ops/sec | 100K-1M ops/sec | 10K-100K |
| **Object Store** | 100-1K ops/sec | 100-1K ops/sec | 1K-10K |
## ⚠️ **COMMON PITFALLS**

### **RDBMS Pitfalls**
- **N+1 Query Problem**: Multiple queries instead of joins
- **Missing Indexes**: No indexes on frequently queried columns
- **Connection Pool Exhaustion**: Too many database connections
- **Long-Running Transactions**: Transactions holding locks too long

### **Key-Value Store Pitfalls**
- **Memory Exhaustion**: Running out of memory
- **Hot Keys**: Uneven key distribution
- **Network Partition**: Split-brain scenarios
- **Cache Stampede**: Multiple requests for same expired key

### **Document Store Pitfalls**
- **Large Documents**: Documents exceeding 16MB
- **Missing Indexes**: No indexes on queried fields
- **Schema Drift**: Inconsistent document structures
- **Embedded Array Growth**: Unbounded array growth

### **Wide Column Store Pitfalls**
- **Poor Partition Key Design**: Uneven data distribution
- **Wide Rows**: Too many columns per row
- **Read Repair Overhead**: Frequent consistency repairs
- **Compaction Pressure**: Insufficient compaction resources

### **Time Series DB Pitfalls**
- **Cardinality Explosion**: Too many unique time series
- **Retention Policy Issues**: Incorrect data lifecycle
- **Query Time Range**: Very large time ranges
- **Downsampling Configuration**: Incorrect aggregation intervals

## 🎯 **KEY TAKEAWAYS**

1. **Choose storage based on access patterns, not just data structure**
2. **Consider consistency requirements vs. performance needs**
3. **Plan for scaling from day one**
4. **Use appropriate indexing strategies for your workload**
5. **Monitor and optimize based on actual usage patterns**
6. **Consider operational complexity and team expertise**
7. **Plan for data lifecycle and retention policies**
8. **Implement comprehensive backup and recovery procedures**
9. **Establish monitoring and alerting for operational visibility**
10. **Plan for zero-downtime maintenance procedures**

---

*This summary provides quick reference for data storage systems. Use it for rapid revision and decision-making during system design discussions.*
