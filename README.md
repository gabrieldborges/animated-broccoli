## Animated Broccoli

Welcome to **Animated Broccoli**! This project provides a set of RESTful calculator APIs built with Flask. Each calculator endpoint takes a single number input and performs distinct mathematical operations, returning a computed result in a standardized JSON format.

### Features

- **Modular Calculator Endpoints:** Three separate calculator routes, each with unique mathematical processing.
- **Error Handling:** Custom exception classes (such as `HttpBadRequest` and `HttpUnprocessableEntity`) ensure informative error responses and proper HTTP status codes.
- **Organized Codebase:** Clear separation of concerns using Flask Blueprints, factories, and error controllers.


#### POST `/calculator/1`

**Description:**  
Divides a number into three equal parts.  
- First part: divided by 4, add 7, square the result, multiply by 0.257.
- Second part: raised to power 2.121, divide by 5, add 1.
- Third part: remains unchanged.
- Final result is the sum of all parts.

**Request Example**
```json
{
  "number": 90
}
```

**Response Example**
```json
{
  "result": 99.123
}
```

#### Additional Calculator Endpoints

- `/calculator/2`
- `/calculator/3`

Each endpoint has its own logic. Check the `src/calculators/` directory for detailed implementation.

### How to Run

1. Clone the repository:
    ```
    git clone https://github.com/gabrieldborges/animated-broccoli.git
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Start the Flask app:
    ```
    flask run
    ```

### Project Structure

```
.
├── src/
│   ├── calculators/
│   ├── errors/
│   └── main/
├── .vscode/
├── requirements.txt
└── README.md
```


© 2024 animated-broccoli
