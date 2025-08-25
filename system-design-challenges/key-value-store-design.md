---
title: Key Value Store Design - System Design Challenge
description: Comprehensive solution for key value store design system design challenge
layout: default
parent: Key Value Store Design
grand_parent: System Design Challenges
---

# Design a Distributed Key-Value Store - System Design Challenge

*Comprehensive solution for designing a distributed key-value store, covering consistency models, partitioning, replication, and global scale.*

## 🎯 **Challenge Overview**

Design a distributed key-value store that can handle millions of operations per second with high availability and consistency guarantees.

### **Key Requirements**
- **Scale**: 100M+ keys, 1M+ operations/second
- **Availability**: 99.99% uptime
- **Consistency**: Configurable consistency levels
- **Latency**: <10ms for reads, <50ms for writes
- **Durability**: Data persistence across failures

## 🏗️ **RESHADED Framework Solution**

### **Step 1: Requirements & Constraints**

#### **Functional Requirements**
- **CRUD Operations**: Create, Read, Update, Delete key-value pairs
- **TTL Support**: Automatic expiration of keys
- **Batch Operations**: Multi-key operations
- **Scan Operations**: Range queries and pattern matching
- **Atomic Operations**: Compare-and-swap, increment/decrement

#### **Non-Functional Requirements**
- **Scalability**: Horizontal scaling across multiple nodes
- **Availability**: Fault tolerance and automatic failover
- **Consistency**: Configurable consistency (Eventual, Strong, Causal)
- **Performance**: Low latency and high throughput
- **Durability**: Data persistence and recovery

#### **Constraints**
- **Network Partitioning**: Handle network failures gracefully
- **Clock Skew**: Distributed timestamp ordering
- **Storage Limits**: Efficient memory and disk usage
- **Cost**: Minimize infrastructure costs

### **Step 2: Estimation & Scale**

#### **Capacity Planning**
```
Total Keys: 100M
Average Key Size: 100 bytes
Average Value Size: 1KB
Total Data: 100M × 1.1KB = 110GB

Read Operations: 800K/second (80%)
Write Operations: 200K/second (20%)
Total Operations: 1M/second

Storage Growth: 10% per month
5-Year Storage: 110GB × (1.1)^60 = ~2.5TB
```

#### **Peak Load Estimation**
```
Peak Factor: 3x normal load
Peak Operations: 3M/second
Peak Storage: 330GB

Read Distribution: 90% hot data, 10% cold data
Write Distribution: 70% updates, 30% new keys
```

### **Step 3: System Interface Design**

#### **API Design**
```python
# Core Operations
GET(key) -> value
PUT(key, value, ttl=None) -> success
DELETE(key) -> success
EXISTS(key) -> boolean

# Batch Operations
MGET(keys[]) -> values[]
MSET(key_value_pairs[]) -> success
MDELETE(keys[]) -> success

# Advanced Operations
INCR(key, amount=1) -> new_value
CAS(key, expected_value, new_value) -> success
SCAN(pattern, limit=100) -> keys[]
TTL(key) -> remaining_seconds
```

#### **Data Models**
```json
{
  "key": "user:123:profile",
  "value": {
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2024-01-01T00:00:00Z"
  },
  "metadata": {
    "ttl": 86400,
    "version": 5,
    "last_modified": "2024-01-01T12:00:00Z"
  }
}
```

### **Step 4: High-Level Architecture**

```
┌─────────────────────────────────────────────────────────┐
│                Client Applications                      │
├─────────────────────────────────────────────────────────┤
│                    Load Balancer                        │
├─────────────────────────────────────────────────────────┤
│              API Gateway / Proxy Layer                  │
├─────────────────────────────────────────────────────────┤
│              Partitioning Layer (Consistent Hashing)    │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Node 1    │  │   Node 2    │  │   Node N    │     │
│  │ (Primary)   │  │ (Primary)   │  │ (Primary)   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │ Replica 1   │  │ Replica 2   │  │ Replica N   │     │
│  │ (Secondary) │  │ (Secondary) │  │ (Secondary) │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│              Storage Layer (LSM Tree)                  │
├─────────────────────────────────────────────────────────┤
│              Distributed Coordination                   │
└─────────────────────────────────────────────────────────┘
```

### **Step 5: Application Layer Design**

#### **Partitioning Strategy**
```python
class ConsistentHashing:
    def __init__(self, nodes, virtual_nodes=150):
        self.ring = {}
        self.nodes = nodes
        self.virtual_nodes = virtual_nodes
        self._build_ring()
    
    def _build_ring(self):
        for node in self.nodes:
            for i in range(self.virtual_nodes):
                virtual_key = f"{node}:{i}"
                hash_value = self._hash(virtual_key)
                self.ring[hash_value] = node
    
    def get_node(self, key):
        hash_value = self._hash(key)
        sorted_hashes = sorted(self.ring.keys())
        
        for hash_val in sorted_hashes:
            if hash_val >= hash_value:
                return self.ring[hash_val]
        
        return self.ring[sorted_hashes[0]]  # Wrap around
```

#### **Replication Strategy**
```python
class ReplicationManager:
    def __init__(self, replication_factor=3):
        self.replication_factor = replication_factor
    
    def get_replicas(self, primary_node, all_nodes):
        replicas = []
        node_list = list(all_nodes)
        primary_index = node_list.index(primary_node)
        
        for i in range(1, self.replication_factor):
            replica_index = (primary_index + i) % len(node_list)
            replicas.append(node_list[replica_index])
        
        return replicas
    
    def quorum_size(self):
        return (self.replication_factor // 2) + 1
```

#### **Consistency Management**
```python
class ConsistencyManager:
    def __init__(self, consistency_level):
        self.consistency_level = consistency_level
    
    def read_quorum(self, replicas):
        if self.consistency_level == "STRONG":
            return len(replicas)  # Read from all replicas
        elif self.consistency_level == "EVENTUAL":
            return 1  # Read from any replica
        else:  # Causal
            return (len(replicas) // 2) + 1
    
    def write_quorum(self, replicas):
        if self.consistency_level == "STRONG":
            return len(replicas)  # Write to all replicas
        else:
            return (len(replicas) // 2) + 1  # Majority
```

### **Step 6: Data Layer Design**

#### **Storage Engine (LSM Tree)**
```python
class LSMTree:
    def __init__(self):
        self.memtable = {}  # In-memory table
        self.sstables = []  # Sorted string tables
        self.memtable_size_limit = 64 * 1024 * 1024  # 64MB
    
    def put(self, key, value):
        self.memtable[key] = value
        
        if len(self.memtable) >= self.memtable_size_limit:
            self._flush_memtable()
    
    def get(self, key):
        # Check memtable first
        if key in self.memtable:
            return self.memtable[key]
        
        # Check SSTables (newest first)
        for sstable in reversed(self.sstables):
            value = sstable.get(key)
            if value is not None:
                return value
        
        return None
    
    def _flush_memtable(self):
        # Create new SSTable from memtable
        sstable = SSTable(self.memtable)
        self.sstables.append(sstable)
        self.memtable = {}
        
        # Trigger compaction if needed
        self._compact_sstables()
```

#### **Data Access Patterns**
```python
class DataAccessPatterns:
    def __init__(self):
        self.cache = {}  # LRU cache for hot data
        self.bloom_filter = BloomFilter()  # For SSTable lookups
    
    def read_pattern(self, key):
        # 1. Check cache first
        if key in self.cache:
            return self.cache[key]
        
        # 2. Check bloom filter
        if not self.bloom_filter.might_contain(key):
            return None  # Key definitely doesn't exist
        
        # 3. Check memtable
        value = self.memtable.get(key)
        if value:
            self.cache[key] = value
            return value
        
        # 4. Check SSTables
        for sstable in self.sstables:
            value = sstable.get(key)
            if value:
                self.cache[key] = value
                return value
        
        return None
    
    def write_pattern(self, key, value):
        # 1. Update cache
        self.cache[key] = value
        
        # 2. Update bloom filter
        self.bloom_filter.add(key)
        
        # 3. Write to memtable
        self.memtable[key] = value
        
        # 4. Replicate to other nodes
        self._replicate_write(key, value)
```

### **Step 7: Error Handling & Edge Cases**

#### **Failure Scenarios**
```python
class FailureHandler:
    def handle_node_failure(self, failed_node):
        # 1. Detect failure via health checks
        if not self._is_node_healthy(failed_node):
            # 2. Redirect traffic to replicas
            self._redirect_traffic(failed_node)
            
            # 3. Trigger rebalancing
            self._rebalance_partitions()
            
            # 4. Replicate missing data
            self._replicate_missing_data(failed_node)
    
    def handle_network_partition(self):
        # 1. Detect partition via consensus
        if not self._can_reach_quorum():
            # 2. Continue serving with available nodes
            self._serve_with_available_nodes()
            
            # 3. Queue writes for later sync
            self._queue_pending_writes()
            
            # 4. Resolve conflicts when partition heals
            self._resolve_conflicts()
    
    def handle_data_corruption(self, corrupted_key):
        # 1. Detect corruption via checksums
        if not self._verify_checksum(corrupted_key):
            # 2. Restore from replica
            self._restore_from_replica(corrupted_key)
            
            # 3. Validate data integrity
            self._validate_data_integrity()
```

#### **Conflict Resolution**
```python
class ConflictResolver:
    def resolve_write_conflicts(self, key, values):
        # Last-write-wins strategy
        latest_value = max(values, key=lambda v: v.timestamp)
        return latest_value
    
    def resolve_cas_conflicts(self, key, expected_value, new_value):
        # Optimistic concurrency control
        current_value = self.get(key)
        if current_value == expected_value:
            self.put(key, new_value)
            return True
        else:
            return False  # Conflict detected
```

### **Step 8: Deployment & Monitoring**

#### **Deployment Architecture**
```yaml
# Kubernetes Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: key-value-store
spec:
  replicas: 10
  selector:
    matchLabels:
      app: key-value-store
  template:
    metadata:
      labels:
        app: key-value-store
    spec:
      containers:
      - name: kv-store
        image: kv-store:latest
        ports:
        - containerPort: 6379
        resources:
          requests:
            memory: "2Gi"
            cpu: "500m"
          limits:
            memory: "4Gi"
            cpu: "1000m"
        env:
        - name: REPLICATION_FACTOR
          value: "3"
        - name: CONSISTENCY_LEVEL
          value: "EVENTUAL"
```

#### **Monitoring & Observability**
```python
class MonitoringSystem:
    def __init__(self):
        self.metrics = {
            'operations_per_second': Counter(),
            'latency_p99': Histogram(),
            'error_rate': Counter(),
            'memory_usage': Gauge(),
            'disk_usage': Gauge()
        }
    
    def record_operation(self, operation_type, latency, success):
        self.metrics['operations_per_second'].inc()
        self.metrics['latency_p99'].observe(latency)
        
        if not success:
            self.metrics['error_rate'].inc()
    
    def alert_on_thresholds(self):
        if self.metrics['error_rate'].get() > 0.01:  # 1% error rate
            self._send_alert("High error rate detected")
        
        if self.metrics['latency_p99'].get() > 100:  # 100ms P99
            self._send_alert("High latency detected")
```

## 📊 **Summary**

### **Building Blocks Used**
1. **Data Storage**: LSM Tree for efficient writes, SSTables for persistence
2. **Caching & Performance**: In-memory cache, bloom filters, read replicas
3. **Networking & Communication**: Consistent hashing, replication protocols
4. **Scalability & Distribution**: Horizontal partitioning, automatic failover
5. **Monitoring & Observability**: Metrics collection, alerting, health checks

### **Key Trade-offs**
- **Consistency vs Availability**: Strong consistency reduces availability during partitions
- **Write Performance vs Read Performance**: LSM trees optimize writes but require compaction
- **Memory vs Disk**: More memory improves performance but increases cost
- **Replication Factor vs Storage**: Higher replication improves availability but increases storage

### **Scalability Considerations**
- **Horizontal Scaling**: Add nodes to increase capacity
- **Vertical Scaling**: Increase node resources for better performance
- **Geographic Distribution**: Place nodes closer to users for lower latency
- **Auto-scaling**: Automatically adjust capacity based on load

This design provides a robust, scalable key-value store that can handle millions of operations per second while maintaining high availability and configurable consistency levels.
