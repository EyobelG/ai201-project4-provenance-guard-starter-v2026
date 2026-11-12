# Batch run log — before

- Produced by: `run_batch_eval.py::main`
- Service: `app.py::batch` (Unit 9 capstone extension)
- 3 trials · 2026-11-11 22:03

Real output per trial. Targets and verdicts come from `criteria.md`.

## Trial 1

```json
{
  "1_and_4": {
    "batch": {
      "status": 200,
      "elapsed_ms": 8148.0,
      "body": {
        "batch_id": "19959aa9-6085-4609-9af1-c5a977a782d3",
        "count": 10,
        "results": [
          {
            "confidence": 0.6825,
            "content_id": "af0c9f51-beab-4964-973d-72558b93577e",
            "duration_ms": 7584.1,
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
            "content_id": "362f848f-6584-4770-9c74-522a3045423d",
            "duration_ms": 92.7,
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
            "content_id": "45267ec9-359d-419e-8a30-46421a4c114e",
            "duration_ms": 55.1,
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
            "content_id": "bb43b49a-58f7-49d3-970b-487eb02eda36",
            "duration_ms": 55.2,
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
            "content_id": "9dab9759-caca-4b5f-a633-20897a2fcf6c",
            "duration_ms": 69.5,
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
            "content_id": "56ba74d9-d9ab-41bb-97a8-dea9a4c028c0",
            "duration_ms": 48.7,
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
            "content_id": "3ab84909-1d59-4993-9aea-c3b543992a6e",
            "duration_ms": 49.8,
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
            "content_id": "122ce9cd-7c40-45fd-b401-12ebd6ca2444",
            "duration_ms": 70.8,
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
            "content_id": "432db4f8-ac88-4790-b62d-42810710348a",
            "duration_ms": 53.3,
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
            "content_id": "36866fb7-25fa-45e1-867e-a03b3758bc7c",
            "duration_ms": 56.3,
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
        "elapsed_ms": 61.7,
        "body": {
          "confidence": 0.6825,
          "content_id": "179386f7-e094-43ce-b602-52a55da23e9b",
          "duration_ms": 52.6,
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
        "elapsed_ms": 56.6,
        "body": {
          "confidence": 0.7076,
          "content_id": "8535b916-a66d-4786-b89f-95ca0dab1d2a",
          "duration_ms": 54.9,
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
        "elapsed_ms": 45.6,
        "body": {
          "confidence": 0.4218,
          "content_id": "ff0f05e7-d250-4eca-8eba-e74e0906300b",
          "duration_ms": 43.9,
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
        "elapsed_ms": 52.6,
        "body": {
          "confidence": 0.6131,
          "content_id": "625ef717-05ea-458d-90aa-b5bd92dfbba5",
          "duration_ms": 50.8,
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
        "elapsed_ms": 50.9,
        "body": {
          "confidence": 0.5901,
          "content_id": "06ddd00d-5c2e-4f92-84fa-9c98576b6aeb",
          "duration_ms": 49.3,
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
        "elapsed_ms": 47.7,
        "body": {
          "confidence": 0.5542,
          "content_id": "b2bc3feb-92e6-4a8d-8a1d-6637b5c79744",
          "duration_ms": 46.0,
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
        "elapsed_ms": 51.7,
        "body": {
          "confidence": 0.5318,
          "content_id": "5720393f-9696-41d9-ade0-59669cfabdbe",
          "duration_ms": 50.0,
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
        "elapsed_ms": 63.7,
        "body": {
          "confidence": 0.6509,
          "content_id": "f8a8fc2a-fdcb-43c8-8d39-db46b36306d7",
          "duration_ms": 61.1,
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
        "elapsed_ms": 49.0,
        "body": {
          "confidence": 0.5819,
          "content_id": "213a7579-5725-4264-8bef-840547d351f0",
          "duration_ms": 47.3,
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
        "elapsed_ms": 51.2,
        "body": {
          "confidence": 0.3554,
          "content_id": "c3d49673-753f-40cd-811c-adc5fac73191",
          "duration_ms": 49.5,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.5798,
          "model_score": 0.3371,
          "style_score": 0.2506,
          "verified_human": false
        }
      }
    ],
    "solo_total_ms": 530.7,
    "solo_per_item_ms": 53.1,
    "batch_per_item_ms": 814.8
  },
  "2": {
    "status": 200,
    "elapsed_ms": 463.3,
    "body": {
      "batch_id": "9fc0c3e3-ad96-4c2a-a4fd-7f61680406e8",
      "count": 10,
      "results": [
        {
          "confidence": 0.6825,
          "content_id": "b97169b8-0bd8-42bf-ac82-b826d9a64690",
          "duration_ms": 98.1,
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
          "content_id": "7f8e3a44-8ef0-49f2-843c-63d2586b5532",
          "duration_ms": 101.6,
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
          "content_id": "d39d5a5d-f9ba-4cea-8429-fa462233eca4",
          "duration_ms": 51.4,
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
          "content_id": "05693025-45b0-4534-a9f6-e4b3f151ffcd",
          "duration_ms": 61.2,
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
          "content_id": "291f394e-1d49-4cfb-8ff9-b534dcbe4c16",
          "duration_ms": 57.7,
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
          "content_id": "875e0b7d-22be-4bfb-b656-2f3c913f9d5e",
          "duration_ms": 46.1,
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
          "content_id": "ca96ddbf-9989-4d5f-950c-5ad6d44a6ec1",
          "duration_ms": 43.1,
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
    "elapsed_ms": 1.7,
    "body": {
      "error": "bad_request",
      "message": "Batch of 30 items exceeds the 20-item limit."
    }
  },
  "5": {
    "non_dict_item": {
      "status": 200,
      "elapsed_ms": 1.1,
      "body": {
        "batch_id": "b05eb9e0-9454-4bff-bfbd-837cf1068471",
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
      "elapsed_ms": 0.9,
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

## Trial 2

```json
{
  "1_and_4": {
    "batch": {
      "status": 200,
      "elapsed_ms": 506.2,
      "body": {
        "batch_id": "fa45c113-899d-4f12-a237-1b7996361f11",
        "count": 10,
        "results": [
          {
            "confidence": 0.6825,
            "content_id": "cbe50805-58a9-46f0-b13b-cf9ccab04fa4",
            "duration_ms": 53.9,
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
            "content_id": "c289665f-3a5f-43fc-b719-174db7036962",
            "duration_ms": 51.3,
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
            "content_id": "f18a5413-51d9-4f0c-b6d1-002850a50407",
            "duration_ms": 40.5,
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
            "content_id": "7ee878a8-b808-4a81-91ff-3d906d6776ed",
            "duration_ms": 53.7,
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
            "content_id": "042b073d-9147-46cb-9665-66c2b7d29c1a",
            "duration_ms": 67.4,
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
            "content_id": "6c3bb9c3-c51c-49eb-b124-67d55ca11c53",
            "duration_ms": 46.7,
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
            "content_id": "9148e0a9-2c5e-4540-ad50-79fff9d9c306",
            "duration_ms": 43.6,
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
            "content_id": "65eff719-a472-4b53-a472-5d78f228f702",
            "duration_ms": 55.7,
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
            "content_id": "2ecd18c3-c61f-4005-9753-a700bb42738c",
            "duration_ms": 44.2,
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
            "content_id": "ede8733d-c019-4f19-9920-f3e2994f5cc2",
            "duration_ms": 45.6,
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
        "elapsed_ms": 56.7,
        "body": {
          "confidence": 0.6825,
          "content_id": "12b3ab64-0390-4164-b754-41aedba6d71c",
          "duration_ms": 54.8,
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
        "elapsed_ms": 59.3,
        "body": {
          "confidence": 0.7076,
          "content_id": "bf6c0152-5a95-4c24-91c1-4436e4c22078",
          "duration_ms": 57.5,
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
        "elapsed_ms": 51.4,
        "body": {
          "confidence": 0.4218,
          "content_id": "f95b4c5a-8584-4feb-8ba2-d2da8a2fc2c5",
          "duration_ms": 49.5,
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
        "elapsed_ms": 58.7,
        "body": {
          "confidence": 0.6131,
          "content_id": "5fe1ce1d-be71-4596-90dd-52f387f8a11e",
          "duration_ms": 56.9,
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
        "elapsed_ms": 65.7,
        "body": {
          "confidence": 0.5901,
          "content_id": "d07b901c-5ba3-4d6a-93ef-3c0b57828769",
          "duration_ms": 63.8,
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
        "elapsed_ms": 51.9,
        "body": {
          "confidence": 0.5542,
          "content_id": "7fba62ae-f8ca-473d-a86d-a624ee4e2b8f",
          "duration_ms": 50.1,
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
        "elapsed_ms": 43.1,
        "body": {
          "confidence": 0.5318,
          "content_id": "acea5579-01dd-40ef-bcd4-ffe005115d5f",
          "duration_ms": 41.3,
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
        "elapsed_ms": 53.6,
        "body": {
          "confidence": 0.6509,
          "content_id": "b752b36f-96ef-4cd1-93b3-77d3fd7b457d",
          "duration_ms": 51.9,
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
        "elapsed_ms": 41.8,
        "body": {
          "confidence": 0.5819,
          "content_id": "ddb4c9ec-a8b3-4ab4-8fa3-8382159f22af",
          "duration_ms": 40.1,
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
        "elapsed_ms": 44.5,
        "body": {
          "confidence": 0.3554,
          "content_id": "7d1e764c-47b7-421f-bf4d-6e917ee6492d",
          "duration_ms": 42.9,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.5798,
          "model_score": 0.3371,
          "style_score": 0.2506,
          "verified_human": false
        }
      }
    ],
    "solo_total_ms": 526.7,
    "solo_per_item_ms": 52.7,
    "batch_per_item_ms": 50.6
  },
  "2": {
    "status": 200,
    "elapsed_ms": 333.7,
    "body": {
      "batch_id": "0075f6b8-68c3-4ecd-8cd4-4623ce17e8ef",
      "count": 10,
      "results": [
        {
          "confidence": 0.6825,
          "content_id": "bcbc59ac-1bb7-493d-8c96-ef43496d1d57",
          "duration_ms": 50.2,
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
          "content_id": "c2beecaa-d025-4dcd-8178-ee58ad0c5d6d",
          "duration_ms": 60.8,
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
          "content_id": "aa50e77b-19ab-43b1-94be-eaf1e1ea162e",
          "duration_ms": 40.7,
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
          "content_id": "360be685-ea9a-4a84-9db0-b74a86e00950",
          "duration_ms": 48.3,
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
          "content_id": "28c00968-e36e-4216-8c22-d6a244029e3f",
          "duration_ms": 49.4,
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
          "content_id": "92caaf5d-e05d-4d81-b300-e942a0e87468",
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
          "content_id": "80eca7ae-86ee-40d5-b022-c172cf03dcb6",
          "duration_ms": 39.8,
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
    "elapsed_ms": 1.7,
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
        "batch_id": "7b3a2153-4559-40c9-bf91-f9b8fcb429ab",
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
      "elapsed_ms": 1.7,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    },
    "empty_items": {
      "status": 400,
      "elapsed_ms": 1.5,
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
      "elapsed_ms": 465.1,
      "body": {
        "batch_id": "31c86f86-8901-4be9-aa75-f81808bf9ef7",
        "count": 10,
        "results": [
          {
            "confidence": 0.6825,
            "content_id": "c6bcdc23-b7ed-4f4f-8e50-f1da4d3dbcbf",
            "duration_ms": 49.2,
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
            "content_id": "57874705-9974-4fd7-b0a8-c7175d79766b",
            "duration_ms": 49.4,
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
            "content_id": "2525699b-81e5-4564-a7ea-4d2225961bab",
            "duration_ms": 40.4,
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
            "content_id": "2a513061-0451-47f1-890a-cc03c9aecbc3",
            "duration_ms": 50.2,
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
            "content_id": "733d17d6-c327-454b-8ae3-9325dc9c85bc",
            "duration_ms": 49.0,
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
            "content_id": "dbd697f1-ccc7-4cca-bcd9-3cbca8ca5227",
            "duration_ms": 41.4,
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
            "content_id": "9dc2ed9d-b11f-4296-a2c5-47eb21709292",
            "duration_ms": 40.9,
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
            "content_id": "cdc76ecc-1a2b-4a63-bc3c-64a8d20418ca",
            "duration_ms": 56.0,
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
            "content_id": "3353dec9-61a0-485d-87b0-ea7a2dd6a469",
            "duration_ms": 43.7,
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
            "content_id": "12a5abc4-6d36-4368-a645-c89b8c93984d",
            "duration_ms": 41.9,
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
        "elapsed_ms": 50.4,
        "body": {
          "confidence": 0.6825,
          "content_id": "d8d068d9-6a36-439d-bb77-4366c18a0a87",
          "duration_ms": 48.6,
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
        "elapsed_ms": 50.5,
        "body": {
          "confidence": 0.7076,
          "content_id": "36f7aa70-b52e-445f-8f5b-2daf914352f7",
          "duration_ms": 48.7,
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
        "elapsed_ms": 42.0,
        "body": {
          "confidence": 0.4218,
          "content_id": "5815f14d-723c-44d8-81aa-751753725de6",
          "duration_ms": 40.2,
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
        "elapsed_ms": 49.7,
        "body": {
          "confidence": 0.6131,
          "content_id": "7abffc5d-a86d-4b92-8c32-44fb75714046",
          "duration_ms": 48.0,
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
        "elapsed_ms": 50.7,
        "body": {
          "confidence": 0.5901,
          "content_id": "0aeffaae-322d-48e4-b299-ef86e9c87182",
          "duration_ms": 49.1,
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
        "elapsed_ms": 41.2,
        "body": {
          "confidence": 0.5542,
          "content_id": "f666c00b-5ed0-4fe3-839e-b750f515aede",
          "duration_ms": 39.6,
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
        "elapsed_ms": 46.1,
        "body": {
          "confidence": 0.5318,
          "content_id": "3ea16e6b-ae56-4943-bb7a-1ed9bf116218",
          "duration_ms": 44.3,
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
        "elapsed_ms": 49.1,
        "body": {
          "confidence": 0.6509,
          "content_id": "5992a856-bbad-41bd-a552-bf9a2642bba1",
          "duration_ms": 47.4,
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
        "elapsed_ms": 40.8,
        "body": {
          "confidence": 0.5819,
          "content_id": "a16efa81-c1fe-40f9-b5fa-68571a35ae3c",
          "duration_ms": 39.1,
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
        "elapsed_ms": 41.2,
        "body": {
          "confidence": 0.3554,
          "content_id": "24863167-be45-4311-891d-7efa9b27d503",
          "duration_ms": 39.5,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_score": 0.5798,
          "model_score": 0.3371,
          "style_score": 0.2506,
          "verified_human": false
        }
      }
    ],
    "solo_total_ms": 461.7,
    "solo_per_item_ms": 46.2,
    "batch_per_item_ms": 46.5
  },
  "2": {
    "status": 200,
    "elapsed_ms": 314.8,
    "body": {
      "batch_id": "bdf160e9-3141-4390-9d4e-5a7bd9e6e98c",
      "count": 10,
      "results": [
        {
          "confidence": 0.6825,
          "content_id": "0721b5db-5cb0-4ed1-a40c-c3e2f1d39b3d",
          "duration_ms": 47.5,
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
          "content_id": "9bad038e-d23d-4ff1-a20d-f112e1b612f0",
          "duration_ms": 47.9,
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
          "content_id": "bdf8de30-a288-408b-ab8b-9f4c5680b14f",
          "duration_ms": 40.0,
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
          "content_id": "8adbfce2-7017-4415-ad56-ac6b19be0dd0",
          "duration_ms": 48.4,
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
          "content_id": "858c5407-f3b7-4cee-a234-ffb328fa7b36",
          "duration_ms": 48.0,
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
          "content_id": "3ae05cf2-cbbe-4668-a552-e3b3c44c958c",
          "duration_ms": 39.9,
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
          "content_id": "aaefa551-5d0d-422f-9a4c-c26a8a7292ab",
          "duration_ms": 40.1,
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
    "elapsed_ms": 1.4,
    "body": {
      "error": "bad_request",
      "message": "Batch of 30 items exceeds the 20-item limit."
    }
  },
  "5": {
    "non_dict_item": {
      "status": 200,
      "elapsed_ms": 1.1,
      "body": {
        "batch_id": "20118ae4-1a07-4068-aa45-daf5de1d7e82",
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
      "elapsed_ms": 1.2,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    },
    "empty_items": {
      "status": 400,
      "elapsed_ms": 1.2,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    }
  }
}
```
