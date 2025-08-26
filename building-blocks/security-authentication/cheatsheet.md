---
title: Cheatsheet
layout: default
grand_parent: Building Blocks
parent: Security Authentication
---

# Security & Authentication Systems - Cheat Sheet
## One-Page Quick Reference for Interviews

## 🎯 **QUICK DECISION FRAMEWORK**

### **When to Use Authentication Types**
```
Security Requirements? → Choose Authentication
├─ High Security? → Multi-Factor Authentication
├─ User Convenience? → Biometric Authentication
├─ Third-Party Access? → OAuth 2.0
├─ Enterprise Integration? → SAML
└─ Stateless Systems? → JWT
```

### **Authorization Model Selection**
```
Access Control Needs?
├─ Simple Roles? → RBAC
├─ Complex Policies? → ABAC
├─ Dynamic Rules? → PBAC
├─ Fine-Grained Control? → ACLs
└─ Hybrid Requirements? → Combined Models
```

### **Security Level Selection**
```
Security Level Required?
├─ Basic Security? → Password + HTTPS
├─ Enhanced Security? → MFA + Encryption
├─ High Security? → Zero Trust + Advanced Monitoring
├─ Compliance Required? → Audit Logging + Compliance Tools
└─ Critical Systems? → Defense in Depth + Redundancy
```

---

## 🔐 **AUTHENTICATION QUICK REFERENCE**

### **Authentication Methods**
<div class="table-wrapper">
<table>
<thead>
<tr>
<th>Method</th>
<th>Security</th>
<th>User Experience</th>
<th>Implementation</th>
<th>Use Case</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Password**</td>
<td>Low</td>
<td>Good</td>
<td>Simple</td>
<td>Basic systems</td>
</tr>
<tr>
<td>**MFA (TOTP)**</td>
<td>High</td>
<td>Good</td>
<td>Medium</td>
<td>High security</td>
</tr>
<tr>
<td>**Biometric**</td>
<td>High</td>
<td>Excellent</td>
<td>Complex</td>
<td>Mobile devices</td>
</tr>
<tr>
<td>**OAuth 2.0**</td>
<td>High</td>
<td>Good</td>
<td>Complex</td>
<td>Third-party access</td>
</tr>
<tr>
<td>**SAML**</td>
<td>High</td>
<td>Good</td>
<td>Complex</td>
<td>Enterprise SSO</td>
</tr>
<tr>
<td>**JWT**</td>
<td>Medium</td>
<td>Good</td>
<td>Simple</td>
<td>Stateless systems</td>
</tr>
<tr>
<td>Method</td>
<td>Security Level</td>
<td>Attack Resistance</td>
<td>Storage Overhead</td>
</tr>
<tr>
<td>--------</td>
<td>---------------</td>
<td>------------------</td>
<td>------------------</td>
</tr>
<tr>
<td>**Plain Text**</td>
<td>0%</td>
<td>None</td>
<td>Minimal</td>
</tr>
<tr>
<td>**Simple Hash**</td>
<td>20%</td>
<td>Rainbow tables</td>
<td>Minimal</td>
</tr>
<tr>
<td>**Salted Hash**</td>
<td>60%</td>
<td>Dictionary attacks</td>
<td>Low</td>
</tr>
<tr>
<td>**Adaptive Hash**</td>
<td>80%</td>
<td>Brute force</td>
<td>Medium</td>
</tr>
<tr>
<td>**Password Manager**</td>
<td>95%</td>
<td>Most attacks</td>
<td>None</td>
</tr>
<tr>
<td>Factor</td>
<td>Examples</td>
<td>Security Gain</td>
<td>User Experience</td>
</tr>
<tr>
<td>--------</td>
<td>----------</td>
<td>---------------</td>
<td>-----------------</td>
</tr>
<tr>
<td>**Knowledge**</td>
<td>Password, PIN</td>
<td>50%</td>
<td>Familiar</td>
</tr>
<tr>
<td>**Possession**</td>
<td>TOTP, SMS</td>
<td>90%</td>
<td>Good</td>
</tr>
<tr>
<td>**Inherence**</td>
<td>Fingerprint, Face</td>
<td>95%</td>
<td>Excellent</td>
</tr>
<tr>
<td>**Location**</td>
<td>GPS, IP</td>
<td>70%</td>
<td>Transparent</td>
</tr>
<tr>
<td>**Time**</td>
<td>Time-based tokens</td>
<td>80%</td>
<td>Good</td>
</tr>
<tr>
<td>Model</td>
<td>Complexity</td>
<td>Flexibility</td>
<td>Performance</td>
<td>Best For</td>
</tr>
<tr>
<td>-------</td>
<td>------------</td>
<td>-------------</td>
<td>-------------</td>
<td>----------</td>
</tr>
<tr>
<td>**ACL**</td>
<td>Low</td>
<td>Low</td>
<td>High</td>
<td>Simple systems</td>
</tr>
<tr>
<td>**RBAC**</td>
<td>Medium</td>
<td>Medium</td>
<td>High</td>
<td>Organizations</td>
</tr>
<tr>
<td>**ABAC**</td>
<td>High</td>
<td>High</td>
<td>Medium</td>
<td>Dynamic environments</td>
</tr>
<tr>
<td>**PBAC**</td>
<td>Very High</td>
<td>Very High</td>
<td>Low</td>
<td>Complex compliance</td>
</tr>
<tr>
<td>Algorithm</td>
<td>Type</td>
<td>Key Size</td>
<td>Security</td>
<td>Performance</td>
</tr>
<tr>
<td>-----------</td>
<td>------</td>
<td>----------</td>
<td>----------</td>
<td>-------------</td>
</tr>
<tr>
<td>**AES-256**</td>
<td>Symmetric</td>
<td>256 bits</td>
<td>High</td>
<td>High</td>
</tr>
<tr>
<td>**RSA-2048**</td>
<td>Asymmetric</td>
<td>2048 bits</td>
<td>Medium</td>
<td>Low</td>
</tr>
<tr>
<td>**ECC-256**</td>
<td>Asymmetric</td>
<td>256 bits</td>
<td>High</td>
<td>Medium</td>
</tr>
<tr>
<td>**ChaCha20**</td>
<td>Symmetric</td>
<td>256 bits</td>
<td>High</td>
<td>Very High</td>
</tr>
<tr>
<td>Algorithm</td>
<td>Output Size</td>
<td>Security</td>
<td>Performance</td>
<td>Status</td>
</tr>
<tr>
<td>-----------</td>
<td>-------------</td>
<td>----------</td>
<td>-------------</td>
<td>--------</td>
</tr>
<tr>
<td>**SHA-256**</td>
<td>256 bits</td>
<td>High</td>
<td>Very High</td>
<td>Recommended</td>
</tr>
<tr>
<td>**SHA-384**</td>
<td>384 bits</td>
<td>Very High</td>
<td>High</td>
<td>Recommended</td>
</tr>
<tr>
<td>**SHA-512**</td>
<td>512 bits</td>
<td>Very High</td>
<td>High</td>
<td>Recommended</td>
</tr>
<tr>
<td>**MD5**</td>
<td>128 bits</td>
<td>Broken</td>
<td>Very High</td>
<td>Deprecated</td>
</tr>
<tr>
<td>Cipher Suite</td>
<td>Key Exchange</td>
<td>Encryption</td>
<td>Hash</td>
<td>Security</td>
</tr>
<tr>
<td>--------------</td>
<td>--------------</td>
<td>------------</td>
<td>------</td>
<td>----------</td>
</tr>
<tr>
<td>**TLS_AES_256_GCM_SHA384**</td>
<td>ECDHE</td>
<td>AES-256-GCM</td>
<td>SHA-384</td>
<td>High</td>
</tr>
<tr>
<td>**TLS_CHACHA20_POLY1305_SHA256**</td>
<td>ECDHE</td>
<td>ChaCha20-Poly1305</td>
<td>SHA-256</td>
<td>High</td>
</tr>
<tr>
<td>**TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384**</td>
<td>ECDHE</td>
<td>AES-256-GCM</td>
<td>SHA-384</td>
<td>High</td>
</tr>
<tr>
<td>Version</td>
<td>Security</td>
<td>Performance</td>
<td>Compatibility</td>
<td>Recommendation</td>
</tr>
<tr>
<td>---------</td>
<td>----------</td>
<td>-------------</td>
<td>---------------</td>
<td>----------------</td>
</tr>
<tr>
<td>**TLS 1.0**</td>
<td>Low</td>
<td>High</td>
<td>Legacy</td>
<td>Disable</td>
</tr>
<tr>
<td>**TLS 1.1**</td>
<td>Low</td>
<td>High</td>
<td>Legacy</td>
<td>Disable</td>
</tr>
<tr>
<td>**TLS 1.2**</td>
<td>Medium</td>
<td>High</td>
<td>Widely supported</td>
<td>Accept</td>
</tr>
<tr>
<td>**TLS 1.3**</td>
<td>High</td>
<td>Very High</td>
<td>Modern browsers</td>
<td>Prefer</td>
</tr>
<tr>
<td>VPN Type</td>
<td>Security</td>
<td>Performance</td>
<td>Use Case</td>
<td>Implementation</td>
</tr>
<tr>
<td>----------</td>
<td>----------</td>
<td>-------------</td>
<td>----------</td>
<td>----------------</td>
</tr>
<tr>
<td>**IPSec**</td>
<td>High</td>
<td>Medium</td>
<td>Site-to-site</td>
<td>Hardware</td>
</tr>
<tr>
<td>**OpenVPN**</td>
<td>High</td>
<td>Medium</td>
<td>Remote access</td>
<td>Software</td>
</tr>
<tr>
<td>**WireGuard**</td>
<td>High</td>
<td>High</td>
<td>Modern VPN</td>
<td>Kernel</td>
</tr>
<tr>
<td>**SSL VPN**</td>
<td>Medium</td>
<td>High</td>
<td>Web-based</td>
<td>Browser</td>
</tr>
<tr>
<td>Security Feature</td>
<td>Performance Impact</td>
<td>Security Gain</td>
<td>ROI</td>
</tr>
<tr>
<td>------------------</td>
<td>-------------------</td>
<td>---------------</td>
<td>-----</td>
</tr>
<tr>
<td>**MFA**</td>
<td>2-5x auth time</td>
<td>99%+ improvement</td>
<td>High</td>
</tr>
<tr>
<td>**Strong Encryption**</td>
<td>5-15% CPU</td>
<td>1000x+ resistance</td>
<td>High</td>
</tr>
<tr>
<td>**Audit Logging**</td>
<td>1-5% I/O</td>
<td>100% compliance</td>
<td>Medium</td>
</tr>
<tr>
<td>**Rate Limiting**</td>
<td>1-2% latency</td>
<td>90%+ prevention</td>
<td>High</td>
</tr>
<tr>
<td>Aspect</td>
<td>Challenge</td>
<td>Solution</td>
<td>Performance</td>
</tr>
<tr>
<td>--------</td>
<td>-----------</td>
<td>----------</td>
<td>-------------</td>
</tr>
<tr>
<td>**Authentication**</td>
<td>High volume</td>
<td>Distributed auth</td>
<td>10K+ users/sec</td>
</tr>
<tr>
<td>**Authorization**</td>
<td>Complex policies</td>
<td>Cached decisions</td>
<td>100K+ decisions/sec</td>
</tr>
<tr>
<td>**Encryption**</td>
<td>Key management</td>
<td>Centralized KMS</td>
<td>1GB+ encrypted/sec</td>
</tr>
<tr>
<td>**Monitoring**</td>
<td>High events</td>
<td>Distributed SIEM</td>
<td>1M+ events/sec</td>
</tr>
<tr>
<td>Vulnerability</td>
<td>Impact</td>
<td>Prevention</td>
<td>Detection</td>
</tr>
<tr>
<td>---------------</td>
<td>--------</td>
<td>------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Weak Passwords**</td>
<td>Account compromise</td>
<td>Strong policies</td>
<td>Password audits</td>
</tr>
<tr>
<td>**Password Reuse**</td>
<td>Multiple compromise</td>
<td>Password managers</td>
<td>Breach monitoring</td>
</tr>
<tr>
<td>**Brute Force**</td>
<td>Account takeover</td>
<td>Rate limiting, MFA</td>
<td>Failed login alerts</td>
</tr>
<tr>
<td>**Session Hijacking**</td>
<td>Unauthorized access</td>
<td>Secure sessions</td>
<td>Session monitoring</td>
</tr>
<tr>
<td>Vulnerability</td>
<td>Impact</td>
<td>Prevention</td>
<td>Detection</td>
</tr>
<tr>
<td>---------------</td>
<td>--------</td>
<td>------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Privilege Escalation**</td>
<td>Unauthorized access</td>
<td>Least privilege</td>
<td>Access reviews</td>
</tr>
<tr>
<td>**Missing Authorization**</td>
<td>Unauthorized actions</td>
<td>Always check</td>
<td>Code reviews</td>
</tr>
<tr>
<td>**Insecure Direct Object References**</td>
<td>Data access bypass</td>
<td>Indirect references</td>
<td>Penetration testing</td>
</tr>
<tr>
<td>**Horizontal Privilege Escalation**</td>
<td>Other users' data</td>
<td>Resource-level auth</td>
<td>Access monitoring</td>
</tr>
<tr>
<td>Vulnerability</td>
<td>Impact</td>
<td>Prevention</td>
<td>Detection</td>
</tr>
<tr>
<td>---------------</td>
<td>--------</td>
<td>------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Weak Algorithms**</td>
<td>Data compromise</td>
<td>Strong algorithms</td>
<td>Security scanning</td>
</tr>
<tr>
<td>**Poor Key Management**</td>
<td>Key compromise</td>
<td>Secure KMS</td>
<td>Key rotation</td>
</tr>
<tr>
<td>**Random Number Generation**</td>
<td>Predictable values</td>
<td>Secure RNG</td>
<td>Entropy testing</td>
</tr>
<tr>
<td>**Timing Attacks**</td>
<td>Key extraction</td>
<td>Constant-time ops</td>
<td>Security testing</td>
</tr>
<tr>
<td>Use Case</td>
<td>Primary Security</td>
<td>Secondary Security</td>
<td>Key Decision Factors</td>
</tr>
<tr>
<td>----------</td>
<td>-----------------</td>
<td>-------------------</td>
<td>---------------------</td>
</tr>
<tr>
<td>**Web Application**</td>
<td>HTTPS + MFA</td>
<td>Input validation</td>
<td>User experience + security</td>
</tr>
<tr>
<td>**Mobile App**</td>
<td>Biometric + JWT</td>
<td>Certificate pinning</td>
<td>Convenience + security</td>
</tr>
<tr>
<td>**API Service**</td>
<td>API keys + OAuth</td>
<td>Rate limiting</td>
<td>Performance + security</td>
</tr>
<tr>
<td>**Enterprise System**</td>
<td>SAML + RBAC</td>
<td>Audit logging</td>
<td>Compliance + security</td>
</tr>
<tr>
<td>**IoT Device**</td>
<td>Certificate-based</td>
<td>Secure boot</td>
<td>Scalability + security</td>
</tr>
<tr>
<td>**Financial System**</td>
<td>Multi-factor + encryption</td>
<td>Compliance monitoring</td>
<td>Regulatory + security</td>
</tr>
<tr>
<td>Data Sensitivity</td>
<td>Authentication</td>
<td>Authorization</td>
<td>Encryption</td>
<td>Monitoring</td>
</tr>
<tr>
<td>------------------</td>
<td>----------------</td>
<td>---------------</td>
<td>------------</td>
<td>------------</td>
</tr>
<tr>
<td>**Public Data**</td>
<td>Basic</td>
<td>None</td>
<td>None</td>
<td>Basic</td>
</tr>
<tr>
<td>**Internal Data**</td>
<td>Password</td>
<td>RBAC</td>
<td>In transit</td>
<td>Logging</td>
</tr>
<tr>
<td>**Confidential Data**</td>
<td>MFA</td>
<td>ABAC</td>
<td>At rest + transit</td>
<td>Alerting</td>
</tr>
<tr>
<td>**Highly Sensitive**</td>
<td>Multi-factor</td>
<td>PBAC</td>
<td>End-to-end</td>
<td>Real-time</td>
</tr>
<tr>
<td>**Regulated Data**</td>
<td>Compliance</td>
<td>Compliance</td>
<td>Compliance</td>
<td>Compliance</td>
</tr>
<tr>
<td>Standard</td>
<td>Focus</td>
<td>Requirements</td>
<td>Implementation</td>
</tr>
<tr>
<td>----------</td>
<td>-------</td>
<td>--------------</td>
<td>----------------</td>
</tr>
<tr>
<td>**GDPR**</td>
<td>Privacy</td>
<td>Consent, encryption, rights</td>
<td>Privacy controls</td>
</tr>
<tr>
<td>**SOX**</td>
<td>Financial</td>
<td>Audit trails, access controls</td>
<td>Financial controls</td>
</tr>
<tr>
<td>**HIPAA**</td>
<td>Healthcare</td>
<td>Privacy, security</td>
<td>Healthcare controls</td>
</tr>
<tr>
<td>**PCI DSS**</td>
<td>Payment</td>
<td>Encryption, access controls</td>
<td>Payment controls</td>
</tr>
</tbody>
</table>
</div>
### **Compliance Implementation**
- **Data Classification**: Classify data by sensitivity
- **Access Controls**: Implement appropriate controls
- **Audit Logging**: Log all access and changes
- **Monitoring**: Monitor for compliance violations
- **Incident Response**: Respond to security incidents

---

## 📊 **MONITORING & ALERTING**

### **Key Security Metrics**
- **Authentication Success Rate**: 95%+ success rate
- **Failed Login Attempts**: <5% failure rate
- **Authorization Denials**: Monitor for policy violations
- **Encryption Coverage**: 100% sensitive data encrypted
- **Security Incidents**: 0 critical incidents

### **Alerting Thresholds**
- **Failed Logins > 10/minute**: Potential brute force
- **Unauthorized Access Attempts**: Immediate alert
- **Encryption Failures**: Immediate alert
- **Compliance Violations**: Immediate alert
- **Security Incidents**: Immediate response

---

## 🎯 **50 SECURITY INTERVIEW QUESTIONS**

### **Authentication Questions**
1. **How would you design a secure authentication system?**
2. **What are the different types of MFA?**
3. **How does OAuth 2.0 work?**
4. **What are the security implications of JWT?**
5. **How do you handle password security?**

### **Authorization Questions**
6. **What's the difference between RBAC and ABAC?**
7. **How do you implement least privilege?**
8. **What are the challenges of distributed authorization?**
9. **How do you handle privilege escalation?**
10. **What's the role of policies in authorization?**

### **Cryptography Questions**
11. **What's the difference between symmetric and asymmetric encryption?**
12. **How do you choose encryption algorithms?**
13. **What are the best practices for key management?**
14. **How do you handle cryptographic vulnerabilities?**
15. **What's the role of hash functions in security?**

### **Network Security Questions**
16. **How does TLS/SSL work?**
17. **What are the security implications of different TLS versions?**
18. **How do you secure API communications?**
19. **What's the role of VPNs in security?**
20. **How do you handle network segmentation?**

### **Application Security Questions**
21. **How do you prevent SQL injection?**
22. **What are the OWASP Top 10 vulnerabilities?**
23. **How do you implement secure coding practices?**
24. **What's the role of input validation?**
25. **How do you handle session security?**

### **Security Architecture Questions**
26. **How do you design a zero trust architecture?**
27. **What's the role of defense in depth?**
28. **How do you implement security by design?**
29. **What are the challenges of cloud security?**
30. **How do you handle microservices security?**

### **Compliance Questions**
31. **How do you implement GDPR compliance?**
32. **What are the requirements for PCI DSS?**
33. **How do you handle audit logging?**
34. **What's the role of data classification?**
35. **How do you implement privacy by design?**

### **Incident Response Questions**
36. **How do you handle security incidents?**
37. **What's your incident response plan?**
38. **How do you detect security threats?**
39. **What's the role of threat intelligence?**
40. **How do you handle data breaches?**

### **Security Monitoring Questions**
41. **How do you implement security monitoring?**
42. **What metrics do you track for security?**
43. **How do you handle false positives?**
44. **What's the role of SIEM systems?**
45. **How do you implement automated response?**

### **Advanced Security Questions**
46. **How do you handle quantum-resistant cryptography?**
47. **What's the role of machine learning in security?**
48. **How do you implement secure DevOps?**
49. **What are the challenges of IoT security?**
50. **How do you handle supply chain security?**

---

## ❓ **FREQUENTLY ASKED QUESTIONS (FAQs)**

### **Common Misconceptions & Quick Answers**

#### **Q1: "Security is too expensive"**
**A: FALSE** - Security is an investment that prevents costly breaches:
- **Cost of Breach**: $3.86M average cost of data breach
- **Security Investment**: 1-5% of IT budget typically sufficient
- **ROI**: Security investments typically pay for themselves

#### **Q2: "Passwords are secure enough"**
**A: FALSE** - Passwords alone are insufficient:
- **Password Attacks**: 80% of breaches involve weak passwords
- **MFA Impact**: 99%+ reduction in account compromise
- **Best Practice**: Always use multi-factor authentication

#### **Q3: "Security slows down development"**
**A: FALSE** - Security by design is faster:
- **Early Integration**: Security built-in is faster than retrofitting
- **Automated Tools**: Security scanning and testing can be automated
- **DevSecOps**: Security integrated into CI/CD pipeline

#### **Q4: "We're too small to be attacked"**
**A: FALSE** - Small organizations are common targets:
- **Attack Statistics**: 43% of cyber attacks target small businesses
- **Automated Attacks**: Most attacks are automated and target everyone
- **Supply Chain**: Small organizations are entry points to larger targets

#### **Q5: "Security is IT's responsibility"**
**A: FALSE** - Security is everyone's responsibility:
- **Human Factor**: 95% of breaches involve human error
- **Business Impact**: Security affects business operations
- **Shared Responsibility**: Security requires organizational commitment

---

*Use this cheatsheet for quick reference during interviews. Remember: security is not optional, it's essential for any system design.*
