[dashboard_guide.md](https://github.com/user-attachments/files/24219051/dashboard_guide.md)
# QuickSight Dashboard Guide

1. Sign up for QuickSight (Standard, Free Tier).
2. Datasets:
   - DynamoDB: `slice_state` (add as dataset).
   - S3: `slice-telemetry-demo/telemetry/` (create a manifest JSON in QuickSight pointing to the folder).
3. Fields:
   - Extract latency/jitter from S3 telemetry JSON or use calculated fields.
   - From DynamoDB, parse `last_alloc` as a string; if needed, pre-flatten via a small ETL.
4. Visuals:
   - KPI: % intervals meeting SLA (e.g., latency < 25 ms).
   - Line chart: latency/jitter over time per slice_id.
   - Bar chart: allocated bandwidth vs traffic (utilization).
   - Table: last allocation per slice.
5. Publish the dashboard and share.
