# Batch run log — after

- Produced by: `run_batch_eval.py::main`
- Service: `app.py::batch` (Unit 9 capstone extension)
- 3 trials · 2026-11-11 22:05

Real output per trial. Targets and verdicts come from `criteria.md`.

## Trial 1

```json
{
  "1_and_4": {
    "batch": {
      "status": 200,
      "elapsed_ms": 530.0,
      "body": {
        "batch_id": "965e7f10-576e-4f7c-879d-ed45d9f94ad1",
        "count": 10,
        "results": [
          {
            "confidence": 0.6825,
            "content_id": "9b456a3b-5f38-4b67-afed-37b10b283883",
            "duration_ms": 100.0,
            "guess": "unsure",
            "index": 0,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.8185,
            "model_score": 0.696,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.7076,
            "content_id": "8c28383e-7b90-4f2c-b8ed-514f10ffcc40",
            "duration_ms": 52.1,
            "guess": "unsure",
            "index": 1,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.869,
            "model_score": 0.7293,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.4218,
            "content_id": "ffcb7a26-2ccb-42d0-bd3f-ebe22a490e94",
            "duration_ms": 42.9,
            "guess": "unsure",
            "index": 2,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.687,
            "model_score": 0.3216,
            "style_score": 0.3991,
            "verified_human": false
          },
          {
            "confidence": 0.6131,
            "content_id": "f889d949-80b6-4b01-bc33-35076155954c",
            "duration_ms": 49.4,
            "guess": "unsure",
            "index": 3,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.8044,
            "model_score": 0.5616,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5901,
            "content_id": "f6e04aab-303d-45d2-88be-44582fb00702",
            "duration_ms": 50.4,
            "guess": "unsure",
            "index": 4,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.9005,
            "model_score": 0.6169,
            "style_score": 0.3783,
            "verified_human": false
          },
          {
            "confidence": 0.5542,
            "content_id": "0abce14c-2adc-4bc6-bc1a-1cfec252d541",
            "duration_ms": 43.4,
            "guess": "unsure",
            "index": 5,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.8316,
            "model_score": 0.416,
            "style_score": 0.5735,
            "verified_human": false
          },
          {
            "confidence": 0.5318,
            "content_id": "24048b0f-be91-4e3e-a309-7b8d30c31211",
            "duration_ms": 43.4,
            "guess": "unsure",
            "index": 6,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.7699,
            "model_score": 0.3859,
            "style_score": 0.5833,
            "verified_human": false
          },
          {
            "confidence": 0.6509,
            "content_id": "3f5f8fd6-bcdc-45ed-875f-6c19776a2f74",
            "duration_ms": 51.1,
            "guess": "unsure",
            "index": 7,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.9304,
            "model_score": 0.5895,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5819,
            "content_id": "1edaea79-cc84-402d-aab9-bd1ddbf15d99",
            "duration_ms": 43.5,
            "guess": "unsure",
            "index": 8,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.7637,
            "model_score": 0.5065,
            "style_score": 0.575,
            "verified_human": false
          },
          {
            "confidence": 0.3554,
            "content_id": "e4a6d727-71de-4f60-927b-5505b2a1fd70",
            "duration_ms": 46.0,
            "guess": "unsure",
            "index": 9,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.5798,
            "model_score": 0.3371,
            "style_score": 0.2506,
            "verified_human": false
          }
        ]
      }
    },
    "solo": [
      {
        "status": 200,
        "elapsed_ms": 57.3,
        "body": {
          "confidence": 0.6825,
          "content_id": "e05b3096-94d0-4c8b-83d2-29a40434fcb7",
          "duration_ms": 55.4,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8185,
          "model_score": 0.696,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 53.9,
        "body": {
          "confidence": 0.7076,
          "content_id": "c2d2b3e7-3fdd-4571-8bc8-ec93d95fa406",
          "duration_ms": 52.1,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.869,
          "model_score": 0.7293,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 44.1,
        "body": {
          "confidence": 0.4218,
          "content_id": "d182e841-e34b-4305-87a4-4d618da4154e",
          "duration_ms": 42.4,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.687,
          "model_score": 0.3216,
          "style_score": 0.3991,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 53.8,
        "body": {
          "confidence": 0.6131,
          "content_id": "ee498033-6bc9-4e39-a7c6-2eacf9b45b5d",
          "duration_ms": 52.1,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8044,
          "model_score": 0.5616,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 53.2,
        "body": {
          "confidence": 0.5901,
          "content_id": "147c4cdd-ead0-4c0b-a051-b858ff1e2aba",
          "duration_ms": 51.5,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.9005,
          "model_score": 0.6169,
          "style_score": 0.3783,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 45.0,
        "body": {
          "confidence": 0.5542,
          "content_id": "3e5c9409-85e0-4c70-baf9-df3b7b215136",
          "duration_ms": 43.4,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8316,
          "model_score": 0.416,
          "style_score": 0.5735,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 50.1,
        "body": {
          "confidence": 0.5318,
          "content_id": "47212ff2-bd02-4ee0-a459-d920a1e7a24d",
          "duration_ms": 48.3,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.7699,
          "model_score": 0.3859,
          "style_score": 0.5833,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 65.7,
        "body": {
          "confidence": 0.6509,
          "content_id": "33edf1d1-76ac-47ef-a3cf-00d4d667e263",
          "duration_ms": 63.9,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.9304,
          "model_score": 0.5895,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 44.9,
        "body": {
          "confidence": 0.5819,
          "content_id": "09c6f97b-929a-4f86-a923-2c36670a45d9",
          "duration_ms": 42.0,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.7637,
          "model_score": 0.5065,
          "style_score": 0.575,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 62.8,
        "body": {
          "confidence": 0.3554,
          "content_id": "7a90f930-82ba-4f65-b64c-80bb46d27f34",
          "duration_ms": 47.1,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.5798,
          "model_score": 0.3371,
          "style_score": 0.2506,
          "verified_human": false
        }
      }
    ],
    "solo_total_ms": 530.8,
    "solo_per_item_ms": 53.1,
    "batch_per_item_ms": 53.0
  },
  "2": {
    "status": 200,
    "elapsed_ms": 358.5,
    "body": {
      "batch_id": "f8bb60dd-7ffc-40b6-8975-d23dbcd62fce",
      "count": 10,
      "results": [
        {
          "confidence": 0.6825,
          "content_id": "dbceefaf-ed9e-4a2c-9473-43d29cd8caad",
          "duration_ms": 51.0,
          "guess": "unsure",
          "index": 0,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8185,
          "model_score": 0.696,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.7076,
          "content_id": "9a20e333-adb3-48b9-8253-db3085eb10f6",
          "duration_ms": 56.1,
          "guess": "unsure",
          "index": 1,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.869,
          "model_score": 0.7293,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.4218,
          "content_id": "c1038e79-855f-4163-8567-fc897663e5ab",
          "duration_ms": 47.0,
          "guess": "unsure",
          "index": 2,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.687,
          "model_score": 0.3216,
          "style_score": 0.3991,
          "verified_human": false
        },
        {
          "confidence": 0.6131,
          "content_id": "04811fea-6837-40ff-b7ba-1af896667a80",
          "duration_ms": 52.8,
          "guess": "unsure",
          "index": 3,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8044,
          "model_score": 0.5616,
          "style_score": 0.57,
          "verified_human": false
        },
        {
          "confidence": 0.5901,
          "content_id": "82544d2a-a496-420d-bc1a-1d42a9505ce7",
          "duration_ms": 53.1,
          "guess": "unsure",
          "index": 4,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.9005,
          "model_score": 0.6169,
          "style_score": 0.3783,
          "verified_human": false
        },
        {
          "confidence": 0.5542,
          "content_id": "d7695723-fa53-4a8d-8916-60cd7b8695c8",
          "duration_ms": 42.7,
          "guess": "unsure",
          "index": 5,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8316,
          "model_score": 0.416,
          "style_score": 0.5735,
          "verified_human": false
        },
        {
          "confidence": 0.5318,
          "content_id": "c4cd8eef-2d35-4273-971d-894d73797a0d",
          "duration_ms": 43.2,
          "guess": "unsure",
          "index": 6,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.7699,
          "model_score": 0.3859,
          "style_score": 0.5833,
          "verified_human": false
        },
        {
          "error": "bad_request",
          "index": 7,
          "message": "'text' is required and must be a non-empty string."
        },
        {
          "error": "bad_request",
          "index": 8,
          "message": "'text' is required and must be a non-empty string."
        },
        {
          "error": "bad_request",
          "index": 9,
          "message": "'text' is required and must be a non-empty string."
        }
      ]
    }
  },
  "3": {
    "status": 400,
    "elapsed_ms": 1.9,
    "body": {
      "error": "bad_request",
      "message": "Batch of 30 items exceeds the 20-item limit."
    }
  },
  "5": {
    "non_dict_item": {
      "status": 200,
      "elapsed_ms": 1.0,
      "body": {
        "batch_id": "d6dd0e74-05e0-4e7c-9154-0d1fbabb65a7",
        "count": 1,
        "results": [
          {
            "error": "bad_request",
            "index": 0,
            "message": "Item must be a JSON object."
          }
        ]
      }
    },
    "items_not_a_list": {
      "status": 400,
      "elapsed_ms": 1.0,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    },
    "empty_items": {
      "status": 400,
      "elapsed_ms": 1.0,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    }
  }
}
```

## Trial 2

```json
{
  "1_and_4": {
    "batch": {
      "status": 200,
      "elapsed_ms": 518.6,
      "body": {
        "batch_id": "4150a41a-2b62-4cac-9cad-7baeeeb62f81",
        "count": 10,
        "results": [
          {
            "confidence": 0.6825,
            "content_id": "5d2ab47b-7241-4852-acf2-00d30b5fba71",
            "duration_ms": 51.1,
            "guess": "unsure",
            "index": 0,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.8185,
            "model_score": 0.696,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.7076,
            "content_id": "66da2375-f753-4d94-b9d3-bca5200edc08",
            "duration_ms": 51.7,
            "guess": "unsure",
            "index": 1,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.869,
            "model_score": 0.7293,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.4218,
            "content_id": "7ffa5018-d46a-4999-8f93-30db6758099e",
            "duration_ms": 43.7,
            "guess": "unsure",
            "index": 2,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.687,
            "model_score": 0.3216,
            "style_score": 0.3991,
            "verified_human": false
          },
          {
            "confidence": 0.6131,
            "content_id": "3a334e2e-db8a-4c53-847a-1934ed66fae7",
            "duration_ms": 53.6,
            "guess": "unsure",
            "index": 3,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.8044,
            "model_score": 0.5616,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5901,
            "content_id": "e94446ab-fefe-4e69-aada-779cd7a7bacc",
            "duration_ms": 65.2,
            "guess": "unsure",
            "index": 4,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.9005,
            "model_score": 0.6169,
            "style_score": 0.3783,
            "verified_human": false
          },
          {
            "confidence": 0.5542,
            "content_id": "73f699b0-93e5-4482-824b-46050cdc372c",
            "duration_ms": 52.3,
            "guess": "unsure",
            "index": 5,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.8316,
            "model_score": 0.416,
            "style_score": 0.5735,
            "verified_human": false
          },
          {
            "confidence": 0.5318,
            "content_id": "ad8a79ca-4370-42ff-9f8c-de83aeae69e2",
            "duration_ms": 43.7,
            "guess": "unsure",
            "index": 6,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.7699,
            "model_score": 0.3859,
            "style_score": 0.5833,
            "verified_human": false
          },
          {
            "confidence": 0.6509,
            "content_id": "1427e7c4-3992-4571-b4e4-4850a35b1874",
            "duration_ms": 55.9,
            "guess": "unsure",
            "index": 7,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.9304,
            "model_score": 0.5895,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5819,
            "content_id": "64566672-398c-4adf-802f-500ceecdfdb5",
            "duration_ms": 43.2,
            "guess": "unsure",
            "index": 8,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.7637,
            "model_score": 0.5065,
            "style_score": 0.575,
            "verified_human": false
          },
          {
            "confidence": 0.3554,
            "content_id": "41a0a3e6-8c93-4b5f-a775-3160f0031fe5",
            "duration_ms": 52.9,
            "guess": "unsure",
            "index": 9,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.5798,
            "model_score": 0.3371,
            "style_score": 0.2506,
            "verified_human": false
          }
        ]
      }
    },
    "solo": [
      {
        "status": 200,
        "elapsed_ms": 61.8,
        "body": {
          "confidence": 0.6825,
          "content_id": "6411b58b-71a6-451e-9c54-d900e32e344e",
          "duration_ms": 59.8,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8185,
          "model_score": 0.696,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 63.9,
        "body": {
          "confidence": 0.7076,
          "content_id": "6da4dba9-90cc-4689-93bc-66eacee0e570",
          "duration_ms": 59.9,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.869,
          "model_score": 0.7293,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 57.8,
        "body": {
          "confidence": 0.4218,
          "content_id": "eb23532f-6222-4444-a343-12ff95880587",
          "duration_ms": 55.5,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.687,
          "model_score": 0.3216,
          "style_score": 0.3991,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 53.2,
        "body": {
          "confidence": 0.6131,
          "content_id": "f3036ec6-1679-4fea-a586-96de7e5c4a3d",
          "duration_ms": 51.5,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8044,
          "model_score": 0.5616,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 51.6,
        "body": {
          "confidence": 0.5901,
          "content_id": "78c0f18a-0af7-4954-b8b6-b88c1d57f5e8",
          "duration_ms": 49.9,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.9005,
          "model_score": 0.6169,
          "style_score": 0.3783,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 44.9,
        "body": {
          "confidence": 0.5542,
          "content_id": "1833a0ad-eeeb-4270-aa38-d0111b669938",
          "duration_ms": 43.2,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8316,
          "model_score": 0.416,
          "style_score": 0.5735,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 47.0,
        "body": {
          "confidence": 0.5318,
          "content_id": "2692d384-4234-4ff3-aa61-779557fc4449",
          "duration_ms": 42.8,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.7699,
          "model_score": 0.3859,
          "style_score": 0.5833,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 65.4,
        "body": {
          "confidence": 0.6509,
          "content_id": "165690eb-7b20-4659-b503-13dad1379661",
          "duration_ms": 63.7,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.9304,
          "model_score": 0.5895,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 45.5,
        "body": {
          "confidence": 0.5819,
          "content_id": "7f1a0dda-b80a-4df9-a4dc-134cb596b9a0",
          "duration_ms": 43.8,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.7637,
          "model_score": 0.5065,
          "style_score": 0.575,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 45.8,
        "body": {
          "confidence": 0.3554,
          "content_id": "e0e92933-ab56-42e9-b50c-746c71b94b0e",
          "duration_ms": 44.1,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.5798,
          "model_score": 0.3371,
          "style_score": 0.2506,
          "verified_human": false
        }
      }
    ],
    "solo_total_ms": 536.9,
    "solo_per_item_ms": 53.7,
    "batch_per_item_ms": 51.9
  },
  "2": {
    "status": 200,
    "elapsed_ms": 379.5,
    "body": {
      "batch_id": "5bbf9c92-dac2-4c4c-9981-c37366980ed5",
      "count": 10,
      "results": [
        {
          "confidence": 0.6825,
          "content_id": "0f2b4c0c-3b24-40b5-9280-03305156baa2",
          "duration_ms": 51.7,
          "guess": "unsure",
          "index": 0,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8185,
          "model_score": 0.696,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.7076,
          "content_id": "157f7b6f-4e9c-4a4f-837c-dab789b0025d",
          "duration_ms": 68.2,
          "guess": "unsure",
          "index": 1,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.869,
          "model_score": 0.7293,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.4218,
          "content_id": "b8d18ce2-fd20-4366-a101-125ab9529d86",
          "duration_ms": 47.2,
          "guess": "unsure",
          "index": 2,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.687,
          "model_score": 0.3216,
          "style_score": 0.3991,
          "verified_human": false
        },
        {
          "confidence": 0.6131,
          "content_id": "0b515feb-01d7-4183-b504-6a37628ec903",
          "duration_ms": 62.5,
          "guess": "unsure",
          "index": 3,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8044,
          "model_score": 0.5616,
          "style_score": 0.57,
          "verified_human": false
        },
        {
          "confidence": 0.5901,
          "content_id": "5ab24a14-d4b3-486d-ac89-1b96ef79889c",
          "duration_ms": 55.3,
          "guess": "unsure",
          "index": 4,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.9005,
          "model_score": 0.6169,
          "style_score": 0.3783,
          "verified_human": false
        },
        {
          "confidence": 0.5542,
          "content_id": "f8b94e32-854a-461a-8a29-08f1034bd3b3",
          "duration_ms": 45.9,
          "guess": "unsure",
          "index": 5,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8316,
          "model_score": 0.416,
          "style_score": 0.5735,
          "verified_human": false
        },
        {
          "confidence": 0.5318,
          "content_id": "11c150fd-f582-4afc-a426-10b62cca6ebf",
          "duration_ms": 44.7,
          "guess": "unsure",
          "index": 6,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.7699,
          "model_score": 0.3859,
          "style_score": 0.5833,
          "verified_human": false
        },
        {
          "error": "bad_request",
          "index": 7,
          "message": "'text' is required and must be a non-empty string."
        },
        {
          "error": "bad_request",
          "index": 8,
          "message": "'text' is required and must be a non-empty string."
        },
        {
          "error": "bad_request",
          "index": 9,
          "message": "'text' is required and must be a non-empty string."
        }
      ]
    }
  },
  "3": {
    "status": 400,
    "elapsed_ms": 1.5,
    "body": {
      "error": "bad_request",
      "message": "Batch of 30 items exceeds the 20-item limit."
    }
  },
  "5": {
    "non_dict_item": {
      "status": 200,
      "elapsed_ms": 1.2,
      "body": {
        "batch_id": "cf954d04-3f38-4cbf-bc30-48d1c8121e34",
        "count": 1,
        "results": [
          {
            "error": "bad_request",
            "index": 0,
            "message": "Item must be a JSON object."
          }
        ]
      }
    },
    "items_not_a_list": {
      "status": 400,
      "elapsed_ms": 1.1,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    },
    "empty_items": {
      "status": 400,
      "elapsed_ms": 1.0,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    }
  }
}
```

## Trial 3

```json
{
  "1_and_4": {
    "batch": {
      "status": 200,
      "elapsed_ms": 549.3,
      "body": {
        "batch_id": "bdf1b1d4-e8a4-4f53-ac8a-6e135b58ee97",
        "count": 10,
        "results": [
          {
            "confidence": 0.6825,
            "content_id": "3fb1014e-e588-49fe-b3f5-9ac1151411c8",
            "duration_ms": 64.5,
            "guess": "unsure",
            "index": 0,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.8185,
            "model_score": 0.696,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.7076,
            "content_id": "96fb51cb-4e53-4f4f-b99f-26c155004d31",
            "duration_ms": 65.0,
            "guess": "unsure",
            "index": 1,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.869,
            "model_score": 0.7293,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.4218,
            "content_id": "737cfa75-8c2a-482d-9438-f06e9c41e84d",
            "duration_ms": 53.2,
            "guess": "unsure",
            "index": 2,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.687,
            "model_score": 0.3216,
            "style_score": 0.3991,
            "verified_human": false
          },
          {
            "confidence": 0.6131,
            "content_id": "66dcb7c4-4dbe-4323-bcac-c22a5c8d96f1",
            "duration_ms": 72.5,
            "guess": "unsure",
            "index": 3,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.8044,
            "model_score": 0.5616,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5901,
            "content_id": "2dd24607-7759-47a4-982c-db022288b352",
            "duration_ms": 54.5,
            "guess": "unsure",
            "index": 4,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.9005,
            "model_score": 0.6169,
            "style_score": 0.3783,
            "verified_human": false
          },
          {
            "confidence": 0.5542,
            "content_id": "b093be3f-9c47-4375-be6c-7ea9a9bf5c0a",
            "duration_ms": 46.5,
            "guess": "unsure",
            "index": 5,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.8316,
            "model_score": 0.416,
            "style_score": 0.5735,
            "verified_human": false
          },
          {
            "confidence": 0.5318,
            "content_id": "a1cf2caf-dedd-48fc-8d17-06280d1f00d1",
            "duration_ms": 42.2,
            "guess": "unsure",
            "index": 6,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.7699,
            "model_score": 0.3859,
            "style_score": 0.5833,
            "verified_human": false
          },
          {
            "confidence": 0.6509,
            "content_id": "07451b7e-8bbc-4915-9895-e101f049095d",
            "duration_ms": 51.7,
            "guess": "unsure",
            "index": 7,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.9304,
            "model_score": 0.5895,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5819,
            "content_id": "c2acf17c-dfb5-4c3e-92d0-f49aa0d45496",
            "duration_ms": 44.5,
            "guess": "unsure",
            "index": 8,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.7637,
            "model_score": 0.5065,
            "style_score": 0.575,
            "verified_human": false
          },
          {
            "confidence": 0.3554,
            "content_id": "210730a1-e9ab-4ad8-bf01-58f60c3a266f",
            "duration_ms": 43.3,
            "guess": "unsure",
            "index": 9,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_score": 0.5798,
            "model_score": 0.3371,
            "style_score": 0.2506,
            "verified_human": false
          }
        ]
      }
    },
    "solo": [
      {
        "status": 200,
        "elapsed_ms": 58.2,
        "body": {
          "confidence": 0.6825,
          "content_id": "584d92bb-4aec-4128-8808-ff59cc9275d5",
          "duration_ms": 51.7,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8185,
          "model_score": 0.696,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 52.9,
        "body": {
          "confidence": 0.7076,
          "content_id": "570a74f2-aca6-4c93-a223-fea4313c606c",
          "duration_ms": 51.1,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.869,
          "model_score": 0.7293,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 43.2,
        "body": {
          "confidence": 0.4218,
          "content_id": "0eeef523-3806-4f08-b5d6-bd020f663708",
          "duration_ms": 41.6,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.687,
          "model_score": 0.3216,
          "style_score": 0.3991,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 60.8,
        "body": {
          "confidence": 0.6131,
          "content_id": "14ab20cb-9041-47e0-8de1-1112d3b74617",
          "duration_ms": 51.6,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8044,
          "model_score": 0.5616,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 51.9,
        "body": {
          "confidence": 0.5901,
          "content_id": "7203d6eb-0fb2-400a-b96e-4c85c63671da",
          "duration_ms": 50.2,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.9005,
          "model_score": 0.6169,
          "style_score": 0.3783,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 45.0,
        "body": {
          "confidence": 0.5542,
          "content_id": "021f7cfd-8704-473c-9479-3993f55d27e2",
          "duration_ms": 43.3,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8316,
          "model_score": 0.416,
          "style_score": 0.5735,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 43.8,
        "body": {
          "confidence": 0.5318,
          "content_id": "19dbbce2-d535-46cd-aab0-aeedcf941078",
          "duration_ms": 42.2,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.7699,
          "model_score": 0.3859,
          "style_score": 0.5833,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 54.0,
        "body": {
          "confidence": 0.6509,
          "content_id": "44fdc3c4-7224-41be-a5bb-4f38f352a77f",
          "duration_ms": 52.2,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.9304,
          "model_score": 0.5895,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 43.4,
        "body": {
          "confidence": 0.5819,
          "content_id": "1c5c1de3-f44a-4159-b387-5117325e0d13",
          "duration_ms": 41.4,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.7637,
          "model_score": 0.5065,
          "style_score": 0.575,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 43.7,
        "body": {
          "confidence": 0.3554,
          "content_id": "2038d5af-3af4-4d59-97d7-464f0908af62",
          "duration_ms": 42.1,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.5798,
          "model_score": 0.3371,
          "style_score": 0.2506,
          "verified_human": false
        }
      }
    ],
    "solo_total_ms": 496.9,
    "solo_per_item_ms": 49.7,
    "batch_per_item_ms": 54.9
  },
  "2": {
    "status": 200,
    "elapsed_ms": 342.3,
    "body": {
      "batch_id": "9594d5a9-27fe-4059-8d6a-67c9f0b667f4",
      "count": 10,
      "results": [
        {
          "confidence": 0.6825,
          "content_id": "46e81498-005b-4b1a-b0dc-92441ded1478",
          "duration_ms": 49.5,
          "guess": "unsure",
          "index": 0,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8185,
          "model_score": 0.696,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.7076,
          "content_id": "feb9afbc-9c26-4f78-b6be-8c9b41f437a4",
          "duration_ms": 56.3,
          "guess": "unsure",
          "index": 1,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.869,
          "model_score": 0.7293,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.4218,
          "content_id": "d25082f9-3ce2-44f3-82ae-540d605c3dd8",
          "duration_ms": 42.5,
          "guess": "unsure",
          "index": 2,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.687,
          "model_score": 0.3216,
          "style_score": 0.3991,
          "verified_human": false
        },
        {
          "confidence": 0.6131,
          "content_id": "1e8b6a7d-89cf-45e9-9c29-d2e09eb29456",
          "duration_ms": 50.1,
          "guess": "unsure",
          "index": 3,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8044,
          "model_score": 0.5616,
          "style_score": 0.57,
          "verified_human": false
        },
        {
          "confidence": 0.5901,
          "content_id": "ff578aca-ab77-4d1f-9979-e9e510e1b3ad",
          "duration_ms": 56.6,
          "guess": "unsure",
          "index": 4,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.9005,
          "model_score": 0.6169,
          "style_score": 0.3783,
          "verified_human": false
        },
        {
          "confidence": 0.5542,
          "content_id": "6e916a9e-8202-4c40-9948-384c8f4de1b9",
          "duration_ms": 41.5,
          "guess": "unsure",
          "index": 5,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.8316,
          "model_score": 0.416,
          "style_score": 0.5735,
          "verified_human": false
        },
        {
          "confidence": 0.5318,
          "content_id": "8928b8fd-6083-4bf9-b287-4f8c43c0bfac",
          "duration_ms": 42.8,
          "guess": "unsure",
          "index": 6,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.7699,
          "model_score": 0.3859,
          "style_score": 0.5833,
          "verified_human": false
        },
        {
          "error": "bad_request",
          "index": 7,
          "message": "'text' is required and must be a non-empty string."
        },
        {
          "error": "bad_request",
          "index": 8,
          "message": "'text' is required and must be a non-empty string."
        },
        {
          "error": "bad_request",
          "index": 9,
          "message": "'text' is required and must be a non-empty string."
        }
      ]
    }
  },
  "3": {
    "status": 400,
    "elapsed_ms": 1.3,
    "body": {
      "error": "bad_request",
      "message": "Batch of 30 items exceeds the 20-item limit."
    }
  },
  "5": {
    "non_dict_item": {
      "status": 200,
      "elapsed_ms": 1.0,
      "body": {
        "batch_id": "baa52e42-db98-41e5-a0d1-d8377201a8b1",
        "count": 1,
        "results": [
          {
            "error": "bad_request",
            "index": 0,
            "message": "Item must be a JSON object."
          }
        ]
      }
    },
    "items_not_a_list": {
      "status": 400,
      "elapsed_ms": 1.1,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    },
    "empty_items": {
      "status": 400,
      "elapsed_ms": 0.9,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    }
  }
}
```
