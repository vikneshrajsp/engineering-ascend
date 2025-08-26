---
title: Cheatsheet
layout: default
grand_parent: Building Blocks
parent: Caching Performance
---

# Caching & Performance Systems - Cheat Sheet
## One-Page Quick Reference for Interviews

## 🎯 **QUICK DECISION FRAMEWORK**

### **When to Use Caching**
```
Performance Issues? → Consider Caching
├─ High Latency? → Add Caching Layer
├─ Low Throughput? → Optimize Cache Strategy
├─ High Memory Usage? → Implement Cache Eviction
└─ Network Bottlenecks? → Use CDN Caching
```

### **Cache Type Selection**
```
Data Access Pattern?
├─ Frequently Read, Rarely Written → Application Cache
├─ Global Distribution Needed → CDN Cache
├─ High Availability Required → Distributed Cache
├─ Hardware Optimization → CPU/Memory Cache
└─ Storage Performance → Storage Cache
```

### **Cache Strategy Selection**
```
Data Characteristics?
├─ Static Data → Long TTL, Aggressive Caching
├─ Dynamic Data → Short TTL, Smart Invalidation
├─ User-Specific → Session-Based Caching
├─ Computationally Expensive → Result Caching
└─ Frequently Updated → Write-Through Caching
```

---

## 📊 **CACHE LAYERS QUICK REFERENCE**

### **Cache Hierarchy**
<div class="table-wrapper">
<table>
<thead>
<tr>
<th>Layer</th>
<th>Size</th>
<th>Latency</th>
<th>Use Case</th>
</tr>
</thead>
<tbody>
<tr>
<td>**L1 Cache**</td>
<td>32-64KB</td>
<td>1-3 cycles</td>
<td>CPU instructions/data</td>
</tr>
<tr>
<td>**L2 Cache**</td>
<td>256KB-1MB</td>
<td>10-20 cycles</td>
<td>Unified cache</td>
</tr>
<tr>
<td>**L3 Cache**</td>
<td>8-32MB</td>
<td>40-80 cycles</td>
<td>Shared across cores</td>
</tr>
<tr>
<td>**Memory Cache**</td>
<td>1-100GB</td>
<td>100-1000ns</td>
<td>Application data</td>
</tr>
<tr>
<td>**Distributed Cache**</td>
<td>1TB+</td>
<td>1-10ms</td>
<td>Multi-node systems</td>
</tr>
<tr>
<td>**CDN Cache**</td>
<td>Unlimited</td>
<td>10-100ms</td>
<td>Global content</td>
</tr>
<tr>
<td>Cache Type</td>
<td>Read Latency</td>
<td>Write Latency</td>
<td>Throughput</td>
<td>Memory Usage</td>
</tr>
<tr>
<td>------------</td>
<td>--------------</td>
<td>---------------</td>
<td>------------</td>
<td>--------------</td>
</tr>
<tr>
<td>**CPU Cache**</td>
<td>1-40ns</td>
<td>1-40ns</td>
<td>100M+ ops/sec</td>
<td>32KB-32MB</td>
</tr>
<tr>
<td>**Memory Cache**</td>
<td>100-1000ns</td>
<td>100-1000ns</td>
<td>1M+ ops/sec</td>
<td>1-100GB</td>
</tr>
<tr>
<td>**Redis**</td>
<td>1-10ms</td>
<td>1-10ms</td>
<td>100K+ ops/sec</td>
<td>1-1TB</td>
</tr>
<tr>
<td>**Distributed Cache**</td>
<td>1-50ms</td>
<td>1-50ms</td>
<td>10K+ ops/sec</td>
<td>1TB+</td>
</tr>
<tr>
<td>**CDN Cache**</td>
<td>10-100ms</td>
<td>N/A</td>
<td>1K+ ops/sec</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Pattern</td>
<td>Consistency</td>
<td>Performance</td>
<td>Complexity</td>
<td>Use Case</td>
</tr>
<tr>
<td>---------</td>
<td>-------------</td>
<td>-------------</td>
<td>------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Cache-Aside**</td>
<td>Eventual</td>
<td>High</td>
<td>Low</td>
<td>Simple applications</td>
</tr>
<tr>
<td>**Write-Through**</td>
<td>Strong</td>
<td>Medium</td>
<td>Low</td>
<td>Critical data</td>
</tr>
<tr>
<td>**Write-Behind**</td>
<td>Eventual</td>
<td>Very High</td>
<td>High</td>
<td>High-throughput systems</td>
</tr>
<tr>
<td>**Refresh-Ahead**</td>
<td>Eventual</td>
<td>High</td>
<td>Medium</td>
<td>Predictive caching</td>
</tr>
<tr>
<td>Strategy</td>
<td>Implementation</td>
<td>Performance</td>
<td>Use Case</td>
</tr>
<tr>
<td>----------</td>
<td>----------------</td>
<td>-------------</td>
<td>----------</td>
</tr>
<tr>
<td>**TTL**</td>
<td>Automatic expiration</td>
<td>High</td>
<td>Time-sensitive data</td>
</tr>
<tr>
<td>**Event-Based**</td>
<td>Publish-subscribe</td>
<td>Medium</td>
<td>Real-time updates</td>
</tr>
<tr>
<td>**Version-Based**</td>
<td>Cache key versioning</td>
<td>High</td>
<td>Schema changes</td>
</tr>
<tr>
<td>**Manual**</td>
<td>Explicit invalidation</td>
<td>Low</td>
<td>Critical updates</td>
</tr>
<tr>
<td>Technique</td>
<td>Performance Gain</td>
<td>Implementation</td>
<td>Use Case</td>
</tr>
<tr>
<td>-----------</td>
<td>------------------</td>
<td>----------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Cache Warming**</td>
<td>20-50%</td>
<td>Pre-load data</td>
<td>Cold starts</td>
</tr>
<tr>
<td>**Stale-While-Revalidate**</td>
<td>50-80%</td>
<td>Return stale + update</td>
<td>High availability</td>
</tr>
<tr>
<td>**Cache Prefetching**</td>
<td>10-30%</td>
<td>Predict requests</td>
<td>Sequential access</td>
</tr>
<tr>
<td>**Connection Pooling**</td>
<td>30-60%</td>
<td>Reuse connections</td>
<td>Database caching</td>
</tr>
<tr>
<td>Technique</td>
<td>Throughput Gain</td>
<td>Implementation</td>
<td>Use Case</td>
</tr>
<tr>
<td>-----------</td>
<td>-----------------</td>
<td>----------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Batch Operations**</td>
<td>2-5x</td>
<td>Group operations</td>
<td>Bulk processing</td>
</tr>
<tr>
<td>**Pipeline Operations**</td>
<td>3-10x</td>
<td>Parallel processing</td>
<td>High concurrency</td>
</tr>
<tr>
<td>**Lock-Free Caching**</td>
<td>2-4x</td>
<td>Concurrent structures</td>
<td>Multi-threaded</td>
</tr>
<tr>
<td>**Compression**</td>
<td>20-50%</td>
<td>Reduce data size</td>
<td>Network caching</td>
</tr>
<tr>
<td>Technique</td>
<td>Memory Savings</td>
<td>Implementation</td>
<td>Use Case</td>
</tr>
<tr>
<td>-----------</td>
<td>----------------</td>
<td>----------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Memory Pooling**</td>
<td>30-60%</td>
<td>Reuse objects</td>
<td>Object creation</td>
</tr>
<tr>
<td>**Compression**</td>
<td>40-80%</td>
<td>Compress data</td>
<td>Large objects</td>
</tr>
<tr>
<td>**Eviction Policies**</td>
<td>Variable</td>
<td>LRU, LFU, TTL</td>
<td>Memory constraints</td>
</tr>
<tr>
<td>**Cache Partitioning**</td>
<td>Better utilization</td>
<td>Distribute load</td>
<td>Large datasets</td>
</tr>
<tr>
<td>Implementation</td>
<td>Performance</td>
<td>Scalability</td>
<td>Complexity</td>
<td>Best For</td>
</tr>
<tr>
<td>----------------</td>
<td>-------------</td>
<td>-------------</td>
<td>------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Redis**</td>
<td>Very High</td>
<td>High</td>
<td>Low</td>
<td>General purpose</td>
</tr>
<tr>
<td>**Memcached**</td>
<td>High</td>
<td>High</td>
<td>Low</td>
<td>Simple key-value</td>
</tr>
<tr>
<td>**In-Memory**</td>
<td>Very High</td>
<td>Low</td>
<td>Medium</td>
<td>Single application</td>
</tr>
<tr>
<td>**Distributed**</td>
<td>High</td>
<td>Very High</td>
<td>High</td>
<td>Multi-node systems</td>
</tr>
<tr>
<td>Policy</td>
<td>Algorithm</td>
<td>Performance</td>
<td>Best For</td>
</tr>
<tr>
<td>--------</td>
<td>-----------</td>
<td>-------------</td>
<td>----------</td>
</tr>
<tr>
<td>**LRU**</td>
<td>Least Recently Used</td>
<td>O(1)</td>
<td>Temporal locality</td>
</tr>
<tr>
<td>**LFU**</td>
<td>Least Frequently Used</td>
<td>O(log n)</td>
<td>Access patterns</td>
</tr>
<tr>
<td>**TTL**</td>
<td>Time-To-Live</td>
<td>O(1)</td>
<td>Time-sensitive data</td>
</tr>
<tr>
<td>**FIFO**</td>
<td>First-In-First-Out</td>
<td>O(1)</td>
<td>Simple scenarios</td>
</tr>
<tr>
<td>Metric</td>
<td>Target</td>
<td>Monitoring</td>
<td>Action</td>
</tr>
<tr>
<td>--------</td>
<td>--------</td>
<td>------------</td>
<td>--------</td>
</tr>
<tr>
<td>**Cache Hit Ratio**</td>
<td>>80%</td>
<td>Real-time</td>
<td>Optimize if <70%</td>
</tr>
<tr>
<td>**Average Latency**</td>
<td><10ms</td>
<td>P95, P99</td>
<td>Investigate if >50ms</td>
</tr>
<tr>
<td>**Throughput**</td>
<td>>10K ops/sec</td>
<td>Per second</td>
<td>Scale if <5K ops/sec</td>
</tr>
<tr>
<td>**Memory Usage**</td>
<td><80% capacity</td>
<td>Continuous</td>
<td>Evict if >90%</td>
</tr>
<tr>
<td>**Error Rate**</td>
<td><1%</td>
<td>Per minute</td>
<td>Alert if >5%</td>
</tr>
<tr>
<td>Hit Ratio</td>
<td>Performance</td>
<td>User Experience</td>
<td>Action</td>
</tr>
<tr>
<td>-----------</td>
<td>-------------</td>
<td>-----------------</td>
<td>--------</td>
</tr>
<tr>
<td>**90%+**</td>
<td>Excellent</td>
<td>Great</td>
<td>Monitor</td>
</tr>
<tr>
<td>**80-90%**</td>
<td>Good</td>
<td>Good</td>
<td>Optimize</td>
</tr>
<tr>
<td>**70-80%**</td>
<td>Acceptable</td>
<td>Fair</td>
<td>Improve</td>
</tr>
<tr>
<td>**<70%**</td>
<td>Poor</td>
<td>Bad</td>
<td>Major optimization</td>
</tr>
<tr>
<td>Use Case</td>
<td>Primary Cache</td>
<td>Secondary Cache</td>
<td>Key Decision Factors</td>
</tr>
<tr>
<td>----------</td>
<td>---------------</td>
<td>-----------------</td>
<td>---------------------</td>
</tr>
<tr>
<td>**Web Application**</td>
<td>Application Cache</td>
<td>CDN Cache</td>
<td>Performance + global distribution</td>
</tr>
<tr>
<td>**Mobile App**</td>
<td>Local Cache</td>
<td>Remote Cache</td>
<td>Offline capability + sync</td>
</tr>
<tr>
<td>**API Service**</td>
<td>Response Cache</td>
<td>Database Cache</td>
<td>Latency + throughput</td>
</tr>
<tr>
<td>**Real-time System**</td>
<td>In-Memory Cache</td>
<td>Distributed Cache</td>
<td>Speed + consistency</td>
</tr>
<tr>
<td>**Analytics Platform**</td>
<td>Result Cache</td>
<td>Query Cache</td>
<td>Computation cost + data size</td>
</tr>
<tr>
<td>**E-commerce**</td>
<td>Product Cache</td>
<td>Session Cache</td>
<td>Static data + user state</td>
</tr>
<tr>
<td>**Social Media**</td>
<td>Feed Cache</td>
<td>Media Cache</td>
<td>Personalization + content</td>
</tr>
<tr>
<td>**Gaming**</td>
<td>Game State Cache</td>
<td>Asset Cache</td>
<td>Real-time + resource loading</td>
</tr>
<tr>
<td>Data Pattern</td>
<td>Cache Choice</td>
<td>Reasoning</td>
<td>Trade-offs</td>
</tr>
<tr>
<td>--------------</td>
<td>--------------</td>
<td>-----------</td>
<td>------------</td>
</tr>
<tr>
<td>**Static Data**</td>
<td>Long TTL Cache</td>
<td>Rarely changes</td>
<td>Stale data risk</td>
</tr>
<tr>
<td>**Dynamic Data**</td>
<td>Short TTL Cache</td>
<td>Frequently changes</td>
<td>Cache miss penalty</td>
</tr>
<tr>
<td>**User-Specific**</td>
<td>Session Cache</td>
<td>User context</td>
<td>Memory usage</td>
</tr>
<tr>
<td>**Computationally Expensive**</td>
<td>Result Cache</td>
<td>High computation cost</td>
<td>Storage cost</td>
</tr>
<tr>
<td>**Frequently Accessed**</td>
<td>Hot Data Cache</td>
<td>Access patterns</td>
<td>Memory allocation</td>
</tr>
<tr>
<td>**Large Objects**</td>
<td>Compressed Cache</td>
<td>Storage efficiency</td>
<td>CPU overhead</td>
</tr>
</tbody>
</table>
</div>
---

## 🚀 **SCALING PATTERNS**

### **Horizontal Scaling**
- **Distributed Caching**: Multiple cache nodes
- **Consistent Hashing**: Even distribution
- **Cache Replication**: High availability
- **Load Balancing**: Even load distribution

### **Vertical Scaling**
- **Memory Expansion**: Larger cache capacity
- **CPU Optimization**: Better cache performance
- **Storage Optimization**: Faster cache storage
- **Network Optimization**: Reduced cache latency

---

## ⚖️ **CONSISTENCY MODELS**

### **Strong Consistency**
- **Write-Through**: Immediate consistency
- **Synchronous Replication**: All nodes updated
- **Use**: Critical data, financial transactions
- **Trade-off**: Higher latency

### **Eventual Consistency**
- **Write-Behind**: Background updates
- **Asynchronous Replication**: Eventual sync
- **Use**: Non-critical data, user preferences
- **Trade-off**: Temporary inconsistency

---

## 📈 **PERFORMANCE OPTIMIZATION**

### **Read-Heavy Workloads**
- Cache warming, aggressive caching, read replicas
- Performance: 80%+ hit ratio, <10ms latency

### **Write-Heavy Workloads**
- Write-through caching, batch operations, write buffering
- Performance: 50-70% hit ratio, <50ms latency

### **Mixed Workloads**
- Multi-layer caching, smart invalidation, adaptive TTL
- Performance: 70-90% hit ratio, <20ms latency

---

## 🔧 **COMMON IMPLEMENTATIONS**

### **In-Memory Caches**
- **Redis**: High-performance, feature-rich
- **Memcached**: Simple, fast, distributed
- **Hazelcast**: Java-based, distributed
- **Caffeine**: Java in-memory cache

### **Distributed Caches**
- **Redis Cluster**: Scalable, high availability
- **Hazelcast IMDG**: In-memory data grid
- **Apache Ignite**: Distributed computing platform
- **Infinispan**: Java-based, distributed

### **CDN Caches**
- **CloudFront**: AWS global CDN
- **Cloud CDN**: Google Cloud CDN
- **Azure CDN**: Microsoft CDN
- **Fastly**: Real-time CDN

---

## 📊 **MONITORING & ALERTING**

### **Key Metrics to Monitor**
- **Cache Hit Ratio**: Primary performance indicator
- **Latency**: P50, P95, P99 percentiles
- **Throughput**: Operations per second
- **Memory Usage**: Capacity and utilization
- **Error Rate**: Cache failures and timeouts

### **Alerting Thresholds**
- **Cache Hit Ratio < 70%**: Performance degradation
- **Latency > 50ms**: Slow response times
- **Memory Usage > 90%**: Capacity issues
- **Error Rate > 5%**: Cache failures

---

## 🎯 **50 CACHING INTERVIEW QUESTIONS**

### **Basic Concepts**
1. **What is caching and why use it?**
2. **Explain cache hit vs cache miss**
3. **What is cache hit ratio and why is it important?**
4. **Describe different cache layers**
5. **What is cache invalidation?**

### **Cache Strategies**
6. **Explain cache-aside pattern**
7. **What is write-through caching?**
8. **Describe write-behind caching**
9. **What is cache warming?**
10. **Explain stale-while-revalidate pattern**

### **Cache Implementation**
11. **How would you implement an LRU cache?**
12. **What is consistent hashing?**
13. **How do you handle cache eviction?**
14. **Explain cache partitioning**
15. **What is cache replication?**

### **Performance Optimization**
16. **How do you optimize cache performance?**
17. **What is cache compression?**
18. **Explain cache prefetching**
19. **How do you handle cache stampede?**
20. **What is cache pollution?**

### **Distributed Caching**
21. **How do you scale a cache horizontally?**
22. **What is cache consistency?**
23. **Explain cache coherency protocols**
24. **How do you handle cache failures?**
25. **What is cache partitioning?**

### **Real-World Scenarios**
26. **Design a caching strategy for a web application**
27. **How would you cache a social media feed?**
28. **Design caching for an e-commerce platform**
29. **How do you cache API responses?**
30. **Design caching for a real-time system**

### **Advanced Concepts**
31. **What is cache-oblivious algorithms?**
32. **Explain cache-friendly data structures**
33. **How do you optimize for CPU cache?**
34. **What is cache line optimization?**
35. **Explain memory hierarchy optimization**

### **Monitoring & Observability**
36. **What metrics do you monitor for caching?**
37. **How do you debug cache issues?**
38. **What is cache profiling?**
39. **How do you measure cache effectiveness?**
40. **What alerts do you set up for caching?**

### **System Design Questions**
41. **Design a distributed cache system**
42. **How would you design a CDN?**
43. **Design a caching layer for a database**
44. **How do you cache in a microservices architecture?**
45. **Design caching for a mobile application**

### **Troubleshooting**
46. **How do you handle cache failures?**
47. **What do you do when cache hit ratio is low?**
48. **How do you handle cache inconsistency?**
49. **What happens when cache memory is full?**
50. **How do you optimize cache for high concurrency?**

---

## ❓ **FREQUENTLY ASKED QUESTIONS (FAQs)**

### **Common Misconceptions & Quick Answers**

#### **Q1: "Caching always improves performance"**
**A: FALSE** - Caching can hurt performance if:
- Cache hit ratio is low (<50%)
- Cache overhead exceeds benefits
- Cache invalidation is too frequent
- Memory pressure causes thrashing

#### **Q2: "More cache is always better"**
**A: FALSE** - More cache can be worse if:
- Memory pressure affects other components
- Cache warming time is too long
- Cache complexity increases latency
- Cost exceeds performance benefits

#### **Q3: "Cache consistency doesn't matter for performance"**
**A: FALSE** - Cache consistency affects:
- User experience (stale data)
- System reliability (incorrect data)
- Debugging complexity
- Business logic correctness

#### **Q4: "Cache hit ratio is the only metric that matters"**
**A: FALSE** - Other important metrics:
- Latency (P95, P99)
- Throughput (ops/sec)
- Memory usage
- Error rates
- Cost per operation

#### **Q5: "All caching strategies are the same"**
**A: FALSE** - Different strategies for different needs:
- Cache-aside: Simple, flexible
- Write-through: Strong consistency
- Write-behind: High performance
- Refresh-ahead: No cache misses

---

*Use this cheatsheet for quick reference during interviews. Remember: choose caching strategy based on requirements, not just familiarity.*
