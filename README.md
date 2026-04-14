# logaggregation

Personal lab — experimenting with log aggregation stacks using Docker Compose.
Two separate setups: one with the Elastic stack (EFK), one with OpenSearch + Fluent Bit.

A Python script generates dummy log lines into a local file, which the log shipper
tails and forwards to the backend.

> **Note:** This is an early personal sandbox — rough configs used while
> learning the stacks. The actual working lab (with proper structure and
> Kubernetes manifests) lives in a private company environment and cannot
> be shared publicly.

---

## Repository structure

```
try_log/          — Elasticsearch + Kibana + Filebeat (EFK stack)
try_opensearch/   — OpenSearch + OpenSearch Dashboards + Fluent Bit
```

---

## try_log — EFK stack

**Stack:** Elasticsearch 9.1.2 · Kibana 9.1.2 · Filebeat 9.1.2

Filebeat tails `alog1/f1.log`, parses structured log lines using `dissect`,
and ships them to Elasticsearch. Kibana is available at `http://localhost:5601`.

### Run

```bash
cd try_log

# Create the log directory and start the generator
mkdir -p alog1
python pyLog.py &

# Start the stack
docker compose up -d
```

### Log format

`pyLog.py` writes lines in this format:

```
2025-06-27 14:44:50.625 - INFO - Application started successfully
```

Filebeat parses `timestamp`, `level`, and `message` fields via `dissect`.

---

## try_opensearch — OpenSearch + Fluent Bit

**Stack:** OpenSearch 3.1.0 · OpenSearch Dashboards 3.1.0 · Fluent Bit 4.0.3

Fluent Bit tails `alog1/f1.log` and ships to OpenSearch over TLS (self-signed,
verify disabled). Dashboards available at `http://localhost:5601`.

### Run

```bash
cd try_opensearch

# Create the log directory and start the generator
mkdir -p alog1
python pyLog.py &

# Start the stack
docker compose up -d
```

### Credentials

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `MyS3cur3P123123123ppPP` |

> Change the password in both `docker-compose.yaml` and `fluent-bit.conf`
> before any non-local use.

### Version snapshots

The `_30` suffix files (`docker-compose.yaml_30`, `fluent-bit.conf_30`) are
snapshots from when Fluent Bit 3.0.0 was used. The current files target 4.0.3,
which adds `storage.backlog.flush_on_shutdown` and `threaded` input options.

---

## Requirements

- Docker + Docker Compose
- Python 3 (for `pyLog.py`)
