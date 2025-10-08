# DNS over HTTPS with JSON Format

DNS over HTTPS (DoH) is a protocol for performing DNS resolution via HTTPS, increasing privacy and security by preventing eavesdropping and manipulation of DNS data.

### JSON Format (Google & Cloudflare):
- Both Google and Cloudflare offer DoH endpoints that accept DNS queries and return results in JSON format.
- Instead of the traditional binary DNS message, you send an HTTP GET or POST request with query parameters (e.g., domain name, record type).
- The response is a JSON object containing DNS records, status, and other metadata.

**Example:**
- **Google:**  
  Endpoint: `https://dns.google/resolve?name=example.com&type=A`
- **Cloudflare:**  
  Endpoint: `https://cloudflare-dns.com/dns-query?name=example.com&type=A`

**Response Example:**
```json
{
  "Status": 0,
  "Question": [{ "name": "example.com", "type": 1 }],
  "Answer": [{ "name": "example.com", "type": 1, "TTL": 299, "data": "93.184.216.34" }]
}
```

