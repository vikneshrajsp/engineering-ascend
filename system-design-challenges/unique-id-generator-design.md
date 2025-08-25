# Design a Unique ID Generator - System Design Challenge

*Comprehensive solution for designing a distributed unique ID generator, covering various ID generation strategies, collision handling, and global scale.*

## 🎯 **Challenge Overview**

Design a distributed unique ID generator that can generate millions of unique identifiers per second across multiple data centers without collisions.

### **Key Requirements**
- **Scale**: 10M+ IDs/second across multiple regions
- **Uniqueness**: Zero collision probability
- **Ordering**: Monotonically increasing IDs
- **Performance**: <1ms latency for ID generation
- **Availability**: 99.99% uptime

## 🏗️ **RESHADED Framework Solution**

### **Step 1: Requirements & Constraints**

#### **Functional Requirements**
- **ID Generation**: Generate unique, sortable IDs
- **Bulk Generation**: Generate multiple IDs in one request
- **Custom Prefixes**: Support for application-specific prefixes
- **ID Validation**: Validate ID format and uniqueness
- **Metadata**: Include timestamp, node info, sequence number

#### **Non-Functional Requirements**
- **Scalability**: Handle millions of requests per second
- **Availability**: High availability across data centers
- **Performance**: Low latency ID generation
- **Uniqueness**: Guaranteed uniqueness across all nodes
- **Ordering**: Monotonically increasing IDs

#### **Constraints**
- **Clock Synchronization**: Handle clock skew between nodes
- **Network Latency**: Minimize coordination overhead
- **Storage**: Efficient storage of ID metadata
- **Cost**: Minimize infrastructure costs

### **Step 2: Estimation & Scale**

#### **Capacity Planning**
```
Daily ID Generation: 10M/second × 86400 seconds = 864B IDs/day
Monthly ID Generation: 864B × 30 = 25.9T IDs/month
Yearly ID Generation: 25.9T × 12 = 311T IDs/year

ID Size: 64 bits = 8 bytes
Daily Storage: 864B × 8 bytes = 6.9TB/day
Monthly Storage: 6.9TB × 30 = 207TB/month

Peak Load: 3x normal = 30M IDs/second
```

#### **Peak Load Estimation**
```
Peak Factor: 3x normal load
Peak Generation: 30M/second
Peak Storage: 20.7TB/day

Distribution: 70% sequential, 30% random access
Regions: 5 data centers globally
```

### **Step 3: System Interface Design**

#### **API Design**
```python
# Core Operations
generate_id() -> unique_id
generate_bulk(count) -> [unique_id]
generate_with_prefix(prefix) -> prefixed_id

# Validation
validate_id(id) -> boolean
extract_metadata(id) -> metadata

# Advanced Operations
generate_sequential(start_id, count) -> [sequential_ids]
generate_custom_format(format) -> formatted_id
```

#### **ID Format**
```python
# 64-bit ID Structure
class IDStructure:
    def __init__(self):
        self.timestamp_bits = 41    # 41 bits for timestamp
        self.node_id_bits = 10      # 10 bits for node ID
        self.sequence_bits = 12     # 12 bits for sequence number
        self.sign_bit = 1           # 1 bit for sign (always 0)
    
    def generate_id(self, timestamp, node_id, sequence):
        id_value = 0
        id_value |= (timestamp << 22)  # Shift timestamp to bits 22-62
        id_value |= (node_id << 12)    # Shift node_id to bits 12-21
        id_value |= sequence           # Sequence in bits 0-11
        return id_value
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
│              ID Generation Service                      │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Node 1    │  │   Node 2    │  │   Node N    │     │
│  │ (DC: US-E)  │  │ (DC: US-W)  │  │ (DC: EU)    │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│              Clock Synchronization                      │
├─────────────────────────────────────────────────────────┤
│              Coordination Layer                         │
├─────────────────────────────────────────────────────────┤
│              Storage Layer (Metadata)                   │
└─────────────────────────────────────────────────────────┘
```

### **Step 5: Application Layer Design**

#### **Snowflake ID Generator**
```python
class SnowflakeGenerator:
    def __init__(self, node_id, epoch=1609459200000):  # 2021-01-01 epoch
        self.node_id = node_id
        self.epoch = epoch
        self.sequence = 0
        self.last_timestamp = -1
        self.node_id_bits = 10
        self.sequence_bits = 12
        self.max_sequence = (1 << self.sequence_bits) - 1
    
    def generate_id(self):
        current_timestamp = self._get_current_timestamp()
        
        if current_timestamp < self.last_timestamp:
            raise Exception("Clock moved backwards")
        
        if current_timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & self.max_sequence
            if self.sequence == 0:
                current_timestamp = self._wait_for_next_millisecond()
        else:
            self.sequence = 0
        
        self.last_timestamp = current_timestamp
        
        return self._combine_bits(current_timestamp, self.node_id, self.sequence)
    
    def _get_current_timestamp(self):
        return int(time.time() * 1000) - self.epoch
    
    def _wait_for_next_millisecond(self):
        timestamp = self._get_current_timestamp()
        while timestamp <= self.last_timestamp:
            timestamp = self._get_current_timestamp()
        return timestamp
    
    def _combine_bits(self, timestamp, node_id, sequence):
        return (timestamp << (self.node_id_bits + self.sequence_bits)) | \
               (node_id << self.sequence_bits) | \
               sequence
```

#### **UUID v4 Generator**
```python
class UUIDGenerator:
    def __init__(self):
        self.random_generator = random.Random()
    
    def generate_uuid(self):
        # Generate 16 random bytes
        random_bytes = [self.random_generator.randint(0, 255) for _ in range(16)]
        
        # Set version (4) and variant bits
        random_bytes[6] = (random_bytes[6] & 0x0f) | 0x40  # Version 4
        random_bytes[8] = (random_bytes[8] & 0x3f) | 0x80  # Variant 1
        
        # Convert to UUID string
        return self._bytes_to_uuid(random_bytes)
    
    def _bytes_to_uuid(self, bytes_array):
        hex_string = ''.join([f'{b:02x}' for b in bytes_array])
        return f"{hex_string[:8]}-{hex_string[8:12]}-{hex_string[12:16]}-{hex_string[16:20]}-{hex_string[20:32]}"
```

#### **ULID Generator**
```python
class ULIDGenerator:
    def __init__(self):
        self.random_generator = random.Random()
    
    def generate_ulid(self):
        # Generate timestamp (48 bits)
        timestamp = int(time.time() * 1000)
        timestamp_bytes = timestamp.to_bytes(6, byteorder='big')
        
        # Generate randomness (80 bits)
        random_bytes = [self.random_generator.randint(0, 255) for _ in range(10)]
        
        # Combine and encode as base32
        combined_bytes = timestamp_bytes + bytes(random_bytes)
        return self._encode_base32(combined_bytes)
    
    def _encode_base32(self, data):
        # Base32 encoding (Crockford's base32)
        alphabet = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
        result = ''
        
        for i in range(0, len(data), 5):
            chunk = data[i:i+5]
            value = int.from_bytes(chunk, byteorder='big')
            
            for j in range(8):
                if i * 8 + j < len(data) * 8:
                    result += alphabet[(value >> (35 - j * 5)) & 0x1f]
        
        return result
```

### **Step 6: Data Layer Design**

#### **ID Metadata Storage**
```python
class IDMetadataStore:
    def __init__(self):
        self.metadata_db = {}  # In-memory for performance
    
    def store_metadata(self, id_value, metadata):
        self.metadata_db[id_value] = {
            'timestamp': metadata['timestamp'],
            'node_id': metadata['node_id'],
            'sequence': metadata['sequence'],
            'created_at': time.time()
        }
    
    def get_metadata(self, id_value):
        return self.metadata_db.get(id_value)
    
    def validate_uniqueness(self, id_value):
        return id_value not in self.metadata_db
```

#### **Clock Synchronization**
```python
class ClockSynchronizer:
    def __init__(self):
        self.ntp_servers = ['pool.ntp.org', 'time.google.com']
        self.clock_offset = 0
    
    def sync_clock(self):
        # Get time from multiple NTP servers
        times = []
        for server in self.ntp_servers:
            try:
                ntp_time = self._get_ntp_time(server)
                times.append(ntp_time)
            except Exception:
                continue
        
        if times:
            # Calculate median time to avoid outliers
            median_time = sorted(times)[len(times) // 2]
            local_time = time.time()
            self.clock_offset = median_time - local_time
    
    def get_synchronized_time(self):
        return time.time() + self.clock_offset
```

### **Step 7: Error Handling & Edge Cases**

#### **Clock Drift Handling**
```python
class ClockDriftHandler:
    def __init__(self):
        self.max_clock_drift = 10  # 10ms max drift
        self.last_sync_time = 0
        self.sync_interval = 300  # Sync every 5 minutes
    
    def handle_clock_drift(self, current_timestamp, last_timestamp):
        # Check if clock moved backwards
        if current_timestamp < last_timestamp:
            drift = last_timestamp - current_timestamp
            
            if drift > self.max_clock_drift:
                # Clock moved backwards significantly
                raise Exception(f"Clock moved backwards by {drift}ms")
            else:
                # Small drift, wait for next millisecond
                return self._wait_for_next_millisecond(last_timestamp)
        
        return current_timestamp
    
    def _wait_for_next_millisecond(self, last_timestamp):
        while True:
            current_time = time.time() * 1000
            if current_time > last_timestamp:
                return int(current_time)
            time.sleep(0.001)  # Wait 1ms
```

#### **Node Failure Handling**
```python
class NodeFailureHandler:
    def __init__(self):
        self.node_status = {}
        self.failover_nodes = {}
    
    def handle_node_failure(self, failed_node_id):
        # Mark node as failed
        self.node_status[failed_node_id] = 'failed'
        
        # Redirect traffic to backup node
        backup_node = self.failover_nodes.get(failed_node_id)
        if backup_node:
            return backup_node
        
        # Generate new node ID for replacement
        return self._generate_new_node_id()
    
    def _generate_new_node_id(self):
        # Generate unique node ID from available pool
        available_ids = set(range(1024)) - set(self.node_status.keys())
        if available_ids:
            return min(available_ids)
        else:
            raise Exception("No available node IDs")
```

### **Step 8: Deployment & Monitoring**

#### **Deployment Architecture**
```yaml
# Kubernetes Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: id-generator
spec:
  replicas: 5
  selector:
    matchLabels:
      app: id-generator
  template:
    metadata:
      labels:
        app: id-generator
    spec:
      containers:
      - name: id-generator
        image: id-generator:latest
        ports:
        - containerPort: 8080
        env:
        - name: NODE_ID
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: EPOCH_TIMESTAMP
          value: "1609459200000"
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
```

#### **Monitoring & Observability**
```python
class IDGeneratorMonitoring:
    def __init__(self):
        self.metrics = {
            'ids_generated_per_second': Counter(),
            'generation_latency': Histogram(),
            'collision_rate': Counter(),
            'clock_drift': Gauge(),
            'node_health': Gauge()
        }
    
    def record_id_generation(self, latency, success):
        self.metrics['ids_generated_per_second'].inc()
        self.metrics['generation_latency'].observe(latency)
        
        if not success:
            self.metrics['collision_rate'].inc()
    
    def record_clock_drift(self, drift_ms):
        self.metrics['clock_drift'].set(drift_ms)
        
        if abs(drift_ms) > 10:
            self._send_alert(f"High clock drift detected: {drift_ms}ms")
    
    def check_node_health(self, node_id):
        # Health check logic
        is_healthy = self._perform_health_check(node_id)
        self.metrics['node_health'].set(1 if is_healthy else 0)
        return is_healthy
```

## 📊 **Summary**

### **Building Blocks Used**
1. **Data Storage**: Metadata storage for ID tracking
2. **Compute & Processing**: ID generation algorithms and validation
3. **Networking & Communication**: Clock synchronization, node coordination
4. **Scalability & Distribution**: Multi-node deployment, load balancing
5. **Monitoring & Observability**: Metrics collection, health checks

### **Key Trade-offs**
- **Uniqueness vs Performance**: Stronger uniqueness guarantees require more coordination
- **Ordering vs Distribution**: Monotonic ordering requires clock synchronization
- **ID Size vs Storage**: Larger IDs provide more uniqueness but use more storage
- **Centralized vs Distributed**: Centralized generation is simpler but creates single point of failure

### **Scalability Considerations**
- **Horizontal Scaling**: Add nodes to increase generation capacity
- **Geographic Distribution**: Place nodes closer to users for lower latency
- **Clock Synchronization**: Use NTP servers for accurate time
- **Load Balancing**: Distribute requests across multiple nodes

This design provides a robust, scalable unique ID generator that can handle millions of requests per second while maintaining guaranteed uniqueness and ordering across distributed systems.
