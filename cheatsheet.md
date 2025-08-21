# System Design Interview Cheatsheet
## Senior Staff Software Engineer - Quick Reference

## 🏗️ **BUILDING BLOCKS DECISION TREE**

### **Data Storage**
```
ACID Required? → RDBMS (MySQL, PostgreSQL)
High Performance? → Key-Value (Redis, DynamoDB)
Analytics? → Wide Column (Cassandra, HBase)
Time Series? → InfluxDB, TimescaleDB
Search? → Elasticsearch, Solr
Large Files? → Object Store (S3, GCS)
```

### **Compute & Processing**
```
I/O Bound? → Async Processing + CPU
CPU Bound? → Multi-core + Algorithm Optimization
Parallel Workload? → GPU + Distributed Computing
Batch Processing? → MapReduce + Stream Processing
Real-time? → Event-Driven + Stream Processing
```

### **Messaging & Communication**
```
Reliable Delivery? → Message Queue (RabbitMQ, SQS)
Broadcasting? → Pub/Sub (Kafka, SNS)
Event Sourcing? → Event Streaming (Kafka, Pulsar)
Real-time? → WebSocket + Stream Processing
```

### **Networking & Load Balancing**
```
Layer 7 Routing? → Application Load Balancer
High Performance? → Network Load Balancer
Global Distribution? → CDN + Geographic Load Balancing
Microservices? → Service Mesh (Istio, Linkerd)
```

### **Caching Strategy**
```
Fastest Access? → In-Memory Cache (Redis)
Shared Access? → Distributed Cache (Redis Cluster)
Global Distribution? → CDN
Multi-level? → L1 (Memory) + L2 (Redis) + L3 (Database)
```

---

## 📊 **TRADE-OFF MATRIX**

| Dimension | Option A | Option B | When to Choose A | When to Choose B |
|-----------|----------|----------|------------------|------------------|
| **Consistency** | Strong | Eventual | Financial, User Accounts | Social Media, Content |
| **Availability** | High | Low | Social Media, Content | Financial, Critical Systems |
| **Performance** | Low Latency | High Throughput | Real-time, User Experience | Batch Processing, Analytics |
| **Scalability** | Vertical | Horizontal | Small Scale, Simple | Large Scale, Complex |
| **Complexity** | Simple | Complex | MVP, Small Team | Enterprise, Large Team |
| **Cost** | Low | High | Startup, Budget Constrained | Enterprise, Performance Critical |

---

## 🚀 **SCALING PATTERNS**

### **Horizontal Scaling**
- **Sharding**: Data distribution across nodes
- **Partitioning**: Logical data separation
- **Replication**: Data redundancy and availability
- **Load Balancing**: Traffic distribution

### **Vertical Scaling**
- **CPU**: More cores, higher clock speeds
- **Memory**: Larger RAM, faster access
- **Storage**: SSDs, NVMe drives
- **Network**: Higher bandwidth, lower latency

---

## 🔄 **CONSISTENCY MODELS**

### **Strong Consistency**
- **Linearizability**: All operations appear atomic
- **Sequential Consistency**: Operations appear in sequential order
- **Use Cases**: Financial transactions, user accounts

### **Eventual Consistency**
- **Monotonic Reads**: Reads never go backwards
- **Monotonic Writes**: Writes appear in order
- **Use Cases**: Social media feeds, content delivery

---

## 📈 **PERFORMANCE OPTIMIZATION**

### **Read-Heavy Workloads**
- **Optimizations**: Read replicas, caching, indexing
- **Storage Types**: RDBMS with B-tree indexes, read-optimized NoSQL

### **Write-Heavy Workloads**
- **Optimizations**: Write buffering, LSM trees, async processing
- **Storage Types**: LSM-based stores, time series databases

### **Mixed Workloads**
- **Strategies**: Read/write separation, caching layers, background processing
- **Architecture**: Multi-tier storage, intelligent routing

---

## 🔍 **INDEXING STRATEGIES**

### **In-Memory Indexes**
- **Hash Tables**: O(1) lookup, memory-intensive
- **B-Trees**: Balanced performance, range queries
- **Skip Lists**: Probabilistic structure, good for concurrent access

### **On-Disk Indexes**
- **B-Tree Variants**: Optimized for disk access patterns
- **LSM Trees**: Write-optimized, background compaction
- **Bitmap Indexes**: Boolean operations, compression

---

## 🎯 **INTERVIEW FRAMEWORK**

### **1. Requirements Clarification**
- Functional requirements
- Non-functional requirements (scale, performance, availability)
- Constraints and assumptions

### **2. High-Level Design**
- System components and their relationships
- Data flow and API design
- Technology choices and rationale

### **3. Deep Dive**
- Detailed component design
- Data models and schemas
- Scaling and performance considerations

### **4. Trade-off Discussion**
- Consistency vs. availability
- Performance vs. complexity
- Cost vs. performance

### **5. Failure Scenarios**
- Single points of failure
- Disaster recovery
- Monitoring and alerting

---

## 🔧 **COMMON PATTERNS**

### **Design Patterns**
- **CQRS**: Command and query responsibility separation
- **Event Sourcing**: State reconstruction from events
- **Saga Pattern**: Distributed transaction coordination
- **Circuit Breaker**: Failure detection and isolation
- **Bulkhead**: Resource isolation and failure containment

### **Architecture Patterns**
- **Microservices**: Service-oriented architecture
- **Event-Driven**: Reactive system design
- **Lambda Architecture**: Batch + stream processing
- **Kappa Architecture**: Stream-only processing

---

## 📊 **MONITORING METRICS**

### **Key Performance Indicators**
- **Latency**: Response time percentiles (P50, P95, P99)
- **Throughput**: Operations per second
- **Availability**: Uptime percentage
- **Error Rate**: Failure percentage
- **Resource Utilization**: CPU, memory, disk, network

### **Business Metrics**
- **User Experience**: Page load time, transaction success rate
- **Business Impact**: Revenue, user engagement, conversion rates
- **Operational**: Cost per request, resource efficiency

---

## ⚠️ **RED FLAGS TO AVOID**

### **Design Issues**
- Single point of failure
- No scalability plan
- Ignoring consistency requirements
- Over-engineering simple problems
- No monitoring or observability

### **Interview Mistakes**
- Jumping to solutions without understanding requirements
- Not considering trade-offs
- Ignoring failure scenarios
- No performance considerations
- Not asking clarifying questions

---

## 🎯 **KEY TAKEAWAYS**

1. **Always start with requirements clarification**
2. **Consider trade-offs explicitly**
3. **Plan for failure from day one**
4. **Monitor everything, optimize based on data**
5. **Choose simplicity over complexity when possible**
6. **Think about operational aspects**
7. **Consider cost implications of design choices**

---

*Use this cheatsheet as a quick reference during interviews and system design discussions. Remember: there are no perfect solutions, only appropriate trade-offs for specific contexts.*
