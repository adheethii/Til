## 📌 What is an API and How It Works

### What is an API?

**API (Application Programming Interface)** is a messenger that allows two software applications to communicate with each other.

> An API lets one application request data or services from another application and receive a response.

---

### 🍽️ Real-Life Example: Ordering Food

Imagine you're in a restaurant:

- **You** → Customer
- **Waiter** → API
- **Kitchen** → Server/Application

#### How it works:
1. You tell the waiter what you want.
2. The waiter takes your request to the kitchen.
3. The kitchen prepares the food.
4. The waiter brings the food back to you.

The waiter acts as the **API**, carrying requests and responses.

---

### 💻 How APIs Work in Software

Suppose a weather app wants today's weather.

#### Step 1: Client Sends a Request

```http
GET /weather?city=London
```

The request is sent to the weather server through the API.

#### Step 2: Server Processes the Request

The server:
- Receives the request.
- Finds London's weather data.
- Prepares a response.

#### Step 3: Server Sends a Response

```json
{
  "city": "London",
  "temperature": 22,
  "condition": "Cloudy"
}
```

---

### 🔄 API Request Flow

```text
Client/App
    ↓ Request
API
    ↓
Server/Database
    ↑
API
    ↑ Response
Client/App
```

---

### 📱 Example: Instagram Login with Google

When you click **"Continue with Google"**:

1. Instagram sends a request to Google's API.
2. Google verifies your identity.
3. Google sends back confirmation.
4. Instagram logs you in.

Without APIs, apps could not share services like login, payments, maps, or weather data.

---

### ⭐ Why Are APIs Important?

APIs help developers:

- ✅ Reuse existing services
- ✅ Connect different applications
- ✅ Save development time
- ✅ Access external data
- ✅ Build scalable systems

Examples:
- Payment APIs (Stripe, Razorpay)
- Maps APIs (Google Maps)
- Weather APIs
- AI APIs (OpenAI)

---

### 📚 Key Terms to Remember

| Term | Meaning |
|--------|----------|
| Client | The application making the request |
| Server | The application providing data or services |
| Request | What the client asks for |
| Response | What the server sends back |
| Endpoint | A specific API URL |
| JSON | Common format used to exchange data |

---

### 📝 One-Line Summary

> **An API is a bridge that enables different software applications to communicate by sending requests and receiving responses.**
