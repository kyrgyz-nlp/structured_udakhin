FROM python:3.9

# Copy requirements first
COPY requirements.txt .

# Install everything with SSL verification disabled
RUN --mount=type=secret,id=PRODIGY_KEY \
    python -m pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip && \
    python -m pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org -r requirements.txt && \
    python -m pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host download.prodi.gy --trusted-host s3.eu-west-1.amazonaws.com prodigy==1.15.7 -f https://$(cat /run/secrets/PRODIGY_KEY)@download.prodi.gy

# Install everything with SSL verification disabled
# RUN --mount=type=secret,id=PRODIGY_KEY \
#     python -m pip install --upgrade pip && \
#     python -m pip install -r requirements.txt && \
#     python -m pip install prodigy==1.15.7 -f https://$(cat /run/secrets/PRODIGY_KEY)@download.prodi.gy

# Copy the rest in, keeping .dockerignore in mind
COPY . .
RUN chmod +x /run.sh

# Set some environment variables
ENV PRODIGY_LOGGING="basic"
ENV PRODIGY_ALLOWED_SESSIONS="user1,user2,user3,user4,user5,user6,user7,user8,user9,user10"

# Set environment variables using build-time secrets
RUN --mount=type=secret,id=PRODIGY_BASIC_AUTH_USER \
    --mount=type=secret,id=PRODIGY_BASIC_AUTH_PASS \
    echo "export PRODIGY_BASIC_AUTH_USER=$(cat /run/secrets/PRODIGY_BASIC_AUTH_USER)" >> /etc/profile.d/prodigy_env.sh && \
    echo "export PRODIGY_BASIC_AUTH_PASS=$(cat /run/secrets/PRODIGY_BASIC_AUTH_PASS)" >> /etc/profile.d/prodigy_env.sh && \
    chmod +x /etc/profile.d/prodigy_env.sh

# Expose the port number appropriate for cloud vendor
EXPOSE 8080

CMD ["bash", "-c", "source /etc/profile.d/prodigy_env.sh && ./run.sh"]
