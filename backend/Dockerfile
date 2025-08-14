###############################################################################
#  backend/Dockerfile
#
#  Minimal container for the FastAPI backend.  In Phase 1 we simply run
#  a long‑lived process to satisfy docker‑compose dependencies.  When
#  Phase 2 begins this Dockerfile will be extended to install
#  dependencies and launch the FastAPI application.
###############################################################################

FROM python:3.11-slim

# Prevent interactive prompts during package install
ENV DEBIAN_FRONTEND=noninteractive

# Set workdir
WORKDIR /app

# Copy requirements separately to leverage Docker cache and then copy
# application code.  This allows dependency installation to be cached
COPY requirements.txt ./

##
## NOTE:
## In an air‑gapped environment you must install Python packages from a
## pre‑downloaded bundle.  See docs/INSTALLATION‑WINDOWS.md for
## instructions on building the `packages/` directory offline.  The
## following two lines demonstrate how to perform an offline installation.
## Without a local package cache this step will attempt to download
## packages from the internet which is forbidden at runtime.  When
## preparing your air‑gapped environment, build the image with the
## offline installation commands uncommented and provide a `packages/`
## directory containing the wheel files.
##
# COPY packages/ /packages/
# RUN pip install --no-index --find-links=/packages -r requirements.txt

# Install dependencies.  In an offline build this line can remain
# commented out, replaced by the offline install above.
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ ./app/

# Expose the API port used by the FastAPI application
EXPOSE 8000

# Launch the FastAPI application using uvicorn.  The application
# instance is located at app.main:app.  The host is set to 0.0.0.0 so
# it is reachable from other containers.  The port must align with
# API_PORT in the environment (default 8000).
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]