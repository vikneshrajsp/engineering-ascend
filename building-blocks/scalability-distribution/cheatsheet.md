---
title: Cheatsheet
layout: default
grand_parent: Building Blocks
parent: Scalability Distribution
---

# Scalability & Distribution Systems - Cheat Sheet
## One-Page Quick Reference for Interviews

## 🎯 **QUICK DECISION FRAMEWORK**

### **When to Use Scaling Types**
```
Scaling Requirements? → Choose Scaling
├─ High Traffic? → Horizontal Scaling
├─ Resource Intensive? → Vertical Scaling
├─ Global Users? → Geographic Distribution
├─ Variable Load? → Auto-scaling
└─ Fault Tolerance? → Redundancy + Replication
```

### **Distribution Strategy Selection**
```
Distribution Needs?
├─ Simple Scaling? → Load Balancing
├─ Service Isolation? → Microservices
├─ Event Processing? → Event-Driven Architecture
├─ Data Consistency? → Consensus Algorithms
└─ Complex Transactions? → Saga Pattern
```

### **Consensus Algorithm Selection**
```
Consensus Requirements?
├─ Simple Agreement? → Basic Consensus
├─ Fault Tolerance? → Paxos/Raft
├─ Byzantine Faults? → Byzantine Fault Tolerance
├─ Performance Critical? → Fast Consensus
└─ Consistency Critical? → Strong Consistency
```

---

## 📈 **SCALING QUICK REFERENCE**

### **Horizontal vs Vertical Scaling**
<div class="table-wrapper">

<th>Aspect</th>
<th>Horizontal Scaling</th>
<th>Vertical Scaling</th>

**Approach**
Add more machines
Add more resources

**Complexity**
High
Low

**Cost**
Linear
Exponential

**Fault Tolerance**
High
Low

**Performance**
Distributed
Centralized

Strategy
Purpose
Implementation
Benefits

-------

### **Stateless Scaling**

| Scale services independently | External state management | Linear scaling |
|---|---|---|
| **Data Partitioning** | Distribute data across nodes | Hash/range partitioning | Data locality |

### **Service Decomposition**

| Break monoliths into services | Microservices architecture | Independent scaling |
|---|---|---|
| **Load Distribution** | Spread load across resources | Load balancers, CDNs | Better performance |

Method
Use Case
Advantages
Disadvantages

-------

### **Hash-based**

| Even distribution | Balanced load | Range queries difficult |
|---|---|---|
| **Range-based** | Ordered data | Range queries efficient | Uneven distribution |

### **Directory-based**

| Flexible mapping | Easy rebalancing | Centralized directory |
|---|---|---|
| **Composite** | Complex requirements | Multiple strategies | Increased complexity |

Algorithm
Use Case
Performance
Fairness

### **Round Robin**

| Simple distribution | O(1) | Equal |
|---|---|---|
| **Least Connections** | Dynamic load | O(n) | Load-based |

### **Weighted Round Robin**

| Different capacities | O(1) | Capacity-based |
|---|---|---|
| **IP Hash** | Session affinity | O(1) | Client-based |

Type
Layer
Use Case
Features

------
-------
----

### **Application (ALB)**

| Layer 7 | Web applications | Content-based routing |
|---|---|---|
| **Network (NLB)** | Layer 4 | High performance | TCP/UDP support |

### **Global (GLB)**

| DNS | Geographic distribution | Multi-region |
|---|---|---|
| Type | Purpose | Frequency | Timeout |
Action

------
-----

**Liveness**
Is service alive?
30-60s
5-10s
Restart

**Readiness**
Ready for traffic?
5-10s
1-5s
Remove from LB

**Startup**
Started successfully?
5-10s
1-5s
Restart

Strategy
Response Time
Accuracy
Use Case

-------

### **Reactive**

| 1-5 minutes | High | Predictable patterns |
|---|---|---|
| **Predictive** | Pre-emptive | Variable | ML-based prediction |

### **Scheduled**

| Scheduled | High | Known patterns |
|---|---|---|
| Metric | Threshold (Scale Up) | Threshold (Scale Down) | Window |

---
### **CPU Usage**

| 70-80% | 30-40% | 5-15 minutes |
|---|---|---|
| **Memory Usage** | 80-90% | 50-60% | 5-15 minutes |

### **Request Rate**

| Based on capacity | Based on capacity | 1-5 minutes |
|---|---|---|
| **Response Time** | Based on SLA | Based on SLA | 5-15 minutes |

Benefit
Description
Implementation

--------

**Cost Optimization**
Pay only for needed resources
Dynamic provisioning

**Performance**
Maintain performance under load
Automatic scaling

**Availability**
Handle traffic spikes
Proactive scaling

**Operational Efficiency**
Reduce manual intervention
Automated scaling

Pattern
Purpose
Benefits
Challenges

--------

### **Domain-driven**

| Business alignment | Clear ownership | Domain boundaries |
|---|---|---|
| **Bounded Context** | Domain isolation | Simplified models | Context mapping |

### **API Gateway**

| Client simplification | Single entry point | Gateway bottleneck |
|---|---|---|
| Type | Protocol | Use Case | Performance |

------
---------

### **Synchronous**

| HTTP/REST | Simple requests | Medium |
|---|---|---|
| **High Performance** | gRPC | Internal services | High |

### **Flexible**

| GraphQL | Complex queries | Variable |
|---|---|---|
| **Asynchronous** | Message Queues | Decoupled services | High |

Pattern
Implementation
Benefits
Challenges

---------

### **Client-side**

| Client finds services | Direct communication | Client complexity |
|---|---|---|
| **Server-side** | Load balancer finds services | Simple clients | Load balancer dependency |

### **Service Registry**

| Centralized directory | Service management | Registry availability |
|---|---|---|
| Algorithm | Complexity | Performance | Use Case |

--
### **Paxos**

| High | Medium | Distributed databases |
|---|---|---|
| **Raft** | Medium | Medium | General consensus |

**Byzantine**
Very High
Low
Security-critical systems

Property
Definition
Importance

----------

**Safety**
No two nodes decide different values
Consistency

**Liveness**
Eventually a value is decided
Progress

**Fault Tolerance**
Works despite node failures
Reliability

Application
Consensus Use
Benefits
Trade-offs

### **Distributed Databases**

| Write consensus | Strong consistency | Performance |
|---|---|---|
| **Service Coordination** | Leader election | Consistent coordination | Overhead |

### **Configuration Management**

| Config consensus | Consistent config | Complexity |
|---|---|---|
| Pattern | Purpose | Implementation | Benefits |

------

### **Shared State**

| Multiple nodes access | Centralized storage | Consistency |
|---|---|---|
| **Partitioned State** | Large state distribution | Hash/range partitioning | Scalability |

### **Replicated State**

| High availability | Multiple copies | Availability |
|---|---|---|
| Model | Guarantees | Performance | Use Case |

-------
-----------

### **Strong Consistency**

| Immediate consistency | Low | Critical data |
|---|---|---|
| **Eventual Consistency** | Eventually consistent | High | User data |

### **Causal Consistency**

| Causally consistent | Medium | Social applications |
|---|---|---|
| Strategy | Purpose | Implementation | Benefits |

-------

### **Hash Partitioning**

| Even distribution | Consistent hashing | Balanced load |
|---|---|---|
| **Range Partitioning** | Ordered access | Key ranges | Range queries |

### **Replication**

| High availability | Multiple copies | Fault tolerance |
|---|---|---|
| Scaling Type | Performance Gain | Cost | Complexity |

------

### **Horizontal**

| Linear scaling | Linear | High |
|---|---|---|
| **Vertical** | Limited by hardware | Exponential | Low |

### **Auto-scaling**

| Dynamic scaling | Variable | Medium |
|---|---|---|
| **Load Balancing** | Better distribution | Low | Medium |

Component
Performance Impact
Optimization
Monitoring

### **Network Communication**

| Latency overhead | Service locality | Network monitoring |
|---|---|---|
| **Consensus Algorithms** | Coordination overhead | Efficient algorithms | Consensus monitoring |

### **State Management**

| Consistency overhead | Appropriate models | State monitoring |
|---|---|---|
| **Service Discovery** | Lookup overhead | Caching | Discovery monitoring |

Vulnerability
Impact
Prevention
Detection

--------

### **Premature Optimization**

| Wasted effort | Measure first | Performance monitoring |
|---|---|---|
| **Over-engineering** | Complexity | Start simple | Architecture reviews |

### **Single Point of Failure**

| System downtime | Redundancy | Failure testing |
|---|---|---|
| **Poor Load Distribution** | Uneven load | Proper load balancing | Load monitoring |

Vulnerability
Impact
Prevention
Detection

--------

### **Network Partitions**

| Inconsistency | Partition tolerance | Network monitoring |
|---|---|---|
| **Consensus Failures** | No progress | Proper consensus | Consensus monitoring |

### **State Inconsistency**

| Data corruption | Consistency models | Data validation |
|---|---|---|
| **Service Dependencies** | Cascading failures | Circuit breakers | Dependency monitoring |

Use Case
Primary Scaling
Secondary Scaling
Key Decision Factors

-------
### **Web Application**

| Horizontal scaling | Load balancing | Traffic distribution + performance |
|---|---|---|
| **API Service** | Auto-scaling | Load balancing | Variable load + response time |

### **Database System**

| Vertical scaling | Horizontal scaling | Data consistency + performance |
|---|---|---|
| **Microservices** | Service scaling | Load balancing | Independent scaling + communication |

### **Real-time System**

| Horizontal scaling | Load balancing | Low latency + high throughput |
|---|---|---|
| **Batch Processing** | Horizontal scaling | Auto-scaling | Resource utilization + cost |

System Type
Load Balancing
Consensus
State Management

--
### **Monolithic**

| Simple load balancing | Basic consensus | Centralized state |
|---|---|---|
| **Microservices** | Service mesh | Service coordination | Distributed state |

### **Event-driven**

| Message routing | Event ordering | Event sourcing |
|---|---|---|
| **Real-time** | Low-latency LB | Fast consensus | In-memory state |

### **Batch Processing**

| Job distribution | Job coordination | Shared state |
|---|---|---|
| Metric | Target | Monitoring | Optimization |

----

### **Throughput**

| 1000+ requests/sec | Request rate monitoring | Load balancing |
|---|---|---|
| **Latency** | <100ms response time | Response time monitoring | Caching, optimization |

### **Availability**

| 99.9%+ uptime | Uptime monitoring | Redundancy, health checks |
|---|---|---|
| **Scalability** | Linear scaling | Scaling metrics | Proper architecture |

Metric
Target
Monitoring
Optimization

----

### **Network Latency**

| <10ms inter-service | Network monitoring | Service locality |
|---|---|---|
| **Consensus Time** | <100ms agreement | Consensus monitoring | Efficient algorithms |

### **State Consistency**

| <1s consistency | State monitoring | Appropriate models |
|---|---|---|
| **Service Discovery** | <1s lookup time | Discovery monitoring | Caching, optimization |

</div>
---

## 🎯 **50 SCALING INTERVIEW QUESTIONS**

### **Scaling Fundamentals**
1. **How would you design a scalable system?**
2. ### **What's the difference between horizontal and vertical scaling?**

| 3. **When would you choose horizontal vs vertical scaling?** | 4. **How do you measure system scalability?** | 5. **What are the limits of scaling?** |
|---|---|---|
| ### **Load Balancing Questions** | 6. **How do you design a load balancer?** | 7. **What load balancing algorithms do you know?** | 8. **How do you handle session affinity?** |
9. **How do you implement health checks?**
10. **How do you handle load balancer failures?**

### **Auto-scaling Questions**
11. **How do you design an auto-scaling system?**
12. ### **What metrics do you use for auto-scaling?**

| 13. **How do you prevent scaling thrashing?** | 14. **How do you handle scaling during failures?** | 15. **How do you optimize auto-scaling costs?** |
|---|---|---|
| ### **Microservices Questions** | 16. **How do you decompose a monolith into microservices?** | 17. **How do services communicate in a microservices architecture?** | 18. **How do you handle service discovery?** |
19. **How do you manage distributed transactions?**
20. **How do you handle service failures?**

### **Consensus Questions**
21. **How do you implement distributed consensus?**
22. ### **What's the difference between Paxos and Raft?**

| 23. **How do you handle Byzantine failures?** | 24. **How do you optimize consensus performance?** | 25. **How do you handle consensus failures?** |
|---|---|---|
| ### **State Management Questions** | 26. **How do you manage state in distributed systems?** | 27. **What consistency models do you know?** | 28. **How do you handle state partitioning?** |
29. **How do you handle state replication?**
30. **How do you handle state conflicts?**

### **Performance Questions**
31. **How do you optimize system performance?**
32. ### **How do you identify performance bottlenecks?**

| 33. **How do you handle high traffic?** | 34. **How do you optimize network communication?** | 35. **How do you handle resource contention?** |
|---|---|---|
| ### **Fault Tolerance Questions** | 36. **How do you design for fault tolerance?** | 37. **How do you handle node failures?** | 38. **How do you implement circuit breakers?** |
39. **How do you handle cascading failures?**
40. **How do you implement retry logic?**

### **Monitoring Questions**
41. **How do you monitor distributed systems?**
42. ### **How do you track system performance?**

| 43. **How do you handle monitoring at scale?** | 44. **How do you implement alerting?** | 45. **How do you handle monitoring failures?** |
|---|---|---|
| ### **Advanced Questions** | 46. **How do you handle global distribution?** | 47. **How do you implement edge computing?** | 48. **How do you handle multi-cloud scaling?** |
49. **How do you implement serverless scaling?**
50. **How do you handle quantum-resistant scaling?**

---

## ❓ **FREQUENTLY ASKED QUESTIONS (FAQs)**

### **Common Misconceptions & Quick Answers**

#### **Q1: "Scaling is just adding more servers"**
**A: FALSE** - Scaling requires proper architecture and design:
- **Load Distribution**: Need proper load balancing
- **State Management**: Need distributed state management
- **Consistency**: Need consensus for consistency
- **Monitoring**: Need comprehensive monitoring

#### **Q2: "Horizontal scaling is always better than vertical"**
**A: FALSE** - Each has its place:
- **Vertical Scaling**: Better for simple systems, lower complexity
- **Horizontal Scaling**: Better for complex systems, higher fault tolerance
- **Hybrid Approach**: Often the best solution
- **Cost Considerations**: Vertical scaling can be more cost-effective initially

#### **Q3: "Auto-scaling solves all scaling problems"**
**A: FALSE** - Auto-scaling has limitations:
- **Configuration**: Requires careful configuration
- **Predictability**: May not handle unpredictable load
- **Cost**: Can lead to unexpected costs
- **Complexity**: Adds operational complexity

#### **Q4: "Consensus is only for databases"**
**A: FALSE** - Consensus has many applications:
- **Service Coordination**: Leader election, configuration management
- **Distributed Systems**: State replication, fault tolerance
- **Blockchain**: Distributed ledger consensus
- **IoT Systems**: Device coordination

#### **Q5: "State management is simple in distributed systems"**
**A: FALSE** - Distributed state is complex:
- **Consistency**: Trade-offs between consistency and performance
- **Partitioning**: Complex data partitioning strategies
- **Replication**: Multiple replication strategies
- **Conflicts**: Complex conflict resolution

---

*Use this cheatsheet for quick reference during interviews. Remember: scaling and distribution are essential for modern systems.*
