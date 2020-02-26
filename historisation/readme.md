# Historisation Library


### How to use

`python main.py path/to/config/file.json`

### Config file

#### `historifier`

- `domain_id`: (required) id of the domain
- `dataset_id`: (required) id of the dataset
- `apikey`: (optional) apikey if dataset is private
- `time_format`: (optional) python time format to prefix file names with

#### `action`

- `type`: (required) `fetch_records` or `fetch_aggregations`
- `fetch_records`
- `fetch_aggregations`
    - `params`
        - `select`
        - `where`
        - `group_by`
        - `map_on` : when the `group_by` cardinality is greater than
        20000, use map_on to split the group_by operation on a given
        field. (ie: `group_by`:`cities`, `map_on`:`regions`)

#### `storage`

- `type`: (required) `local` or `ftp` (for now)
- `local`
    - `params`
        - `root_dir`: directory where files will be saved
- `ftp`
    - `params`
        - `root_dir`: directory where files will be saved
        - `host`: ftp hostname
        - `username`: ftp username
        - `password`: ftp password

```json
{
  "historifier": {
    "domain_id": "data",
    "dataset_id": "disponibilite-parking-aximumcolas@issy-les-moulineaux",
    "apikey": "",
    "time_format": "%Y-%m-%d"
  },
  "action": {
    "type": "fetch_aggregations",
    "params": {
      "select": "count(*) as count",
      "group_by": "implantation"
    }
  },
  "storage": {
    "type": "local",
    "params": {
      "root_dir": "test"
    }
  }
}

```

__________________________________
## Contribute

To add more storage options, new classes implementing the [storage interface](historisation/storage.py) need to be added in [the `storages` package](historisation/storages).

