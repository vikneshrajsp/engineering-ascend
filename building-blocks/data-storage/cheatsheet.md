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
- **Team Expertise:**
  - What's the team's experience with different storage types?
  - What's the learning curve for new technologies?
  - Do we have operational expertise?

- **Infrastructure Constraints:**
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
| **Financial Transactions** | RDBMS | Event Sourcing | ACID vs audit trail |
| **Real-time Analytics** | Time Series DB | Wide Column Store | Time queries vs general analytics |
| **Search Functionality** | Text Search Engine | Document Store | Search quality vs general purpose |
| **Configuration Management** | Key-Value Store | Document Store | Simple access vs structured data |
| **Log Storage** | Time Series DB | Object Store | Query patterns vs cost |
| **User Profiles** | Document Store | RDBMS | Schema flexibility vs relationships |
| **Caching Layer** | Key-Value Store | In-Memory DB | Performance vs persistence |

---

## 📊 **COMPREHENSIVE DECISION CRITERIA**

### **Decision Dimensions & Weighting**

| Dimension | Weight | Description | Critical For |
|-----------|--------|-------------|--------------|
| **Consistency Requirements** | 25% | ACID vs eventual consistency | Financial, user data |
| **Performance Requirements** | 20% | Latency & throughput needs | Real-time systems |
| **Scalability Needs** | 20% | Horizontal vs vertical scaling | High-growth systems |
| **Query Complexity** | 15% | Simple lookups vs complex queries | Analytics, reporting |
| **Schema Flexibility** | 10% | Fixed vs evolving schemas | Rapid development |
| **Operational Complexity** | 10% | Team expertise & maintenance | Production systems |

### **Detailed Comparison Matrix**

| Storage Type | Consistency | Performance | Scalability | Query Flexibility | Schema Flexibility | Operational Complexity | Best For |
|--------------|-------------|-------------|-------------|-------------------|-------------------|------------------------|----------|
| **RDBMS** | ✅ Linearizable | ⚠️ 1-10ms | ❌ Vertical Only | ✅ Complex SQL | ❌ Schema Migration | ⚠️ Moderate | ACID Transactions |
| **Key-Value** | ⚠️ Eventual | ✅ 0.1-1ms | ✅ Horizontal | ❌ Simple Only | ✅ No Schema | ✅ Simple | High-Performance Lookups |
| **Wide Column** | ❌ Eventual | ✅ 1-10ms | ✅ Horizontal | ⚠️ Limited | ⚠️ Column Families | ⚠️ Moderate | Analytics/OLAP |
| **Document** | ❌ Eventual | ✅ 1-10ms | ✅ Horizontal | ✅ Rich Queries | ✅ Flexible | ⚠️ Moderate | Flexible Data Models |
| **Time Series** | ❌ Eventual | ✅ 1-10ms | ✅ Horizontal | ⚠️ Time-Based | ⚠️ Time Schema | ⚠️ Moderate | Time-Ordered Data |
| **Text Search** | ❌ Eventual | ⚠️ 10-100ms | ✅ Horizontal | ✅ Search Queries | ⚠️ Index Schema | ❌ Complex | Full-Text Search |
| **Object Store** | ❌ Eventual | ❌ 100ms-1s | ✅ Horizontal | ❌ Metadata Only | ✅ No Schema | ✅ Simple | Large Binary Files |

### **Scenario-Specific Decision Framework**

#### **Scenario 1: File Metadata Storage**
**Question**: "Should I use RDBMS or Document Store for file metadata?"

**Decision Framework**:
```
Consistency Requirements:
├─ ACID transactions needed? → RDBMS
├─ Eventual consistency acceptable? → Document Store
└─ Consider: File operations atomicity

Schema Evolution:
├─ Fixed metadata structure? → RDBMS
├─ Evolving metadata fields? → Document Store
└─ Consider: Future metadata additions

Query Patterns:
├─ Complex joins with users/permissions? → RDBMS
├─ Simple metadata lookups? → Document Store
└─ Consider: Query complexity requirements

Final Decision:
├─ RDBMS: When ACID + complex relationships + fixed schema
└─ Document Store: When flexibility + simple queries + evolving schema
```

#### **Scenario 2: User Session Data**
**Question**: "Should I use Key-Value Store or Document Store for user sessions?"

**Decision Framework**:
```
Performance Requirements:
├─ Sub-millisecond access needed? → Key-Value Store
├─ 1-10ms acceptable? → Document Store
└─ Consider: Session access frequency

Data Structure:
├─ Simple key-value pairs? → Key-Value Store
├─ Complex session objects? → Document Store
└─ Consider: Session data complexity

Query Patterns:
├─ Simple session retrieval? → Key-Value Store
├─ Session analytics needed? → Document Store
└─ Consider: Future query requirements

Final Decision:
├─ Key-Value Store: When performance + simple data + basic queries
└─ Document Store: When flexibility + complex data + analytics
```

#### **Scenario 3: E-commerce Product Catalog**
**Question**: "Should I use RDBMS or Document Store for product catalog?"

**Decision Framework**:
```
Data Relationships:
├─ Complex product-category relationships? → RDBMS
├─ Simple product documents? → Document Store
└─ Consider: Data normalization needs

Schema Evolution:
├─ Fixed product attributes? → RDBMS
├─ Dynamic product attributes? → Document Store
└─ Consider: Product variety across categories

Query Patterns:
├─ Complex inventory joins? → RDBMS
├─ Product search & filtering? → Document Store
└─ Consider: Query performance requirements

Final Decision:
├─ RDBMS: When complex relationships + fixed schema + inventory management
└─ Document Store: When flexible schema + search requirements + product variety
```

#### **Scenario 4: Real-time Analytics Dashboard**
**Question**: "Should I use Time Series DB or Wide Column Store for real-time analytics?"

**Decision Framework**:
```
Time-Based Queries:
├─ Primarily time-range queries? → Time Series DB
├─ Multi-dimensional analytics? → Wide Column Store
└─ Consider: Query pattern distribution

Data Volume:
├─ High-frequency time-series data? → Time Series DB
├─ Large-scale analytical data? → Wide Column Store
└─ Consider: Data ingestion rates

Query Complexity:
├─ Simple aggregations over time? → Time Series DB
├─ Complex analytical queries? → Wide Column Store
└─ Consider: Query sophistication needs

Final Decision:
├─ Time Series DB: When time-centric + high frequency + simple analytics
└─ Wide Column Store: When multi-dimensional + complex analytics + large scale
```

#### **Scenario 5: Configuration Management**
**Question**: "Should I use Key-Value Store or Document Store for configuration management?"

**Decision Framework**:
```
Access Patterns:
├─ Simple key-based lookups? → Key-Value Store
├─ Complex configuration objects? → Document Store
└─ Consider: Configuration complexity

Update Frequency:
├─ Frequent individual updates? → Key-Value Store
├─ Batch configuration updates? → Document Store
└─ Consider: Update granularity

Query Requirements:
├─ Simple configuration retrieval? → Key-Value Store
├─ Configuration analytics needed? → Document Store
└─ Consider: Future query needs

Final Decision:
├─ Key-Value Store: When simple configs + frequent updates + basic queries
└─ Document Store: When complex configs + batch updates + analytics
```

#### **Scenario 6: User Profile Management**
**Question**: "Should I use RDBMS or Document Store for user profiles?"

**Decision Framework**:
```
Data Relationships:
├─ Complex user-role-permission relationships? → RDBMS
├─ Self-contained user documents? → Document Store
└─ Consider: Data normalization needs

Profile Flexibility:
├─ Fixed user attributes? → RDBMS
├─ Dynamic user preferences? → Document Store
└─ Consider: User customization needs

Query Patterns:
├─ Complex user analytics & reporting? → RDBMS
├─ Simple profile lookups & updates? → Document Store
└─ Consider: Query complexity requirements

Final Decision:
├─ RDBMS: When complex relationships + fixed schema + analytics
└─ Document Store: When flexible profiles + simple queries + user customization
```

---

## 🔍 **DATA STRUCTURES & TRANSFORMATIONS**

### **Comprehensive Data Structure Table**
| Storage Type | Primary Data Structure | Secondary Structures | Transformations | Time Complexity |
|--------------|------------------------|---------------------|-----------------|-----------------|
| **RDBMS** | B+ Tree Indexes | Hash Tables (Buffer Pool), LRU Lists, WAL | Buffer Pool → WAL → B+ Tree → Disk | O(log n) search, O(1) buffer access |
| **Key-Value** | Hash Tables + LSM Trees | Skiplist (MemTable), Bloom Filters, SSTables | Skiplist → SSTable → LSM Tree | O(1) hash lookup, O(log n) skiplist |
| **Wide Column** | Column-Oriented Storage | B-Tree Indexes, Compression Algorithms | Raw Data → Column Groups → Compressed | O(log n) index, O(n) compression |
| **Document** | B-Tree Indexes | JSON/BSON Parser, Field Mappers | JSON → BSON → Index Entries | O(log n) index, O(n) parsing |
| **Time Series** | Time Buckets | Columnar Storage, Compression | Timestamp → Bucket → Column → Compressed | O(1) bucketing, O(n) compression |
| **Text Search** | Inverted Indexes | Skip Lists, Hash Tables, Compression | Text → Tokens → Inverted Index | O(n) tokenization, O(log n) search |
| **Object Store** | Hash-based Distribution | Metadata Indexes, Compression | File → Chunks → Distributed → Compressed | O(1) hash, O(n) compression |

### **Data Structure Transformation Details**

#### **RDBMS Pipeline**
```
Write: SQL → Parse Tree → Buffer Pool → WAL → B+ Tree → Disk
Read: Query → Query Plan → B+ Tree → Buffer Pool → Result
- Hash Table: O(1) page lookup in buffer pool
- LRU List: O(1) eviction decisions
- B+ Tree: O(log n) index operations
- WAL: O(1) sequential append
```

#### **Key-Value Pipeline**
```
Write: Key-Value → Hash Table → Skiplist → SSTable → LSM Tree
Read: Key → Hash Table → Bloom Filter → SSTable → Value
- Hash Table: O(1) duplicate detection
- Skiplist: O(log n) in-memory ordering
- Bloom Filter: O(k) false positive checking
- SSTable: O(log n) binary search
```

#### **Text Search Pipeline**
```
Indexing: Document → Tokens → Term Dictionary → Posting Lists
Search: Query → Terms → Posting Lists → Intersection → Results
- Tokenization: O(n) character processing
- Hash Table: O(1) term dictionary lookup
- Skip Lists: O(log n) posting list access
- Intersection: O(n) merge complexity
```

### **Performance Characteristics by Data Structure**
| Data Structure | Lookup | Insert/Delete | Range Queries | Memory Usage | Best For |
|----------------|--------|---------------|---------------|--------------|----------|
| **Hash Tables** | O(1) | O(1) | ❌ | O(n) | Exact lookups |
| **B-Trees** | O(log n) | O(log n) | ✅ | O(n) | Ordered data |
| **Skip Lists** | O(log n) | O(log n) | ✅ | O(n) | Concurrent access |
| **LSM Trees** | O(log n) | O(1) | ✅ | O(n) | Write-heavy workloads |
| **Inverted Indexes** | O(log n) | O(log n) | ✅ | O(n) | Text search |
| **Columnar Storage** | O(log n) | O(n) | ✅ | O(n) | Analytics |

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

### **When Asked About Storage Selection:**
1. **Start with Requirements**: "What are the consistency, performance, and scalability requirements?"
2. **Analyze Access Patterns**: "Is this read-heavy, write-heavy, or mixed workload?"
3. **Consider Data Relationships**: "Are there complex relationships or simple key-value lookups?"
4. **Evaluate Schema Evolution**: "Will the data structure change frequently?"
5. **Assess Operational Complexity**: "What's the team's expertise and maintenance capacity?"

### **Quick Decision Framework for Interviews:**
```
Step 1: "What's the primary requirement?"
├─ ACID Transactions → RDBMS
├─ High Performance → Key-Value Store
├─ Complex Analytics → Wide Column Store
├─ Full-Text Search → Text Search Engine
├─ Time-Series Data → Time Series DB
├─ Large Files → Object Store
└─ Flexible Schema → Document Store

Step 2: "What are the trade-offs?"
├─ Consistency vs Performance
├─ Complexity vs Scalability
├─ Flexibility vs Structure
└─ Cost vs Features

Step 3: "What's the operational impact?"
├─ Team expertise required
├─ Maintenance overhead
├─ Scaling complexity
└─ Cost implications
```

### **Common Interview Scenarios & Quick Answers:**

#### **"Design a URL Shortener"**
- **Storage**: Key-Value Store (Redis) + RDBMS (PostgreSQL)
- **Reasoning**: Fast lookups + analytics + ACID for user data
- **Trade-offs**: Performance vs analytics capabilities

#### **"Design a Social Media Feed"**
- **Storage**: Document Store (MongoDB) + Time Series DB (InfluxDB)
- **Reasoning**: Flexible post structure + engagement metrics
- **Trade-offs**: Schema flexibility vs analytics performance

#### **"Design an E-commerce Platform"**
- **Storage**: RDBMS (PostgreSQL) + Document Store (MongoDB)
- **Reasoning**: ACID for orders + flexible product catalog
- **Trade-offs**: Transaction safety vs product variety

#### **"Design a Real-time Analytics Dashboard"**
- **Storage**: Time Series DB (InfluxDB) + Key-Value Store (Redis)
- **Reasoning**: Time-ordered data + real-time aggregations
- **Trade-offs**: Query performance vs real-time updates

### **Red Flags to Avoid in Interviews:**
- ❌ **"I'll use MongoDB for everything"** - No consideration of requirements
- ❌ **"RDBMS can't scale"** - Misunderstanding of scaling strategies
- ❌ **"We'll figure out the schema later"** - No upfront planning
- ❌ **"Performance doesn't matter"** - Ignoring user experience
- ❌ **"We don't need ACID"** - Not considering data integrity

### **Green Flags for Interviews:**
- ✅ **"Let me understand the requirements first"** - Systematic approach
- ✅ **"What are the access patterns?"** - Thinking about usage
- ✅ **"Let me consider the trade-offs"** - Balanced decision making
- ✅ **"What's the team's expertise?"** - Operational awareness
- ✅ **"How will this scale?"** - Forward-thinking approach

---

## 📋 **QUICK REFERENCE: COMMON SCENARIOS**

### **Storage Selection by Use Case**

| Use Case | Primary Storage | Secondary Storage | Key Decision Factors |
|----------|----------------|-------------------|---------------------|
| **User Authentication** | RDBMS | Key-Value Cache | ACID + performance |
| **Session Management** | Key-Value Store | - | Performance + TTL |
| **Product Catalog** | Document Store | Text Search | Flexibility + search |
| **Order Management** | RDBMS | Message Queue | ACID + event sourcing |
| **User Profiles** | Document Store | RDBMS | Flexibility vs relationships |
| **File Storage** | Object Store | Document Store | Large files + metadata |
| **Analytics Dashboard** | Time Series DB | Wide Column Store | Time queries + analytics |
| **Configuration** | Key-Value Store | Document Store | Simple access + complexity |
| **Log Storage** | Time Series DB | Object Store | Time queries + cost |
| **Search Engine** | Text Search Engine | Object Store | Search quality + documents |
| **Real-time Chat** | Document Store | Message Queue | Flexibility + real-time |
| **Gaming Leaderboard** | Key-Value Store | Time Series DB | Performance + historical |
| **IoT Data** | Time Series DB | Object Store | Time queries + large volumes |
| **Content Management** | Document Store | Text Search | Flexibility + search |
| **Financial Transactions** | RDBMS | Event Store | ACID + audit trail |

### **Storage Selection by Data Pattern**

| Data Pattern | Storage Choice | Reasoning | Trade-offs |
|--------------|----------------|-----------|------------|
| **Simple Key-Value** | Key-Value Store | O(1) lookups | Limited querying |
| **Complex Documents** | Document Store | Schema flexibility | Eventual consistency |
| **Time-Series Data** | Time Series DB | Time-optimized queries | Limited general use |
| **Relational Data** | RDBMS | ACID + joins | Scaling complexity |
| **Large Binary Files** | Object Store | Cost-effective storage | High latency |
| **Searchable Content** | Text Search Engine | Rich search capabilities | Storage overhead |
| **Analytical Data** | Wide Column Store | Column-oriented queries | Complex modeling |

## ⚠️ **RED FLAGS TO AVOID**

### **Technical Red Flags:**
- ❌ **Single point of failure** - No redundancy or failover
- ❌ **No scaling plan** - Assuming current solution will scale indefinitely
- ❌ **Ignoring consistency requirements** - Not considering data integrity needs
- ❌ **Over-engineering simple problems** - Using complex solutions for simple use cases
- ❌ **No monitoring strategy** - Flying blind in production

### **Decision-Making Red Flags:**
- ❌ **"We'll use what we know"** - Not considering requirements
- ❌ **"Performance doesn't matter"** - Ignoring user experience
- ❌ **"We can always migrate later"** - Underestimating migration complexity
- ❌ **"One size fits all"** - Using same storage for everything
- ❌ **"We don't need ACID"** - Not understanding data integrity needs

### **Operational Red Flags:**
- ❌ **No backup strategy** - Assuming data won't be lost
- ❌ **No disaster recovery plan** - No plan for system failures
- ❌ **Ignoring team expertise** - Choosing technology team can't maintain
- ❌ **No cost analysis** - Not considering total cost of ownership
- ❌ **No compliance consideration** - Ignoring regulatory requirements

---

## 📋 **COMPREHENSIVE DECISION CHECKLIST**

### **Requirements Analysis**
- [ ] **Consistency Requirements**: ACID vs eventual consistency defined?
- [ ] **Performance Requirements**: Latency & throughput targets specified?
- [ ] **Scalability Requirements**: Expected growth & scaling strategy?
- [ ] **Query Requirements**: Simple lookups vs complex queries?
- [ ] **Schema Requirements**: Fixed vs evolving data structure?
- [ ] **Operational Requirements**: Team expertise & maintenance capacity?

### **Technical Constraints**
- [ ] **Data Volume**: Current & projected data size?
- [ ] **Access Patterns**: Read vs write heavy, frequency?
- [ ] **Query Patterns**: Point queries vs range queries vs analytics?
- [ ] **Data Relationships**: Simple vs complex relationships?
- [ ] **Update Patterns**: Individual vs batch updates?
- [ ] **Geographic Distribution**: Single vs multi-region?

### **Operational Considerations**
- [ ] **Team Expertise**: Current skills vs learning curve?
- [ ] **Infrastructure**: Cloud vs on-premise constraints?
- [ ] **Cost Constraints**: Budget vs performance requirements?
- [ ] **Compliance**: Regulatory requirements (GDPR, HIPAA, etc.)?
- [ ] **Integration**: Existing system compatibility?
- [ ] **Vendor Lock-in**: Proprietary vs open-source preference?

### **Risk Assessment**
- [ ] **Single Point of Failure**: High availability requirements?
- [ ] **Data Loss**: Backup & recovery procedures?
- [ ] **Performance Degradation**: Monitoring & alerting strategy?
- [ ] **Scalability Limits**: Growth ceiling considerations?
- [ ] **Operational Complexity**: Maintenance overhead?
- [ ] **Technology Maturity**: Production readiness assessment?

### **Decision Validation**
- [ ] **Proof of Concept**: Technical feasibility validated?
- [ ] **Performance Testing**: Meets latency/throughput requirements?
- [ ] **Scalability Testing**: Handles expected load?
- [ ] **Cost Analysis**: Total cost of ownership calculated?
- [ ] **Risk Mitigation**: Contingency plans in place?
- [ ] **Team Buy-in**: Stakeholder approval obtained?

---

## 🎯 **50 SYSTEM DESIGN INTERVIEW QUESTIONS**

### **Search & Analytics Questions**

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

#### **6. Design a Search Engine**
- **Storage Choice**: Text Search (Elasticsearch) + Object Store (GCS)
- **Trade-offs**: Elasticsearch for search, GCS for web pages
- **Scaling**: Document-based sharding, distributed indexing

#### **7. Design a Payment System (Stripe)**
- **Storage Choice**: RDBMS (PostgreSQL) + Message Queue (Kafka)
- **Trade-offs**: PostgreSQL for ACID transactions, Kafka for events
- **Scaling**: Account-based sharding, read replicas

#### **8. Design a Recommendation System**
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

### **E-commerce & Storage Questions**

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

## ❓ **FREQUENTLY ASKED QUESTIONS (FAQs)**

### **Common Misconceptions & Quick Answers**

#### **Q1: "RDBMS can't scale - they're only for small applications"**
**A: FALSE** - RDBMS can scale significantly:
- **Vertical Scaling**: 2-10x (hardware upgrades)
- **Horizontal Scaling**: 100-1000x (read replicas + sharding)
- **Real Examples**: Facebook MySQL (1B+ users), YouTube (1B+ requests/day)
- **Scaling Limits**: Petabytes of data, millions of users

#### **Q2: "NoSQL is always faster than RDBMS"**
**A: FALSE** - Performance depends on use case:
- **Simple Lookups**: NoSQL (0.1-1ms) vs RDBMS (1-10ms)
- **Complex Queries**: RDBMS (1-10ms) vs NoSQL (10-100ms)
- **Analytics**: RDBMS (10ms-1s) vs NoSQL (100ms-10s)
- **When RDBMS Wins**: Complex joins, ACID transactions, analytical queries

#### **Q3: "Document stores are schema-less - you can store anything"**
**A: PARTIALLY TRUE** - Schema flexibility has trade-offs:
- **Flexible**: Add fields without migration
- **Constraints**: Application-level validation required
- **Indexing**: Schema changes affect query performance
- **Best Practice**: Design schema upfront, use consistent field naming

#### **Q4: "Time series databases are just regular databases with timestamps"**
**A: FALSE** - Highly specialized for time data:
- **Storage**: Time-based partitioning, columnar compression
- **Queries**: Time-range optimization, aggregation functions
- **Lifecycle**: Automatic downsampling, retention policies
- **Performance**: Write-optimized, time-ordered storage

#### **Q5: "Object stores are just file systems in the cloud"**
**A: FALSE** - Object stores have unique characteristics:
- **Distributed**: Geographic distribution, erasure coding
- **API-Based**: RESTful APIs, versioning, lifecycle policies
- **Cost Optimization**: Storage tiering, compression, pay-per-use
- **Scalability**: 1PB-100PB+ capacity, 1000-10000x scaling

## 🚀 **SCALING MECHANISMS BY STORAGE TYPE**

### **RDBMS Scaling Strategies**
| Strategy | Scale Factor | Implementation | Use Case |
|----------|--------------|----------------|----------|
| **Vertical Scaling** | 2-10x | Hardware upgrade | Single instance performance |
| **Read Replicas** | 10-50x | Master-slave replication | Read-heavy workloads |
| **Sharding** | 100-1000x | Hash/range partitioning | Write-heavy workloads |
| **Partitioning** | 10-100x | Table partitioning | Large tables |
| **Connection Pooling** | 10-100x | Connection management | Connection limits |
| **Caching** | 10-100x | Application cache | Frequently accessed data |

### **Key-Value Store Scaling Strategies**
| Strategy | Scale Factor | Implementation | Use Case |
|----------|--------------|----------------|----------|
| **Horizontal Scaling** | 100-1000x | Consistent hashing | Even distribution |
| **Replication** | 10-100x | Master-slave | High availability |
| **Partitioning** | 100-1000x | Hash partitioning | Data distribution |
| **Auto-scaling** | 10-100x | Dynamic scaling | Variable workloads |
| **Caching Layers** | 10-100x | Multi-level cache | Performance optimization |

### **Document Store Scaling Strategies**
| Strategy | Scale Factor | Implementation | Use Case |
|----------|--------------|----------------|----------|
| **Horizontal Scaling** | 100-1000x | Sharding | Data distribution |
| **Replication** | 10-100x | Replica sets | High availability |
| **Indexing** | 10-100x | B-tree indexes | Query performance |
| **Caching** | 10-100x | In-memory cache | Frequently accessed data |
| **Aggregation** | 10-100x | Pipeline processing | Analytics queries |

### **Wide Column Store Scaling Strategies**
| Strategy | Scale Factor | Implementation | Use Case |
|----------|--------------|----------------|----------|
| **Horizontal Scaling** | 100-1000x | Consistent hashing | Data distribution |
| **Replication** | 10-100x | Multi-DC replication | Geographic distribution |
| **Compression** | 2-10x | Columnar compression | Storage optimization |
| **Batch Operations** | 10-100x | Bulk operations | High throughput |
| **Caching** | 10-100x | Row/key cache | Performance optimization |

### **Time Series DB Scaling Strategies**
| Strategy | Scale Factor | Implementation | Use Case |
|----------|--------------|----------------|----------|
| **Horizontal Scaling** | 100-1000x | Time-based sharding | Data distribution |
| **Compression** | 5-20x | Columnar compression | Storage optimization |
| **Downsampling** | 10-100x | Time-based aggregation | Long-term storage |
| **Retention Policies** | 10-100x | TTL-based deletion | Storage management |
| **Caching** | 10-100x | Hot data caching | Recent data access |

## 🔄 **CONSENSUS & DISTRIBUTION ALGORITHMS**

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

## 🛡️ **SYSTEM CHARACTERISTICS**

### **Availability by Storage Type**
| Storage Type | Native | Max with Scaling | Failure Recovery |
|--------------|--------|------------------|------------------|
| **RDBMS** | 99.9% | 99.99% | Automatic failover |
| **Key-Value** | 99.95% | 99.999% | Sub-second failover |
| **Document** | 99.9% | 99.99% | Automatic failover |
| **Wide Column** | 99.99% | 99.999% | Geographic failover |
| **Time Series** | 99.9% | 99.99% | Automatic failover |
| **Object Store** | 99.99% | 99.999% | Regional failover |

### **Consistency Models**
| Storage Type | Default | Configurable | Trade-offs |
|--------------|---------|--------------|------------|
| **RDBMS** | Linearizable | Read committed, repeatable read | Performance vs consistency |
| **Key-Value** | Eventual | Strong, causal, session | Consistency vs availability |
| **Document** | Eventual | Read concern levels | Consistency vs performance |
| **Wide Column** | Eventual | Quorum reads/writes | Consistency vs latency |
| **Time Series** | Eventual | Time-based consistency | Consistency vs performance |

## 💾 **BACKUP & ARCHIVAL STRATEGIES**

### **Backup Methods by Storage Type**
| Storage Type | Method | Recovery Time | Frequency | Special Considerations |
|--------------|--------|---------------|-----------|----------------------|
| **RDBMS** | Full + incremental | Hours | Daily | Point-in-time recovery |
| **Key-Value** | Snapshot + WAL | Minutes | Daily | Memory state + disk state |
| **Document** | Oplog replay | Minutes | Daily | Replica set consistency |
| **Wide Column** | SSTable backup | Hours | Daily | Consistency across nodes |
| **Time Series** | Time-based backup | Minutes | Daily | Retention policy alignment |
| **Object Store** | Cross-region copy | Hours | Daily | Geographic distribution |

### **Storage Tiering Strategy**
| Tier | Access Pattern | Latency | Cost | Migration Trigger |
|------|----------------|---------|------|-------------------|
| **Hot Storage** | Frequent access | < 10ms | High | Active data |
| **Warm Storage** | Occasional access | 10-100ms | Medium | Recent data |
| **Cold Storage** | Rare access | 100ms-1s | Low | Historical data |
| **Archive Storage** | Compliance only | 1s-1min | Very Low | Long-term retention |

### **Data Lifecycle Management**
| Phase | Duration | Storage Type | Access Pattern | Cost Optimization |
|-------|----------|--------------|----------------|-------------------|
| **Active** | 0-30 days | Hot storage | Frequent | Performance optimization |
| **Recent** | 30-90 days | Warm storage | Occasional | Balanced cost/performance |
| **Historical** | 90 days-1 year | Cold storage | Rare | Storage optimization |
| **Archive** | 1+ years | Archive storage | Compliance | Cost optimization |

## 📊 **DATA VOLUME CAPACITIES & LIMITS**

### **Storage Capacity by Type**
| Storage Type | Single Instance | Clustered | Total Capacity | Scaling Factor |
|--------------|----------------|-----------|----------------|----------------|
| **RDBMS** | 1-10TB | 100TB-1PB | 1PB+ | 100-1000x |
| **Key-Value** | 100GB-1TB | 10TB-100TB | 100TB+ | 100-1000x |
| **Document** | 1-10TB | 100TB-1PB | 1PB+ | 100-1000x |
| **Wide Column** | 10-100TB | 1PB-10PB | 10PB+ | 100-1000x |
| **Time Series** | 1-10TB | 100TB-1PB | 1PB+ | 100-1000x |
| **Object Store** | 1-10TB | 1PB-100PB | 100PB+ | 1000-10000x |

### **Performance Limits**
| Storage Type | Read Throughput | Write Throughput | Concurrent Connections | Query Complexity |
|--------------|----------------|------------------|----------------------|------------------|
| **RDBMS** | 10K-100K ops/sec | 1K-10K ops/sec | 10K-100K | Complex SQL |
| **Key-Value** | 100K-1M ops/sec | 100K-1M ops/sec | 100K-1M | Simple lookups |
| **Document** | 10K-100K ops/sec | 10K-100K ops/sec | 10K-100K | Rich queries |
| **Wide Column** | 10K-100K ops/sec | 100K-1M ops/sec | 10K-100K | Analytics |
| **Time Series** | 10K-100K ops/sec | 100K-1M ops/sec | 10K-100K | Time queries |
| **Object Store** | 100-1K ops/sec | 100-1K ops/sec | 1K-10K | Large files |

## 🔀 **DATA PARTITIONING & SHARDING STRATEGIES**

### **RDBMS Partitioning & Sharding**

#### **Table Partitioning Strategies**
| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Range Partitioning** | Partition by value ranges | Time-series data, ordered data | Efficient range queries | Potential hotspots |
| **Hash Partitioning** | Partition by hash function | Even distribution | Balanced load | Range queries inefficient |
| **List Partitioning** | Partition by specific values | Categorical data | Direct partition access | Limited flexibility |
| **Composite Partitioning** | Multiple partitioning methods | Complex requirements | Flexibility | Increased complexity |

**Implementation Examples:**
```
PostgreSQL Range Partitioning:
CREATE TABLE orders (
    order_id SERIAL,
    order_date DATE,
    amount DECIMAL
) PARTITION BY RANGE (order_date);

CREATE TABLE orders_2023 PARTITION OF orders
    FOR VALUES FROM ('2023-01-01') TO ('2024-01-01');

MySQL Hash Partitioning:
CREATE TABLE users (
    user_id INT,
    username VARCHAR(50)
) PARTITION BY HASH(user_id) PARTITIONS 4;
```

#### **RDBMS Sharding Strategies**
| Strategy | Mechanism | Implementation | Use Case | Complexity |
|----------|-----------|----------------|----------|------------|
| **Hash-based Sharding** | Consistent hashing | User ID, UUID | Even distribution | Medium |
| **Range-based Sharding** | Key ranges | Time-series, ordered data | Efficient range queries | High |
| **Directory-based Sharding** | Lookup table | Complex requirements | Flexibility | High |
| **Composite Sharding** | Multiple strategies | Complex data | Optimal distribution | Very High |

**Sharding Implementation:**
```
Hash-based Sharding Example:
Shard 0: user_id % 4 = 0
Shard 1: user_id % 4 = 1
Shard 2: user_id % 4 = 2
Shard 3: user_id % 4 = 3

Range-based Sharding Example:
Shard 0: user_id 1-1000000
Shard 1: user_id 1000001-2000000
Shard 2: user_id 2000001-3000000
Shard 3: user_id 3000001-4000000
```

#### **RDBMS Sharding Challenges & Solutions**
| Challenge | Problem | Solution | Implementation |
|-----------|---------|----------|----------------|
| **Cross-shard Queries** | Joins across shards | Denormalization, application-level joins | Query routing, data duplication |
| **Transaction Management** | ACID across shards | Distributed transactions, eventual consistency | 2PC, saga pattern |
| **Data Distribution** | Uneven shard load | Rebalancing, dynamic sharding | Consistent hashing, virtual nodes |
| **Schema Changes** | Coordinated schema updates | Blue-green deployment, versioning | Migration scripts, backward compatibility |

### **Key-Value Store Partitioning & Sharding**

#### **Consistent Hashing Implementation**
```
Hash Ring Structure:
Node A: 0-1000
Node B: 1001-2000
Node C: 2001-3000
Node D: 3001-4000

Key Distribution:
Key "user:123" → Hash(123) = 1500 → Node B
Key "user:456" → Hash(456) = 2500 → Node C

Virtual Nodes (VNodes):
Node A: 0-500, 2000-2500
Node B: 501-1000, 2501-3000
Node C: 1001-1500, 3001-3500
Node D: 1501-2000, 3501-4000
```

#### **Redis Cluster Partitioning**
| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Hash Slots** | 16384 hash slots | Even distribution | Automatic rebalancing | Limited flexibility |
| **Key Tags** | Custom hash tags | Related data | Co-location | Manual management |
| **Hash Functions** | CRC16, MD5 | Custom distribution | Flexibility | Implementation complexity |

**Redis Cluster Implementation:**
```
Hash Slot Assignment:
Slot 0-5461: Node A
Slot 5462-10922: Node B
Slot 10923-16383: Node C

Key Distribution:
Key "user:123" → CRC16("user:123") % 16384 = 5000 → Node A
Key "user:456" → CRC16("user:456") % 16384 = 10000 → Node B
```

#### **DynamoDB Partitioning**
| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Hash Partition Key** | Single partition key | Simple access patterns | Even distribution | Limited query flexibility |
| **Composite Key** | Partition + Sort key | Range queries | Efficient range queries | Design complexity |
| **GSI Partitioning** | Global secondary indexes | Multiple access patterns | Query flexibility | Additional cost |

**DynamoDB Implementation:**
```
Hash Partition Key:
Table: Users
Partition Key: user_id
Distribution: Even across partitions

Composite Key:
Table: Orders
Partition Key: user_id
Sort Key: order_date
Distribution: User-based with time ordering
```

### **Document Store Partitioning & Sharding**

#### **MongoDB Sharding Strategies**
| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Hash-based Sharding** | Hash of shard key | Even distribution | Balanced load | Range queries inefficient |
| **Range-based Sharding** | Shard key ranges | Range queries | Efficient range queries | Potential hotspots |
| **Zoned Sharding** | Geographic zones | Multi-region | Geographic distribution | Complexity |

**MongoDB Sharding Implementation:**
```
Hash-based Sharding:
Shard Key: {user_id: "hashed"}
Distribution: Even across shards

Range-based Sharding:
Shard Key: {user_id: 1}
Distribution: User ID ranges across shards

Zoned Sharding:
Zone: "us-east" → Shards 0, 1
Zone: "us-west" → Shards 2, 3
Zone: "eu-west" → Shards 4, 5
```

#### **MongoDB Shard Key Selection**
| Criteria | Considerations | Best Practices | Examples |
|----------|---------------|----------------|----------|
| **Cardinality** | High cardinality | Avoid low-cardinality keys | user_id, order_id |
| **Write Distribution** | Even write distribution | Avoid monotonically increasing | UUID, hash-based |
| **Query Patterns** | Support common queries | Include query fields | {user_id: 1, order_date: -1} |
| **Chunk Size** | Optimal chunk size | 64MB-128MB chunks | Balanced distribution |

#### **MongoDB Chunk Management**
```
Chunk Distribution:
Chunk 1: user_id 1-1000000 → Shard A
Chunk 2: user_id 1000001-2000000 → Shard B
Chunk 3: user_id 2000001-3000000 → Shard C

Chunk Splitting:
Large chunk → Split into smaller chunks
Chunk Migration: Automatic rebalancing
Jumbo Chunks: Manual intervention required
```

### **Wide Column Store Partitioning & Sharding**

#### **Cassandra Partitioning Strategies**
| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Hash Partitioning** | Consistent hashing | Even distribution | Balanced load | Range queries difficult |
| **Composite Partitioning** | Multiple partition keys | Complex requirements | Flexibility | Design complexity |
| **Time-based Partitioning** | Time buckets | Time-series data | Time-based queries | Time-based hotspots |

**Cassandra Partition Key Design:**
```
Hash Partitioning:
CREATE TABLE users (
    user_id UUID,
    username text,
    email text,
    PRIMARY KEY (user_id)
);

Composite Partition Key:
CREATE TABLE user_posts (
    user_id UUID,
    post_id UUID,
    content text,
    created_at timestamp,
    PRIMARY KEY ((user_id, post_id), created_at)
);

Time-based Partitioning:
CREATE TABLE sensor_data (
    sensor_id UUID,
    bucket text,  -- Daily bucket: 2023-01-01
    timestamp timestamp,
    value double,
    PRIMARY KEY ((sensor_id, bucket), timestamp)
);
```

#### **Cassandra Token Ring Distribution**
```
Token Ring (vNodes):
Node A: Tokens [0, 1000, 2000, 3000]
Node B: Tokens [250, 1250, 2250, 3250]
Node C: Tokens [500, 1500, 2500, 3500]
Node D: Tokens [750, 1750, 2750, 3750]

Partition Distribution:
Partition Key Hash → Token → Node
user:123 → Hash(123) = 1500 → Node B
user:456 → Hash(456) = 2500 → Node C
```

#### **Cassandra Partitioning Best Practices**
| Practice | Description | Implementation | Benefits |
|----------|-------------|----------------|----------|
| **High Cardinality** | Unique partition keys | UUID, hash-based keys | Even distribution |
| **Avoid Hotspots** | Prevent single partition overload | Composite keys, time buckets | Balanced load |
| **Query Optimization** | Design for query patterns | Denormalization, materialized views | Performance |
| **Compaction Strategy** | Choose appropriate compaction | Size-tiered, leveled compaction | Storage efficiency |

### **Time Series Database Partitioning & Sharding**

#### **InfluxDB Partitioning Strategies**
| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Time-based Partitioning** | Time buckets | Time-series data | Efficient time queries | Time-based hotspots |
| **Tag-based Partitioning** | Tag values | Multi-dimensional data | Flexible queries | Cardinality explosion |
| **Measurement Partitioning** | Different measurements | Logical separation | Clear organization | Cross-measurement queries |

**InfluxDB Implementation:**
```
Time-based Partitioning:
Measurement: cpu_usage
Tags: host, region
Time Field: timestamp
Partition: Daily buckets

Tag-based Partitioning:
Measurement: sensor_data
Tags: sensor_id, location, type
Partition: By sensor_id ranges

Measurement Partitioning:
cpu_usage → Partition 1
memory_usage → Partition 2
disk_usage → Partition 3
```

#### **Time Series Sharding Strategies**
| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Time-based Sharding** | Time ranges per shard | Historical data | Efficient time queries | Time-based hotspots |
| **Metric-based Sharding** | Different metrics per shard | Diverse metrics | Logical separation | Cross-metric queries |
| **Hybrid Sharding** | Time + metric combination | Complex requirements | Flexibility | Complexity |

**Time Series Sharding Implementation:**
```
Time-based Sharding:
Shard 1: 2023-01-01 to 2023-06-30
Shard 2: 2023-07-01 to 2023-12-31
Shard 3: 2024-01-01 to 2024-06-30

Metric-based Sharding:
Shard 1: CPU, Memory metrics
Shard 2: Disk, Network metrics
Shard 3: Application metrics

Hybrid Sharding:
Shard 1: CPU metrics (2023)
Shard 2: CPU metrics (2024)
Shard 3: Memory metrics (2023)
Shard 4: Memory metrics (2024)
```

### **Text Search Engine Partitioning & Sharding**

#### **Elasticsearch Sharding Strategies**
| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Document-based Sharding** | Hash of document ID | Even distribution | Balanced load | Cross-document queries |
| **Routing-based Sharding** | Custom routing | Related documents | Co-location | Manual management |
| **Time-based Sharding** | Time indices | Time-series data | Time-based queries | Time-based hotspots |

**Elasticsearch Implementation:**
```
Document-based Sharding:
Index: users
Shards: 5
Routing: Hash(document_id) % 5

Routing-based Sharding:
Index: user_posts
Routing: user_id
Co-location: All posts by same user in same shard

Time-based Sharding:
Index Pattern: logs-YYYY.MM.DD
Shards per index: 3
Time-based queries: Efficient range queries
```

#### **Elasticsearch Index Management**
| Strategy | Description | Implementation | Benefits |
|----------|-------------|----------------|----------|
| **Index Aliases** | Logical index names | Alias → Multiple indices | Zero-downtime reindexing |
| **Index Lifecycle** | Automated management | Hot → Warm → Cold → Delete | Cost optimization |
| **Shard Allocation** | Custom allocation | Node attributes, awareness | Performance optimization |
| **Replica Management** | High availability | Replica allocation, recovery | Fault tolerance |

### **Object Store Partitioning & Sharding**

#### **S3-style Partitioning Strategies**
| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Hash-based Partitioning** | Hash of object key | Even distribution | Balanced load | No logical grouping |
| **Prefix-based Partitioning** | Key prefixes | Logical organization | Efficient listing | Potential hotspots |
| **Time-based Partitioning** | Time in key | Time-series objects | Time-based access | Time-based hotspots |

**S3 Implementation:**
```
Hash-based Partitioning:
Object Key: Hash(filename) + filename
Distribution: Even across partitions

Prefix-based Partitioning:
Object Key: user_id/date/filename
Organization: Logical grouping by user and date

Time-based Partitioning:
Object Key: YYYY/MM/DD/filename
Access: Efficient time-based queries
```

#### **Object Store Sharding Strategies**
| Strategy | Mechanism | Use Case | Advantages | Disadvantages |
|----------|-----------|----------|------------|---------------|
| **Bucket-based Sharding** | Different buckets | Logical separation | Clear organization | Cross-bucket operations |
| **Region-based Sharding** | Geographic regions | Global distribution | Low latency | Cross-region costs |
| **Storage-tier Sharding** | Different storage classes | Cost optimization | Cost efficiency | Access pattern changes |

## ⚠️ **COMMON PITFALLS BY STORAGE TYPE**

### **RDBMS Pitfalls**
| Pitfall | Description | Impact | Mitigation |
|---------|-------------|--------|-----------|
| **N+1 Query Problem** | Multiple queries instead of joins | Performance degradation | Use eager loading, batch queries |
| **Missing Indexes** | No indexes on frequently queried columns | Slow queries | Analyze query patterns, add indexes |
| **Connection Pool Exhaustion** | Too many database connections | Application failures | Configure connection pooling |
| **Long-Running Transactions** | Transactions holding locks too long | Deadlocks, poor performance | Keep transactions short |
| **Schema Lock Contention** | DDL operations blocking queries | Application downtime | Use online DDL, maintenance windows |

### **Key-Value Store Pitfalls**
| Pitfall | Description | Impact | Mitigation |
|---------|-------------|--------|-----------|
| **Memory Exhaustion** | Running out of memory | Service failures | Configure eviction policies |
| **Hot Keys** | Uneven key distribution | Performance bottlenecks | Use key distribution strategies |
| **Network Partition** | Split-brain scenarios | Data inconsistency | Use quorum-based operations |
| **Cache Stampede** | Multiple requests for same expired key | Performance degradation | Use cache warming, background refresh |
| **TTL Management** | Inconsistent expiration handling | Memory leaks | Implement proper TTL cleanup |

### **Document Store Pitfalls**
| Pitfall | Description | Impact | Mitigation |
|---------|-------------|--------|-----------|
| **Large Documents** | Documents exceeding 16MB | Performance degradation | Normalize large documents |
| **Missing Indexes** | No indexes on queried fields | Slow queries | Create appropriate indexes |
| **Schema Drift** | Inconsistent document structures | Query complexity | Design schema upfront |
| **Embedded Array Growth** | Unbounded array growth | Performance degradation | Use pagination, limit array size |
| **Write Concern Issues** | Insufficient write acknowledgment | Data loss | Configure appropriate write concerns |

### **Wide Column Store Pitfalls**
| Pitfall | Description | Impact | Mitigation |
|---------|-------------|--------|-----------|
| **Poor Partition Key Design** | Uneven data distribution | Hotspots | Design partition keys carefully |
| **Wide Rows** | Too many columns per row | Performance degradation | Normalize wide rows |
| **Read Repair Overhead** | Frequent consistency repairs | Performance degradation | Tune read repair frequency |
| **Compaction Pressure** | Insufficient compaction resources | Performance degradation | Monitor and tune compaction |
| **Network Partition Handling** | Poor partition recovery | Data inconsistency | Configure appropriate consistency levels |

### **Time Series DB Pitfalls**
| Pitfall | Description | Impact | Mitigation |
|---------|-------------|--------|-----------|
| **Cardinality Explosion** | Too many unique time series | Memory usage | Limit cardinality, use tags wisely |
| **Retention Policy Issues** | Incorrect data lifecycle | Storage costs | Configure appropriate retention policies |
| **Query Time Range** | Very large time ranges | Performance degradation | Use appropriate time windows |
| **Downsampling Configuration** | Incorrect aggregation intervals | Data loss | Configure downsampling carefully |
| **Write Buffer Issues** | Insufficient write buffering | Performance degradation | Tune write buffer size |

## 📊 **COMPREHENSIVE DECISION FRAMEWORK**

### **Systematic Decision Process**

#### **Phase 1: Requirements Analysis (30 minutes)**
```
Step 1: Functional Requirements
├─ What data are we storing?
├─ What operations do we need?
├─ What queries will be performed?
└─ What are the access patterns?

Step 2: Non-Functional Requirements
├─ Performance requirements (latency, throughput)
├─ Scalability requirements (growth projections)
├─ Consistency requirements (ACID vs eventual)
├─ Availability requirements (uptime, disaster recovery)
└─ Compliance requirements (GDPR, HIPAA, etc.)

Step 3: Operational Requirements
├─ Team expertise and learning curve
├─ Infrastructure constraints (cloud vs on-premise)
├─ Budget and cost constraints
├─ Timeline and implementation complexity
└─ Integration with existing systems
```

#### **Phase 2: Technical Evaluation (45 minutes)**
```
Step 1: Data Model Analysis
├─ Data structure complexity
├─ Relationship requirements
├─ Schema evolution needs
└─ Query pattern analysis

Step 2: Performance Analysis
├─ Read vs write patterns
├─ Query complexity requirements
├─ Latency and throughput needs
└─ Scaling requirements

Step 3: Technical Constraints
├─ Infrastructure limitations
├─ Integration requirements
├─ Security and compliance needs
└─ Operational complexity tolerance
```

#### **Phase 3: Decision Matrix (15 minutes)**

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
- **✅ 9-10**: Excellent fit for the requirement
- **⚠️ 5-8**: Good fit with some trade-offs
- **❌ 1-4**: Poor fit, significant compromises needed

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
