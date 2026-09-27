---
title: "Snowflake Storage for Apache Iceberg: Open Tables Without Managing a Bucket"
date: 2026-04-18T07:11:00+01:00
draft: false
tags: ["snowflake", "iceberg", "lakehouse", "aws", "azure", "open-source"]
lastmod: 2026-09-26T09:00:00+01:00
description: "Snowflake can now store and manage Apache Iceberg table files for you on AWS and Azure - what it is, how it differs from external volumes, and when to use it."
cover:
  image: /assets/images/data-engineering/snowflake.jpg
  alt: Snowflake Icon
---

## Two Ways to Store an Iceberg Table in Snowflake

*Updated September 2026: this post originally described the feature at preview and got the storage model backwards. It has been rewritten against the GA documentation.*

Snowflake has supported Apache Iceberg tables since 2024, but until April 2026 every one of them needed an **external volume**: your own S3 bucket, Azure container or GCS bucket, plus the IAM roles and trust policies to let Snowflake read and write it. **Snowflake Storage for Apache Iceberg tables** removes that step. [Snowflake stores and manages the Iceberg table files for you](https://docs.snowflake.com/en/user-guide/tables-iceberg-storage), in Snowflake-provided storage, while the table stays in open Iceberg format.

It entered [preview on 14 April 2026](https://docs.snowflake.com/en/release-notes/2026/other/2026-04-14-iceberg-snowflake-storage) and became [generally available on 1 June 2026](https://docs.snowflake.com/en/release-notes/2026/other/2026-06-01-iceberg-snowflake-storage-ga), on AWS and Azure. For a deeper look at Iceberg itself, see [Apache Iceberg in 2026](/data-engineering/apache-iceberg-2026/), and for where this sits in the broader platform picture see [The modern lakehouse stack](/data-engineering/modern-lakehouse-stack/).

| | Snowflake storage | External volume |
|---|---|---|
| **Where the files live** | Snowflake-provided storage | Your S3 / Azure / GCS bucket |
| **Setup** | None beyond `CREATE ICEBERG TABLE` | External volume, IAM role, trust policy |
| **Fail-safe** | Yes, for permanent tables | No (protect it yourself, e.g. bucket versioning) |
| **External Iceberg catalogs** | No - Snowflake is the catalog | Required for externally managed tables |
| **Access from other engines** | Through Snowflake Horizon Catalog | Through Horizon, or directly via your catalog |

## Creating One

```sql
CREATE ICEBERG TABLE my_iceberg_table (col1 INT)
  CATALOG = 'SNOWFLAKE'
  EXTERNAL_VOLUME = 'SNOWFLAKE_MANAGED';
```

That's it: no bucket, no IAM role, no base location. Compare that with the external-volume version, which needs a `CREATE EXTERNAL VOLUME` pointing at your bucket and a role Snowflake can assume before the first table exists.

## Why This Matters

### 1. Iceberg Without the Storage Plumbing

The hardest part of Iceberg on Snowflake was never the table format. It was the cross-account IAM setup, the bucket policies, and the question of who owns them. For teams that want an open format but don't want to run the storage, that work is now gone.

### 2. Open Format Is Not the Same as Your Bucket

This is the trade-off to understand. With Snowflake storage the table is still Iceberg, and [other engines can read and write it through Horizon Catalog](https://docs.snowflake.com/en/user-guide/tables-iceberg-internal-storage). But the files aren't in an account you control. If your reason for choosing Iceberg is "we can walk away with the files", an external volume still gives you the stronger version of that guarantee.

### 3. Snowflake-Grade Protection

Permanent tables on Snowflake storage get Fail-safe, a seven-day recovery window on top of Time Travel, and can be replicated across regions and clouds with failover groups. External-volume tables don't get Fail-safe; the protection is whatever you configure on the bucket.

## When to Use Which

- **Choose Snowflake storage** when Snowflake is your primary engine, other engines are occasional readers or writers, and you'd rather not operate buckets and IAM.
- **Choose an external volume** when the data must live in your own account for residency, audit or exit reasons, when you use an external Iceberg catalog, or when another engine is the primary writer.

## Governance

Iceberg tables in Snowflake use the same governance as native tables: role-based access control, masking policies, row access policies, tags, and access history. External engines that come in through Horizon Catalog are governed by the same policies, which is the main reason to route them that way rather than reading files directly.

## What Else Arrived at Summit 2026

The GA landed alongside [Apache Iceberg v3 support and Horizon Catalog capabilities built on Apache Polaris](https://www.snowflake.com/en/news/press-releases/snowflake-pioneers-new-open-framework-for-interoperable-enterprise-data-and-ai/). Together they position Snowflake as a full Iceberg platform rather than a warehouse that can also read Iceberg.

## Resources

- [Storage for Apache Iceberg tables (Snowflake docs)](https://docs.snowflake.com/en/user-guide/tables-iceberg-storage)
- [Snowflake storage for Apache Iceberg tables (Snowflake docs)](https://docs.snowflake.com/en/user-guide/tables-iceberg-internal-storage)
- [GA release note, 1 June 2026](https://docs.snowflake.com/en/release-notes/2026/other/2026-06-01-iceberg-snowflake-storage-ga)
- [Snowflake announcement blog](https://www.snowflake.com/en/blog/storage-iceberg-tables/)
- [Apache Iceberg Official Documentation](https://iceberg.apache.org/)

## Related Reading

- [Following the Money: Databricks vs Snowflake vs the Open-Source Alternative](/data-engineering/following-the-money/)
- [Apache Iceberg in 2026: The Open Table Format That Won](/data-engineering/apache-iceberg-2026/)
- [ETL Tools & Data Integration Platforms](/data-engineering/etl-tools/)
- [Databricks vs Snowflake in 2026: An Honest Comparison](/data-engineering/databricks-vs-snowflake-2026/)
