# Batch run log — recheck

- Produced by: `run_batch_eval.py::main`
- Service: `app.py::batch` (Unit 9 capstone extension)
- 3 trials · 2026-11-15 18:45

Real output per trial. Targets and verdicts come from `criteria.md`.

## Trial 1

```json
{
  "1_and_4": {
    "batch": {
      "status": 200,
      "elapsed_ms": 688.7,
      "body": {
        "batch_id": "e957b5cb-489e-48f3-90da-e8f99f5480f1",
        "count": 10,
        "results": [
          {
            "confidence": 0.6825,
            "content_id": "da63d037-ee47-4301-9357-d4f1c3bc1b0b",
            "duration_ms": 98.5,
            "guess": "unsure",
            "index": 0,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.1,
            "lexical_score": 0.8185,
            "model_ms": 98.0,
            "model_score": 0.696,
            "scoring_ms": 0.1,
            "style_ms": 0.2,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.7076,
            "content_id": "b58ae746-aa1b-404e-ba3b-21230aa9c85a",
            "duration_ms": 92.3,
            "guess": "unsure",
            "index": 1,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.869,
            "model_ms": 92.1,
            "model_score": 0.7293,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.4218,
            "content_id": "2c79c15e-eaed-4840-9862-ef655be552ef",
            "duration_ms": 59.8,
            "guess": "unsure",
            "index": 2,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.687,
            "model_ms": 59.1,
            "model_score": 0.3216,
            "scoring_ms": 0.1,
            "style_ms": 0.6,
            "style_score": 0.3991,
            "verified_human": false
          },
          {
            "confidence": 0.6131,
            "content_id": "5ca322c0-4217-4679-824d-c87d79923846",
            "duration_ms": 74.6,
            "guess": "unsure",
            "index": 3,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.8044,
            "model_ms": 74.5,
            "model_score": 0.5616,
            "scoring_ms": 0.0,
            "style_ms": 0.0,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5901,
            "content_id": "e56ef0ea-c4ca-45b0-bdf4-2f99644da409",
            "duration_ms": 65.6,
            "guess": "unsure",
            "index": 4,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.9005,
            "model_ms": 65.3,
            "model_score": 0.6169,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.3783,
            "verified_human": false
          },
          {
            "confidence": 0.5542,
            "content_id": "aad1455f-cb44-4680-98df-867e47e6a286",
            "duration_ms": 55.0,
            "guess": "unsure",
            "index": 5,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.8316,
            "model_ms": 54.8,
            "model_score": 0.416,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.5735,
            "verified_human": false
          },
          {
            "confidence": 0.5318,
            "content_id": "b359f3fd-5f83-4144-945e-d5b55caaefe1",
            "duration_ms": 58.5,
            "guess": "unsure",
            "index": 6,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.7699,
            "model_ms": 58.3,
            "model_score": 0.3859,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.5833,
            "verified_human": false
          },
          {
            "confidence": 0.6509,
            "content_id": "424cb4cb-7014-4b6c-82ca-398304359f4d",
            "duration_ms": 72.3,
            "guess": "unsure",
            "index": 7,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.9304,
            "model_ms": 72.1,
            "model_score": 0.5895,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5819,
            "content_id": "f4b9d9f5-3b12-4072-8c9a-73238daef1f5",
            "duration_ms": 51.5,
            "guess": "unsure",
            "index": 8,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.7637,
            "model_ms": 51.4,
            "model_score": 0.5065,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.575,
            "verified_human": false
          },
          {
            "confidence": 0.3554,
            "content_id": "691ee70d-0db0-4173-9cbf-d7ece60f50b7",
            "duration_ms": 54.4,
            "guess": "unsure",
            "index": 9,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.5798,
            "model_ms": 54.2,
            "model_score": 0.3371,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.2506,
            "verified_human": false
          }
        ]
      }
    },
    "solo": [
      {
        "status": 200,
        "elapsed_ms": 67.9,
        "body": {
          "confidence": 0.6825,
          "content_id": "ef2aae30-794b-4405-aa42-24ae2144b55a",
          "duration_ms": 64.7,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8185,
          "model_ms": 64.5,
          "model_score": 0.696,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 69.2,
        "body": {
          "confidence": 0.7076,
          "content_id": "b59de35e-e4b7-47b3-aca8-24a0eef55b34",
          "duration_ms": 66.4,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.869,
          "model_ms": 66.3,
          "model_score": 0.7293,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 58.7,
        "body": {
          "confidence": 0.4218,
          "content_id": "ef5f22f4-81bb-4c2e-b09c-ada3005aa3a7",
          "duration_ms": 56.0,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.687,
          "model_ms": 55.8,
          "model_score": 0.3216,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.3991,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 73.4,
        "body": {
          "confidence": 0.6131,
          "content_id": "da40a521-7ec4-4593-afec-39f75f4d5b38",
          "duration_ms": 70.6,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8044,
          "model_ms": 70.5,
          "model_score": 0.5616,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 68.8,
        "body": {
          "confidence": 0.5901,
          "content_id": "03a6568d-3cc2-4925-b7d4-174595c25b39",
          "duration_ms": 66.2,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.9005,
          "model_ms": 66.0,
          "model_score": 0.6169,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.3783,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 57.2,
        "body": {
          "confidence": 0.5542,
          "content_id": "30ca97a1-9083-40d8-b353-d4a4b290b510",
          "duration_ms": 54.5,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8316,
          "model_ms": 54.3,
          "model_score": 0.416,
          "scoring_ms": 0.0,
          "style_ms": 0.1,
          "style_score": 0.5735,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 58.1,
        "body": {
          "confidence": 0.5318,
          "content_id": "c85db2d1-5594-4897-b110-c9a346289ff8",
          "duration_ms": 55.5,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.7699,
          "model_ms": 55.3,
          "model_score": 0.3859,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.5833,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 67.0,
        "body": {
          "confidence": 0.6509,
          "content_id": "6466a180-1d3b-4071-a663-eddbe6df5213",
          "duration_ms": 64.4,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.9304,
          "model_ms": 64.3,
          "model_score": 0.5895,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 55.7,
        "body": {
          "confidence": 0.5819,
          "content_id": "97882ab6-c052-4968-b708-ce6bac59d5da",
          "duration_ms": 53.2,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.7637,
          "model_ms": 53.0,
          "model_score": 0.5065,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.575,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 128.0,
        "body": {
          "confidence": 0.3554,
          "content_id": "47f9d949-653c-479b-aaa1-5d7a00d34bad",
          "duration_ms": 125.4,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.5798,
          "model_ms": 125.2,
          "model_score": 0.3371,
          "scoring_ms": 0.0,
          "style_ms": 0.1,
          "style_score": 0.2506,
          "verified_human": false
        }
      }
    ],
    "solo_total_ms": 704.0,
    "solo_per_item_ms": 70.4,
    "batch_per_item_ms": 68.9
  },
  "2": {
    "status": 200,
    "elapsed_ms": 424.4,
    "body": {
      "batch_id": "403b8ff1-0821-404c-a77c-1511bee78430",
      "count": 10,
      "results": [
        {
          "confidence": 0.6825,
          "content_id": "bad809ff-6553-43a5-94ef-937112c9939c",
          "duration_ms": 66.3,
          "guess": "unsure",
          "index": 0,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8185,
          "model_ms": 66.1,
          "model_score": 0.696,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.7076,
          "content_id": "30dac554-fd5b-42a0-b920-80e8f3d0c8b2",
          "duration_ms": 64.8,
          "guess": "unsure",
          "index": 1,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.869,
          "model_ms": 64.7,
          "model_score": 0.7293,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.4218,
          "content_id": "c6d9e3c1-f290-4544-8082-4cc65bbd53b5",
          "duration_ms": 53.5,
          "guess": "unsure",
          "index": 2,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.687,
          "model_ms": 53.3,
          "model_score": 0.3216,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.3991,
          "verified_human": false
        },
        {
          "confidence": 0.6131,
          "content_id": "081533b1-1ddb-499f-944d-12611162a534",
          "duration_ms": 65.7,
          "guess": "unsure",
          "index": 3,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8044,
          "model_ms": 65.5,
          "model_score": 0.5616,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.57,
          "verified_human": false
        },
        {
          "confidence": 0.5901,
          "content_id": "fedd6431-6a62-4346-a55d-5ecfeeeac6fc",
          "duration_ms": 64.4,
          "guess": "unsure",
          "index": 4,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.9005,
          "model_ms": 64.1,
          "model_score": 0.6169,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.3783,
          "verified_human": false
        },
        {
          "confidence": 0.5542,
          "content_id": "8eb904e5-a552-4197-b400-50b3dab86b49",
          "duration_ms": 52.4,
          "guess": "unsure",
          "index": 5,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8316,
          "model_ms": 52.2,
          "model_score": 0.416,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.5735,
          "verified_human": false
        },
        {
          "confidence": 0.5318,
          "content_id": "d1d9d18e-cfac-4e37-93a3-e6c115308ffa",
          "duration_ms": 52.7,
          "guess": "unsure",
          "index": 6,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.7699,
          "model_ms": 52.5,
          "model_score": 0.3859,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
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
    "elapsed_ms": 2.3,
    "body": {
      "error": "bad_request",
      "message": "Batch of 30 items exceeds the 20-item limit."
    }
  },
  "5": {
    "non_dict_item": {
      "status": 200,
      "elapsed_ms": 1.6,
      "body": {
        "batch_id": "2fd9cf87-3138-4944-8ce6-abaaa224c2f7",
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
      "elapsed_ms": 1.6,
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

## Trial 2

```json
{
  "1_and_4": {
    "batch": {
      "status": 200,
      "elapsed_ms": 613.8,
      "body": {
        "batch_id": "dea34de9-91de-452c-ba59-702e9d7e1b2e",
        "count": 10,
        "results": [
          {
            "confidence": 0.6825,
            "content_id": "4815f39c-e6dd-441d-941c-806748346b03",
            "duration_ms": 63.3,
            "guess": "unsure",
            "index": 0,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.8185,
            "model_ms": 63.1,
            "model_score": 0.696,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.7076,
            "content_id": "d132ce52-b5ca-4bae-aeb6-2bbb0983c4b1",
            "duration_ms": 66.7,
            "guess": "unsure",
            "index": 1,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.869,
            "model_ms": 66.5,
            "model_score": 0.7293,
            "scoring_ms": 0.0,
            "style_ms": 0.1,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.4218,
            "content_id": "bc06c5c2-ba8b-48c2-908b-9ceb926905e3",
            "duration_ms": 56.1,
            "guess": "unsure",
            "index": 2,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.687,
            "model_ms": 55.9,
            "model_score": 0.3216,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.3991,
            "verified_human": false
          },
          {
            "confidence": 0.6131,
            "content_id": "4041d2fe-d718-4aaa-a0bb-9b0b0540d3fa",
            "duration_ms": 65.9,
            "guess": "unsure",
            "index": 3,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.8044,
            "model_ms": 65.8,
            "model_score": 0.5616,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5901,
            "content_id": "710190b3-b90b-48d8-aaf1-dca62b2fc9d5",
            "duration_ms": 69.4,
            "guess": "unsure",
            "index": 4,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.9005,
            "model_ms": 69.2,
            "model_score": 0.6169,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.3783,
            "verified_human": false
          },
          {
            "confidence": 0.5542,
            "content_id": "c93c96d0-eeef-4be5-a07e-adbe0fc106bb",
            "duration_ms": 53.1,
            "guess": "unsure",
            "index": 5,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.8316,
            "model_ms": 52.9,
            "model_score": 0.416,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.5735,
            "verified_human": false
          },
          {
            "confidence": 0.5318,
            "content_id": "72763a30-f6ca-489a-955a-c035d191d49d",
            "duration_ms": 53.0,
            "guess": "unsure",
            "index": 6,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.7699,
            "model_ms": 52.8,
            "model_score": 0.3859,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.5833,
            "verified_human": false
          },
          {
            "confidence": 0.6509,
            "content_id": "bb6a1f8f-06cc-4071-b07e-f6bf31b037a1",
            "duration_ms": 71.4,
            "guess": "unsure",
            "index": 7,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.9304,
            "model_ms": 71.3,
            "model_score": 0.5895,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5819,
            "content_id": "61bd3459-6b51-4739-8316-3e6495f9476f",
            "duration_ms": 52.3,
            "guess": "unsure",
            "index": 8,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.7637,
            "model_ms": 52.1,
            "model_score": 0.5065,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.575,
            "verified_human": false
          },
          {
            "confidence": 0.3554,
            "content_id": "34c81c69-a322-4aa8-903b-bdddf972d18f",
            "duration_ms": 58.0,
            "guess": "unsure",
            "index": 9,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.5798,
            "model_ms": 57.8,
            "model_score": 0.3371,
            "scoring_ms": 0.0,
            "style_ms": 0.1,
            "style_score": 0.2506,
            "verified_human": false
          }
        ]
      }
    },
    "solo": [
      {
        "status": 200,
        "elapsed_ms": 67.0,
        "body": {
          "confidence": 0.6825,
          "content_id": "ac9032f3-0874-4ec4-8d83-e5c2f32d094d",
          "duration_ms": 64.3,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8185,
          "model_ms": 64.1,
          "model_score": 0.696,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 64.7,
        "body": {
          "confidence": 0.7076,
          "content_id": "6b7068b7-7d2a-455d-99bc-00ea94fe6242",
          "duration_ms": 62.1,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.869,
          "model_ms": 61.9,
          "model_score": 0.7293,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 57.9,
        "body": {
          "confidence": 0.4218,
          "content_id": "6c664921-aa8b-4e16-81ae-30a56fa69258",
          "duration_ms": 55.3,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.687,
          "model_ms": 55.0,
          "model_score": 0.3216,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.3991,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 67.4,
        "body": {
          "confidence": 0.6131,
          "content_id": "bd02fd70-b729-4284-8f9f-f14eb2ed0046",
          "duration_ms": 64.8,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8044,
          "model_ms": 64.7,
          "model_score": 0.5616,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 67.5,
        "body": {
          "confidence": 0.5901,
          "content_id": "408b2648-bd89-460b-b170-2a26c132f7e0",
          "duration_ms": 65.0,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.9005,
          "model_ms": 64.8,
          "model_score": 0.6169,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.3783,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 57.4,
        "body": {
          "confidence": 0.5542,
          "content_id": "f08f2c51-2568-47ee-8a7d-98c7c330590b",
          "duration_ms": 54.9,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8316,
          "model_ms": 54.7,
          "model_score": 0.416,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.5735,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 56.2,
        "body": {
          "confidence": 0.5318,
          "content_id": "8499a145-2ca6-41dd-82a5-2d4267db8cab",
          "duration_ms": 53.7,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.7699,
          "model_ms": 53.5,
          "model_score": 0.3859,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.5833,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 67.6,
        "body": {
          "confidence": 0.6509,
          "content_id": "4c2aafe8-fa90-4e9a-aadf-2a0a706bc46b",
          "duration_ms": 65.0,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.9304,
          "model_ms": 64.8,
          "model_score": 0.5895,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 58.1,
        "body": {
          "confidence": 0.5819,
          "content_id": "f073e78e-7fb7-4c0d-846d-7330b73dc75b",
          "duration_ms": 55.6,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.7637,
          "model_ms": 55.5,
          "model_score": 0.5065,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.575,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 53.0,
        "body": {
          "confidence": 0.3554,
          "content_id": "3533cdb6-eff0-4ae7-ad01-8e69c8d5f24e",
          "duration_ms": 50.5,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.5798,
          "model_ms": 50.3,
          "model_score": 0.3371,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.2506,
          "verified_human": false
        }
      }
    ],
    "solo_total_ms": 616.8,
    "solo_per_item_ms": 61.7,
    "batch_per_item_ms": 61.4
  },
  "2": {
    "status": 200,
    "elapsed_ms": 429.1,
    "body": {
      "batch_id": "7dfd81eb-3e02-4f51-bdb3-c05d0859cece",
      "count": 10,
      "results": [
        {
          "confidence": 0.6825,
          "content_id": "66863e47-197a-4691-8394-885167aefe1d",
          "duration_ms": 67.9,
          "guess": "unsure",
          "index": 0,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8185,
          "model_ms": 67.7,
          "model_score": 0.696,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.7076,
          "content_id": "29d1a077-beec-4dfc-9fa6-2482e69ed1cb",
          "duration_ms": 66.5,
          "guess": "unsure",
          "index": 1,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.869,
          "model_ms": 66.3,
          "model_score": 0.7293,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.4218,
          "content_id": "8de509d2-4271-4b19-b7f6-dc4f9e63a20a",
          "duration_ms": 54.2,
          "guess": "unsure",
          "index": 2,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.687,
          "model_ms": 53.9,
          "model_score": 0.3216,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.3991,
          "verified_human": false
        },
        {
          "confidence": 0.6131,
          "content_id": "94d91a90-49d7-4c7f-a10d-8c696957c05f",
          "duration_ms": 64.4,
          "guess": "unsure",
          "index": 3,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8044,
          "model_ms": 64.2,
          "model_score": 0.5616,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.57,
          "verified_human": false
        },
        {
          "confidence": 0.5901,
          "content_id": "abac846b-d486-40ec-85a3-66982be34560",
          "duration_ms": 65.6,
          "guess": "unsure",
          "index": 4,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.9005,
          "model_ms": 65.4,
          "model_score": 0.6169,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.3783,
          "verified_human": false
        },
        {
          "confidence": 0.5542,
          "content_id": "34836807-cbc4-4a3b-8eb9-2a0064d09b3f",
          "duration_ms": 51.9,
          "guess": "unsure",
          "index": 5,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8316,
          "model_ms": 51.7,
          "model_score": 0.416,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.5735,
          "verified_human": false
        },
        {
          "confidence": 0.5318,
          "content_id": "9f0bc2a9-0e3b-4d31-9287-2577addabc2a",
          "duration_ms": 54.2,
          "guess": "unsure",
          "index": 6,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.7699,
          "model_ms": 54.1,
          "model_score": 0.3859,
          "scoring_ms": 0.0,
          "style_ms": 0.0,
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
    "elapsed_ms": 2.2,
    "body": {
      "error": "bad_request",
      "message": "Batch of 30 items exceeds the 20-item limit."
    }
  },
  "5": {
    "non_dict_item": {
      "status": 200,
      "elapsed_ms": 1.8,
      "body": {
        "batch_id": "fca8dfc8-e461-4a67-ba1c-5ad23c634001",
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
      "elapsed_ms": 1.6,
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
      "elapsed_ms": 592.8,
      "body": {
        "batch_id": "e6cb729d-d711-4c6d-8f53-5694057da137",
        "count": 10,
        "results": [
          {
            "confidence": 0.6825,
            "content_id": "c85ac88b-807f-479d-9291-c2718414476e",
            "duration_ms": 62.0,
            "guess": "unsure",
            "index": 0,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.8185,
            "model_ms": 61.9,
            "model_score": 0.696,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.7076,
            "content_id": "d2c5522a-c217-452a-ab3c-d9d0543289ee",
            "duration_ms": 66.0,
            "guess": "unsure",
            "index": 1,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.869,
            "model_ms": 65.8,
            "model_score": 0.7293,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.5875,
            "verified_human": false
          },
          {
            "confidence": 0.4218,
            "content_id": "fd2e209c-a298-4325-b5fb-93dae530169f",
            "duration_ms": 52.9,
            "guess": "unsure",
            "index": 2,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.687,
            "model_ms": 52.7,
            "model_score": 0.3216,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.3991,
            "verified_human": false
          },
          {
            "confidence": 0.6131,
            "content_id": "17e0eff3-6cd6-45c5-89d8-9c0f46a75ca4",
            "duration_ms": 62.6,
            "guess": "unsure",
            "index": 3,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.8044,
            "model_ms": 62.4,
            "model_score": 0.5616,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5901,
            "content_id": "e2a6c517-9ad1-4c49-b283-8d290b33bd4b",
            "duration_ms": 64.4,
            "guess": "unsure",
            "index": 4,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.9005,
            "model_ms": 64.2,
            "model_score": 0.6169,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.3783,
            "verified_human": false
          },
          {
            "confidence": 0.5542,
            "content_id": "43957e18-9450-4df1-8303-c0875518eb87",
            "duration_ms": 55.3,
            "guess": "unsure",
            "index": 5,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.8316,
            "model_ms": 55.1,
            "model_score": 0.416,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.5735,
            "verified_human": false
          },
          {
            "confidence": 0.5318,
            "content_id": "71c91857-d7d2-4b23-af44-de99e2878771",
            "duration_ms": 51.8,
            "guess": "unsure",
            "index": 6,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.7699,
            "model_ms": 51.7,
            "model_score": 0.3859,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.5833,
            "verified_human": false
          },
          {
            "confidence": 0.6509,
            "content_id": "4fe16e4e-bb75-4a86-baac-e8cdaf7473f8",
            "duration_ms": 64.9,
            "guess": "unsure",
            "index": 7,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.9304,
            "model_ms": 64.7,
            "model_score": 0.5895,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.57,
            "verified_human": false
          },
          {
            "confidence": 0.5819,
            "content_id": "bda5fb45-2909-4aec-a28d-2d2f9d2b53f2",
            "duration_ms": 55.7,
            "guess": "unsure",
            "index": 8,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.7637,
            "model_ms": 55.6,
            "model_score": 0.5065,
            "scoring_ms": 0.1,
            "style_ms": 0.0,
            "style_score": 0.575,
            "verified_human": false
          },
          {
            "confidence": 0.3554,
            "content_id": "530a8623-811c-41de-aea4-371d67e15bfd",
            "duration_ms": 52.6,
            "guess": "unsure",
            "index": 9,
            "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
            "lexical_ms": 0.0,
            "lexical_score": 0.5798,
            "model_ms": 52.4,
            "model_score": 0.3371,
            "scoring_ms": 0.1,
            "style_ms": 0.1,
            "style_score": 0.2506,
            "verified_human": false
          }
        ]
      }
    },
    "solo": [
      {
        "status": 200,
        "elapsed_ms": 67.4,
        "body": {
          "confidence": 0.6825,
          "content_id": "1586b8f6-e9c5-4447-bd99-0eb1b0fe399b",
          "duration_ms": 64.6,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8185,
          "model_ms": 64.4,
          "model_score": 0.696,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 67.4,
        "body": {
          "confidence": 0.7076,
          "content_id": "250cdda7-419c-467e-a3db-841867bfb746",
          "duration_ms": 64.9,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.869,
          "model_ms": 64.7,
          "model_score": 0.7293,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.5875,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 56.5,
        "body": {
          "confidence": 0.4218,
          "content_id": "4ee52676-6744-4a9d-a414-48d11def8c54",
          "duration_ms": 53.9,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.687,
          "model_ms": 53.7,
          "model_score": 0.3216,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.3991,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 68.0,
        "body": {
          "confidence": 0.6131,
          "content_id": "ab4ff821-4a6a-4025-8270-e47d17a579b2",
          "duration_ms": 65.3,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8044,
          "model_ms": 65.2,
          "model_score": 0.5616,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 67.7,
        "body": {
          "confidence": 0.5901,
          "content_id": "f5270e83-8209-4221-a2a6-868516f692c0",
          "duration_ms": 65.0,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.9005,
          "model_ms": 64.8,
          "model_score": 0.6169,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.3783,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 58.2,
        "body": {
          "confidence": 0.5542,
          "content_id": "6162280a-9084-4b0f-a152-4a1ea720fe4b",
          "duration_ms": 55.6,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8316,
          "model_ms": 55.4,
          "model_score": 0.416,
          "scoring_ms": 0.0,
          "style_ms": 0.1,
          "style_score": 0.5735,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 59.5,
        "body": {
          "confidence": 0.5318,
          "content_id": "73283a57-3c59-4d50-bae4-4bd0edca2956",
          "duration_ms": 56.6,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.7699,
          "model_ms": 56.4,
          "model_score": 0.3859,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.5833,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 63.1,
        "body": {
          "confidence": 0.6509,
          "content_id": "b02981a6-3405-460f-b7d7-7e2ed88df0d8",
          "duration_ms": 60.5,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.9304,
          "model_ms": 60.4,
          "model_score": 0.5895,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.57,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 51.9,
        "body": {
          "confidence": 0.5819,
          "content_id": "8381a2b5-e2f3-4502-8e62-468d6dd700d1",
          "duration_ms": 49.4,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.7637,
          "model_ms": 49.2,
          "model_score": 0.5065,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.575,
          "verified_human": false
        }
      },
      {
        "status": 200,
        "elapsed_ms": 57.5,
        "body": {
          "confidence": 0.3554,
          "content_id": "1673a01c-b54c-408b-ada6-f2e9071acaeb",
          "duration_ms": 54.9,
          "guess": "unsure",
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.5798,
          "model_ms": 54.6,
          "model_score": 0.3371,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.2506,
          "verified_human": false
        }
      }
    ],
    "solo_total_ms": 617.2,
    "solo_per_item_ms": 61.7,
    "batch_per_item_ms": 59.3
  },
  "2": {
    "status": 200,
    "elapsed_ms": 528.8,
    "body": {
      "batch_id": "926291c0-c0a5-414c-a049-29d09eb96cca",
      "count": 10,
      "results": [
        {
          "confidence": 0.6825,
          "content_id": "45084cf1-6188-4705-b8b4-c59a3c977085",
          "duration_ms": 65.1,
          "guess": "unsure",
          "index": 0,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8185,
          "model_ms": 65.0,
          "model_score": 0.696,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.7076,
          "content_id": "646bdd4b-befa-432f-944e-85d09ea65be9",
          "duration_ms": 67.8,
          "guess": "unsure",
          "index": 1,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.869,
          "model_ms": 67.6,
          "model_score": 0.7293,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
          "style_score": 0.5875,
          "verified_human": false
        },
        {
          "confidence": 0.4218,
          "content_id": "a4cf59b8-5531-40ce-b8bd-d1fae8bf4186",
          "duration_ms": 58.1,
          "guess": "unsure",
          "index": 2,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.1,
          "lexical_score": 0.687,
          "model_ms": 57.8,
          "model_score": 0.3216,
          "scoring_ms": 0.1,
          "style_ms": 0.2,
          "style_score": 0.3991,
          "verified_human": false
        },
        {
          "confidence": 0.6131,
          "content_id": "c3ec97c7-88d5-4ef1-a224-16cb4c180c91",
          "duration_ms": 66.5,
          "guess": "unsure",
          "index": 3,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.8044,
          "model_ms": 66.4,
          "model_score": 0.5616,
          "scoring_ms": 0.1,
          "style_ms": 0.0,
          "style_score": 0.57,
          "verified_human": false
        },
        {
          "confidence": 0.5901,
          "content_id": "9481f99b-8cab-4e15-a9da-2121517c6af8",
          "duration_ms": 87.9,
          "guess": "unsure",
          "index": 4,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.9005,
          "model_ms": 87.3,
          "model_score": 0.6169,
          "scoring_ms": 0.1,
          "style_ms": 0.3,
          "style_score": 0.3783,
          "verified_human": false
        },
        {
          "confidence": 0.5542,
          "content_id": "f6454430-e5b6-408c-aee0-a193316b0843",
          "duration_ms": 79.9,
          "guess": "unsure",
          "index": 5,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.4,
          "lexical_score": 0.8316,
          "model_ms": 78.9,
          "model_score": 0.416,
          "scoring_ms": 0.1,
          "style_ms": 0.4,
          "style_score": 0.5735,
          "verified_human": false
        },
        {
          "confidence": 0.5318,
          "content_id": "88de0737-f86f-4d74-870b-fe4b7f2c31ec",
          "duration_ms": 98.1,
          "guess": "unsure",
          "index": 6,
          "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you \u2014 if you wrote it yourself, you're welcome to appeal so a person can take a closer look.",
          "lexical_ms": 0.0,
          "lexical_score": 0.7699,
          "model_ms": 97.8,
          "model_score": 0.3859,
          "scoring_ms": 0.1,
          "style_ms": 0.1,
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
    "elapsed_ms": 2.6,
    "body": {
      "error": "bad_request",
      "message": "Batch of 30 items exceeds the 20-item limit."
    }
  },
  "5": {
    "non_dict_item": {
      "status": 200,
      "elapsed_ms": 1.7,
      "body": {
        "batch_id": "17661b33-a457-460a-bded-e7ce71c4e63d",
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
      "elapsed_ms": 1.5,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    },
    "empty_items": {
      "status": 400,
      "elapsed_ms": 1.6,
      "body": {
        "error": "bad_request",
        "message": "'items' is required and must be a non-empty JSON array."
      }
    }
  }
}
```
