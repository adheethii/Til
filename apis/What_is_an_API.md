# What is an API and How it Works

**Date:** 2026-06-16

## What is an API?

**API = Application Programming Interface**

An API is a way for two applications to talk to each other. It defines a set of rules for how requests and responses should be made.

```
Your App → [API Request] → Another App/Service → [API Response] → Your App
```

Think of it like a waiter in a restaurant:
- You (client) tell the waiter (API) what you want
- The waiter goes to the kitchen (server)
- The kitchen prepares it and the waiter brings it back

---

## Real World Examples

| You Use | What's Happening Behind |
|---------|------------------------|
| Google Maps in Uber | Uber calls Google Maps API |
| Login with Google | App calls Google Auth API |
| Weather app | App calls a Weather API |
| Pay with Razorpay | App calls Razorpay Payment API |

---

## How it Works

```
1. CLIENT sends a REQUEST to the API endpoint
         ↓
2. API receives the request and validates it
         ↓
3. SERVER processes the request (database, logic)
         ↓
4. API sends back a RESPONSE (usually JSON)
         ↓
5. CLIENT uses the response data
```

---

## Key Terms

| Term | Meaning |
|------|---------|
| Endpoint | The URL where the API lives |
| Request | What you send to the API |
| Response | What the API sends back |
| Client | The app making the request |
| Server | The app receiving the request |

---

## Example

```
Request:
GET https://api.weather.com/current?city=Kochi

Response:
{
  "city": "Kochi",
  "temperature": 32,
  "condition": "Sunny"
}
```

---

## Types of APIs

| Type | Description |
|------|-------------|
| REST | Most common — uses HTTP methods |
| GraphQL | Client specifies exactly what data it needs |
| WebSocket | Real-time two-way communication |
| gRPC | Fast, used internally between services |

---

## Key Takeaway

> An API is a contract between two applications. One app says "send me a request in this format" and promises to "send back a response in that format." REST APIs are the most common and use HTTP to communicate.
