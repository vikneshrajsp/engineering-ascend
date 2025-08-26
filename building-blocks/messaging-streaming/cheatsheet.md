---
title: Cheatsheet
layout: default
grand_parent: Building Blocks
parent: Messaging Streaming
---

# Message Queuing & Streaming Systems - Cheat Sheet
## One-Page Quick Reference for System Design

## 🚀 **QUICK SELECTION GUIDE**

### **Messaging Type Selection**
```
Point-to-Point Communication? → Message Queues
One-to-Many Broadcasting? → Publish-Subscribe
Persistent Event Logs? → Event Streaming
Real-time Data Processing? → Real-time Processing
```

### **Delivery Requirements**
```
Reliability Critical? → Exactly-once delivery
High Throughput? → At-least-once delivery
Low Latency? → At-most-once delivery
Ordering Important? → Global or partition ordering
```

---

## 📊 **PERFORMANCE COMPARISON**

<div class="table-wrapper">

<th>Messaging Type</th>
<th>Latency</th>
<th>Throughput</th>
<th>Reliability</th>
<th>Ordering</th>
<th>Complexity</th>
<th>Cost</th>
<th>Best For</th>

**Message Queues**
1-100ms
10K-1M msg/sec
High
Partition
Low
Low
Task processing

**Pub-Sub**
1-50ms
10K-500K msg/sec
Medium
None
Medium
Low
Event broadcasting

**Event Streaming**
1-10ms
100K-10M events/sec
Very High
Global/Partition
High
Medium
Event sourcing

**Real-time Processing**
1-1000ms
10K-1M events/sec
High
Time-based
High
High
Stream analytics

</div>
---

## 🔧 **MESSAGING CHARACTERISTICS**

### **Message Queues**
```
Architecture: Point-to-point, guaranteed delivery
Performance: 1-100ms latency, 10K-1M msg/sec
Scaling: Queue partitioning, consumer groups
Use Cases: Task processing, request buffering
```

### **Publish-Subscribe**
```
Architecture: One-to-many, topic-based routing
Performance: 1-50ms latency, 10K-500K msg/sec
Scaling: Topic partitioning, fan-out distribution
Use Cases: Event broadcasting, notifications
```

### **Event Streaming**
```
Architecture: Persistent logs, event sourcing
Performance: 1-10ms latency, 100K-10M events/sec
Scaling: Partition scaling, replay capability
Use Cases: Event sourcing, real-time analytics
```

### **Real-time Processing**
```
Architecture: Stream processing, stateful operations
Performance: 1-1000ms latency, 10K-1M events/sec
Scaling: Operator parallelism, state partitioning
Use Cases: Stream analytics, fraud detection
```

---

## 📈 **DELIVERY PATTERNS**

### **At-Most-Once Delivery**
- Messages may be lost, no duplicates
- Highest throughput, lowest latency
- Fire-and-forget, no acknowledgments
- Use cases: Non-critical notifications, metrics

### **At-Least-Once Delivery**
- Messages guaranteed delivery, may have duplicates
- Medium throughput, reliable delivery
- Acknowledgments, retry mechanisms
- Use cases: Most business applications, data processing

### **Exactly-Once Delivery**
- Messages delivered exactly once
- Lower throughput, highest reliability
- Idempotency, deduplication
- Use cases: Financial transactions, critical operations

---

## 🔄 **MESSAGE ORDERING**

### **Global Ordering**
- All messages in strict order
- Lower throughput, higher latency
- Single partition, sequential processing
- Use cases: Financial transactions, audit trails

### **Partition Ordering**
- Messages ordered within partitions
- Higher throughput, parallel processing
- Partitioned streams, key-based routing
- Use cases: Most streaming applications

### **No Ordering**
- No guarantee on message order
- Highest throughput, lowest latency
- Parallel processing, no ordering constraints
- Use cases: Independent events, notifications

---

## 🚀 **BACKPRESSURE HANDLING**

### **Reactive Backpressure**
- Consumer controls flow rate
- Adaptive throughput, resource efficient
- Pull-based consumption, flow control
- Use cases: Variable load scenarios

### **Buffering Backpressure**
- Buffer messages during high load
- Smooth throughput, memory usage
- In-memory buffers, disk spilling
- Use cases: Burst traffic handling

### **Drop Backpressure**
- Drop messages during overload
- Consistent latency, data loss
- Circuit breakers, load shedding
- Use cases: Real-time systems, non-critical data

---

## 🎯 **DECISION FRAMEWORK**

### **Workload Analysis**
```
Task Processing? → Message Queues
Event Broadcasting? → Pub-Sub
Event Sourcing? → Event Streaming
Real-time Analytics? → Real-time Processing
```

### **Scale Requirements**
```
Small Scale (< 1K msg/sec)? → Message Queues
Medium Scale (1K-100K msg/sec)? → Pub-Sub
Large Scale (100K-1M msg/sec)? → Event Streaming
Very Large Scale (> 1M msg/sec)? → Real-time Processing
```

### **Reliability Requirements**
```
Critical Operations? → Exactly-once delivery
Business Applications? → At-least-once delivery
Non-critical Data? → At-most-once delivery
```

---

## 🔍 **OPTIMIZATION TECHNIQUES**

### **Message Optimization**
- **Compression**: 50-90% size reduction
- **Serialization**: Efficient data formats (Avro, Protocol Buffers)
- **Batching**: Group multiple messages
- **Pipelining**: Overlap processing and I/O

### **Network Optimization**
- **Connection Pooling**: Reuse connections
- **Keep-Alive**: Maintain persistent connections
- **Compression**: Reduce network overhead
- **Load Balancing**: Distribute load evenly

### **Storage Optimization**
- **Sequential Writes**: Optimize for append operations
- **Compaction**: Remove duplicate/obsolete data
- **Indexing**: Fast message retrieval
- **Tiered Storage**: Hot/warm/cold data management

---

## 📋 **IMPLEMENTATION CHECKLIST**

### **Message Queues**
- [ ] Queue partitioning configured?
- [ ] Consumer groups set up?
- [ ] Dead letter queues implemented?
- [ ] Message persistence configured?
- [ ] Monitoring and alerting set up?

### **Publish-Subscribe**
- [ ] Topic partitioning configured?
- [ ] Subscription filtering implemented?
- [ ] Fan-out distribution optimized?
- [ ] Backpressure handling configured?
- [ ] Message routing optimized?

### **Event Streaming**
- [ ] Stream partitioning configured?
- [ ] Replay capability implemented?
- [ ] Event ordering configured?
- [ ] State management set up?
- [ ] Checkpointing configured?

### **Real-time Processing**
- [ ] Operator parallelism configured?
- [ ] State partitioning implemented?
- [ ] Windowing operations set up?
- [ ] Fault tolerance configured?
- [ ] Resource allocation optimized?

---

## 🚨 **COMMON PITFALLS**

### **Message Queues**
- **Message Loss**: Not implementing proper acknowledgments
- **Consumer Bottlenecks**: Not scaling consumers properly
- **Memory Issues**: Not handling large message volumes
- **Ordering Issues**: Not considering message ordering requirements

### **Publish-Subscribe**
- **Fan-out Overhead**: Too many subscribers per topic
- **Message Filtering**: Inefficient subscription patterns
- **Geographic Distribution**: Not considering latency
- **Subscription Management**: Not handling dynamic subscriptions

### **Event Streaming**
- **Partition Imbalance**: Uneven distribution across partitions
- **State Management**: Not handling large state volumes
- **Replay Performance**: Not optimizing for replay scenarios
- **Event Ordering**: Not considering ordering requirements

### **Real-time Processing**
- **State Management**: Not handling state partitioning
- **Checkpointing**: Not optimizing checkpoint frequency
- **Backpressure**: Not implementing proper flow control
- **Resource Allocation**: Not optimizing resource usage

---

## 📚 **QUICK REFERENCE**

### **Performance Formulas**
```
Throughput = Messages per second
Latency = End-to-end processing time
Reliability = (Successful deliveries / Total messages) × 100
Scalability = Linear scaling with partitions
```

### **Scaling Patterns**
```
Horizontal Scaling: Add more partitions/consumers
Vertical Scaling: Increase resources per node
Geographic Scaling: Multi-region deployment
Auto-scaling: Dynamic resource allocation
```

### **Common Patterns**
```
Producer-Consumer: Asynchronous processing
Fan-Out: One-to-many message distribution
Event Sourcing: State reconstruction from events
CQRS: Command Query Responsibility Segregation
```

---

*Use this cheatsheet for quick reference during interviews and system design discussions. Remember: choose messaging type based on delivery requirements, not just familiarity.*
