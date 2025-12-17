# DynamoDB table: slice_state

- Partition key: `slice_id` (String)
- Attributes:
  - `last_alloc` (String, JSON {bandwidth,cpu,memory})
  - `ts` (Number, optional timestamp)

Create via Console:
DynamoDB → Create table → Name `slice_state` → Partition key `slice_id` (String) → Billing mode: On-demand.
