# README

This README provides an overview of the API endpoints, their functionalities, and the data models associated with the Django application.

## Endpoints

### Vendors

#### GET `/vendors/`

- **Description:** Retrieve a list of all vendors.
- **Method:** GET
- **Response:** List of vendor objects.

#### POST `/vendors/`

- **Description:** Create a new vendor.
- **Method:** POST
- **Request Body:**
  - `name` (string): Vendor name.
  - `contact_details` (string): Vendor contact details.
  - `address` (string): Vendor address.
  - `vendor_code` (string): Unique vendor code.
  - `on_time_delivery_rate` (float): On-time delivery rate.
  - `quality_rating_avg` (float): Quality rating average.
  - `average_response_time` (float): Average response time.
  - `fulfillment_rate` (float): Fulfillment rate.
- **Response:** Created vendor object.

#### GET `/vendors/<int:vendor_id>/`

- **Description:** Retrieve details of a specific vendor.
- **Method:** GET
- **Response:** Vendor object.

#### PUT `/vendors/<int:vendor_id>/`

- **Description:** Update details of a specific vendor.
- **Method:** PUT
- **Request Body:** Same as the POST request for creating a vendor.
- **Response:** Updated vendor object.

#### DELETE `/vendors/<int:vendor_id>/`

- **Description:** Delete a specific vendor.
- **Method:** DELETE
- **Response:** No content.

### Purchase Orders

#### GET `/purchase-orders/`

- **Description:** Retrieve a list of all purchase orders.
- **Method:** GET
- **Response:** List of purchase order objects.

#### POST `/purchase-orders/`

- **Description:** Create a new purchase order.
- **Method:** POST
- **Request Body:**
  - `po_number` (string): Purchase order number.
  - `vendor` (object): Vendor details (see vendor POST request body).
  - `order_date` (datetime): Order date.
  - `delivery_date` (datetime): Delivery date.
  - `items` (JSON): JSON array of items.
  - `quantity` (integer): Order quantity.
  - `status` (string): Order status.
  - `quality_rating` (float, optional): Quality rating (can be null or blank).
  - `issue_date` (datetime): Issue date.
  - `acknowledgment_date` (datetime, optional): Acknowledgment date.
- **Response:** Created purchase order object.

#### GET `/purchase-orders/<int:po_id>/`

- **Description:** Retrieve details of a specific purchase order.
- **Method:** GET
- **Response:** Purchase order object.

#### PUT `/purchase-orders/<int:po_id>/`

- **Description:** Update details of a specific purchase order.
- **Method:** PUT
- **Request Body:** Same as the POST request for creating a purchase order.
- **Response:** Updated purchase order object.

#### DELETE `/purchase-orders/<int:po_id>/`

- **Description:** Delete a specific purchase order.
- **Method:** DELETE
- **Response:** No content.

### Vendor Performance

#### GET `/vendors/<int:vendor_id>/performance/`

- **Description:** Retrieve historical performance data for a specific vendor.
- **Method:** GET
- **Response:** List of historical performance objects.

## Data Models

### Vendor

- `name` (string): Vendor name.
- `contact_details` (string): Vendor contact details.
- `address` (string): Vendor address.
- `vendor_code` (string): Unique vendor code.
- `on_time_delivery_rate` (float): On-time delivery rate.
- `quality_rating_avg` (float): Quality rating average.
- `average_response_time` (float): Average response time.
- `fulfillment_rate` (float): Fulfillment rate.

### Purchase Order

- `po_number` (string): Purchase order number.
- `vendor` (object): Vendor details (see vendor data model).
- `order_date` (datetime): Order date.
- `delivery_date` (datetime): Delivery date.
- `items` (JSON): JSON array of items.
- `quantity` (integer): Order quantity.
- `status` (string): Order status.
- `quality_rating` (float, optional): Quality rating (can be null or blank).
- `issue_date` (datetime): Issue date.
- `acknowledgment_date` (datetime, optional): Acknowledgment date.

### Historical Performance

- `vendor` (object): Vendor details (see vendor data model).
- `date` (datetime): Performance date.
- `on_time_delivery_rate` (float): On-time delivery rate.
- `quality_rating_avg` (float): Quality rating average.
- `average_response_time` (float): Average response time.
- `fulfillment_rate` (float): Fulfillment rate.

Feel free to use this README as a reference for understanding and interacting with the API.
