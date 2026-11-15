# Path A hosting attempt — Unit 9 capstone stretch.
#
# RUNNING.md's own arithmetic is still correct for a 512MB free tier
# (Render/Heroku-style PaaS): torch + GPT-2 weights don't fit. This targets
# Hugging Face Spaces' free CPU tier instead, which gives 16GB RAM — the
# constraint RUNNING.md ruled out, not this specific host.
#
# Deploy: create a Space with SDK "Docker", push this repo to it. Spaces
# sets PORT itself; HOST must be 0.0.0.0 for anything outside the box to
# reach it (see RUNNING.md, "Running it somewhere else").

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HOST=0.0.0.0
ENV AI201_DEBUG=0
ENV AI201_PRELOAD_WARMUP=1

# Hugging Face Spaces expects the app to listen on 7860 by default.
ENV PORT=7860
EXPOSE 7860

# --preload imports app:app (and runs the warm-up above) in gunicorn's
# master process, before forking workers, so the model is loaded once and
# inherited rather than re-loaded per worker or left to the first caller.
CMD ["sh", "-c", "gunicorn app:app --preload --bind 0.0.0.0:${PORT} --timeout 120 --workers 1"]
